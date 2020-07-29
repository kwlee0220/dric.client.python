
import logging
import grpc
import paho.mqtt.client as mqtt
from . import marmot_type_pb2 as type_pb
from . import marmot_dataset_pb2 as dataset_pb
from . import marmot_dataset_pb2_grpc as dataset_grpc
from .types import Envelope, Coordinate, RecordSchema, Record
from .proto_utils import handle_pb_error, from_value_proto, handle_string_response
from .client import dataset_server_stub

logger = logging.getLogger('dric.dataset')

def get_dataset(ds_id):
    req = type_pb.StringProto(value=ds_id)
    resp = dataset_server_stub().getDataSetInfo(req)
    return handle_dataset_info(resp)
    
def get_dataset_all():
    req = type_pb.VoidProto()
    for resp in dataset_server_stub().getDataSetInfoAll(req):
        yield handle_dataset_info(resp)
        
def get_dataset_all_in_dir(start, recur):
    req = dataset_pb.DirectoryTraverseRequest(directory=start, recursive=recur)
    for resp in dataset_server_stub().getDataSetInfoAllInDir(req):
        yield handle_dataset_info(resp)

def get_dir_all():
    req = type_pb.VoidProto()
    for resp in dataset_server_stub().getDirAll(req):
        yield handle_string_response(resp)

def get_sub_dir_all(start, recur):
    req = dataset_pb.DirectoryTraverseRequest(directory=start, recursive=recur)
    for resp in dataset_server_stub().getSubDirAll(req):
        yield handle_string_response(resp)

def read_dataset(ds_id):
    ds = get_dataset(ds_id)
    if ds.type == dataset_pb.MQTT:
        raise ValueError("unsupport dataset type: %s" % ds.type)

    req = type_pb.StringProto(value = ds_id)
    return RecordStream(ds.schema, dataset_server_stub().readDataSet2(req))

class DataSet:
    def __init__(self, ds_info):
        self.ds_info = ds_info
        schema_id = ds_info.record_schema
        self.schema = RecordSchema.from_type_id(schema_id)

    def __getattr__(self, name):
        if name == 'id':
            return self.ds_info.id
        elif name == 'type':
            return self.ds_info.type
        elif name == 'record_schema':
            return self.schema
        elif name == 'record_count':
            return self.ds_info.count
        elif name == 'bounds':
            if self.ds_info.WhichOneof('optional_bounds') == 'bounds':
                envl = self.ds_info.bounds
                return Envelope(Coordinate(envl.tl.x, envl.tl.y), Coordinate(envl.br.x, envl.br.y))
            else:
                return None
        elif name == 'parameter':
            return self.ds_info.parameter
        else:
            raise ValueError("unknown attribute: " + name)

    def read(self):
        return read_dataset(self.ds_info.id)

    def __str__(self):
        return '%s:%d:%s' % (self.ds_info.id, self.ds_info.count, str(self.schema))


class RecordStream:
    def __init__(self, schema, rec_iter):
        self.schema = schema
        self.rec_iter = rec_iter

    def __iter__(self):
        for rec_resp in self.rec_iter:
            values = self.__handle_record_response(rec_resp, self.schema)
            yield Record(self.schema, values)

    def __handle_record_response(self, resp, schema):
        case = resp.WhichOneof('either')
        if case == 'error':
            handle_pb_error(resp.error)
        else:
            values = resp.record.column
            return tuple(from_value_proto(values[col.ordinal]) for col in schema.columns)

def handle_dataset_info(resp):
    case = resp.WhichOneof('either')
    if case == 'error':
        handle_pb_error(resp.error)
    else:
        return DataSet(resp.dataset_info)

# NAME_TO_GEOMETRY_TYPES = {
#     'POINT': POINT, 'MULTI_POINT': MULTI_POINT,
#     'LINESTRING': LINESTRING, 'MULTI_LINESTRING': MULTI_LINESTRING,
#     'POLYGON': POLYGON, 'MULTI_POLYGON': MULTI_POLYGON,
#     'GEOM_COLLECTION': GEOM_COLLECTION, 'GEOMETRY': GEOMETRY }

# def from_avro_value(type, avro_value):
#     if type.isPrimitiveType():
#         return avro_value
#     if type.isGeometryType():
#         return loads(wkb)

# class AvroFileDataSet(DataSet):

#     def __init__(self, path):
#         self.path = path

#     def read(self):
#         with open(self.path, 'rb') as fo:
#             avro_reader = reader(fo)
#             schema = self.__to_schema(avro_reader.writer_schema)
#             for record in avro_reader:
#                 [from_avro_value(col.type, record[col.name]) for col in schema]

#     def __to_schema(self, avro_schema):
#         builder = RecordSchemaBuilder()
#         for field in avro_schema['fields']:
#             builder.add(field['name'], self.fromAvroType(field['type']))
#         return builder.build()

#     @staticmethod
#     def fromAvroType(name):
#         if ( isinstance(name, str) ):
#             type = AvroFileDataSet.NAME_TO_TYPE[name.upper()]
#             if type:
#                 return type
#         return None
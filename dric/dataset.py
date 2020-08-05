
import logging
from . import pb2
from .types import Envelope, Coordinate, RecordSchema, Record
from .proto_utils import get_either, from_value_proto, handle_pb_error#, handle_string_response

class DataSet:
    import logging
    __logger = logging.getLogger("marmot.dataset")
    __logger.setLevel(logging.WARN)
    __logger.addHandler(logging.StreamHandler())

    def __init__(self, stub, ds_info):
        self.stub = stub
        self.ds_info = ds_info
        schema_id = ds_info.record_schema
        self.schema = RecordSchema.from_type_id(schema_id)

    @property
    def id(self):
        return self.ds_info.id
    @property
    def type(self):
        return self.ds_info.type
    @property
    def record_schema(self):
        return self.schema
    @property
    def record_count(self):
        return self.ds_info.count
    @property
    def bounds(self):
        envl = get_either(self.ds_info, 'bounds')
        if envl:
            return Envelope(Coordinate(envl.tl.x, envl.tl.y), Coordinate(envl.br.x, envl.br.y))
        else:
            return None
    @property
    def parameter(self):
        return self.ds_info.parameter

    def read(self):
        if self.ds_info.type == pb2.dataset.MQTT:
            raise ValueError("unsupport dataset type: %s" % self.ds_info.type)
        req = pb2.type.StringProto(value = self.ds_info.id)
        return RecordStream(self.schema, self.stub.readDataSet2(req))

    def __str__(self):
        return '%s:%d:%s' % (self.ds_info.id, self.ds_info.count, str(self.schema))

class RecordStream:
    def __init__(self, schema, rec_iter):
        self.schema = schema
        self.rec_iter = rec_iter

    @property
    def record_schema(self):
        return self.schema

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

from io import BytesIO
import paho.mqtt.client as mqtt
from fastavro import parse_schema, schemaless_reader, schemaless_writer
class MqttDataSet(DataSet):
    def __init__(self, stub, ds_info):
        super().__init__(stub, ds_info)

        parts = self.parameter.split(":")
        self.broker_host = parts[0]
        self.broker_port = int(parts[1])
        self.topic = parts[2]
        self.parsed_schema = parse_schema(self.schema.avro_schema)

    def read(self):
        return TopicRecordStream(self.schema, self.parsed_schema, self.broker_host, self.broker_port, self.topic)

    def open_writer(self):
        mqtt_client = mqtt.Client()
        mqtt_client.connect(self.broker_host, self.broker_port)
        return MqttRecordStreamWriter(mqtt_client, self.topic, self.parsed_schema)

class MqttRecordStreamWriter:
    def __init__(self, mqtt, topic, parsed_schema):
        self.parsed_schema = parsed_schema
        self.mqtt = mqtt
        self.topic = topic
        self.qos = 0
        self.retain = 0
        self.count = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        return False

    def write(self, record):
        with BytesIO() as fo:
            schemaless_writer(fo, self.parsed_schema, record.to_dict())
            self.count += 1
            fo.flush()
            self.mqtt.publish(self.topic, fo.getvalue(), self.qos, self.retain)

class TopicRecordStream:
    def __init__(self, schema, parsed_schema, broker_host, broker_port, topic_name):
        self.schema = schema
        self.parsed_schema = parsed_schema

        import threading, queue
        self.cv = threading.Condition()
        self.msg_queue = queue.Queue()

        import paho.mqtt.client as mqtt
        from .mqtt import MqttTopic
        topic = MqttTopic(broker_host, broker_port, topic_name)
        topic.subscribe_async(self.on_message)

    def __iter__(self):
        return self

    @property
    def record_schema(self):
        return self.schema

    def __next__(self):
        with self.cv:
            while 1:
                if self.msg_queue.qsize() > 0:
                    rec_bytes = self.msg_queue.get()
                    with BytesIO(rec_bytes) as fo:
                        grec = schemaless_reader(fo, self.parsed_schema)
                        return Record.read_generic_record(grec, self.schema)
                else:
                    self.cv.wait()

    def on_message(self, bytes):
        with self.cv:
            if self.msg_queue.qsize() < 16:
                self.msg_queue.put(bytes)
                self.cv.notify()
            else:
                print("lost message!!!!!")

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
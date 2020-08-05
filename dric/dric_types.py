from fastavro import parse_schema, schemaless_reader, schemaless_writer
from io import BytesIO
from .types import *

class AvroSerializable:
    @classmethod
    def from_bytes(cls, bytes):
        fo = BytesIO(bytes)
        grec = schemaless_reader(fo, cls.PARSED_AVRO_SCHEMA)
        return Record.read_generic_record(grec, cls.SCHEMA)

    def to_bytes(self):
        pass
        

class CameraFrame(AvroSerializable):
    SCHEMA = RecordSchemaBuilder()   \
                    .add('camera_id', STRING)   \
                    .add('image', BINARY)    \
                    .add('ts', LONG) \
                    .build()
    PARSED_AVRO_SCHEMA = parse_schema(SCHEMA.avro_schema)

    def __init__(self, camera_id, image, ts):
        from .utils import to_bstring_from_mat
        bstr = to_bstring_from_mat(image)
        epoch = int(round(ts * 1000))
        self.record = Record(CameraFrame.SCHEMA, (camera_id, bstr, epoch))

    def to_generic_record(self):
        grec = dict(self.record)
        return grec

    def to_bytes(self):
        with BytesIO() as fo:
            schemaless_writer(fo, CameraFrame.PARSED_AVRO_SCHEMA, self.to_generic_record())
            fo.flush()
            return fo.getvalue()

    def __str__(self):
        return '{0}[id={1}, image.size={2}, ts={3}'.format(type(self).__name__, self.camera_id,
                                                            len(self.image), self.ts)

class ObjectBBoxTrack:
    SCHEMA = RecordSchemaBuilder()   \
                    .add('camera_id', STRING)   \
                    .add('luid', STRING) \
                    .add('bbox', ENVELOPE)   \
                    .add('heading', FLOAT)   \
                    .add('ts', LONG) \
                    .build()
    PARSED_AVRO_SCHEMA = parse_schema(SCHEMA.avro_schema)

    def __init__(self, camera_id, luid, bbox, heading, ts):
        self.camera_id = camera_id
        self.luid = luid
        self.bbox = bbox
        self.heading = heading
        self.ts = ts

class ObjectTrack:
    SCHEMA = RecordSchemaBuilder()   \
                    .add('camera_id', STRING)   \
                    .add('luid', STRING) \
                    .add('lonlat', POINT('EPSG:4326'))   \
                    .add('azimuth', FLOAT)   \
                    .add('ts', LONG) \
                    .build()
    PARSED_AVRO_SCHEMA = parse_schema(SCHEMA.avro_schema)

    def __init__(self, camera_id, luid, lonlat, azimuth, ts):
        self.camera_id = camera_id
        self.luid = luid
        self.lonlat = lonlat
        self.azimuth = azimuth
        self.ts = ts
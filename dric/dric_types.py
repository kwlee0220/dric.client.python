from fastavro import parse_schema, schemaless_reader
from io import BytesIO
from .types import *

class AvroSerializable:
    @classmethod
    def from_bytes(cls, bytes):
        fo = BytesIO(bytes)
        grec = schemaless_reader(fo, cls.PARSED_AVRO_SCHEMA)
        return Record.read_generic_record(grec, cls.SCHEMA)

class CameraFrame(AvroSerializable):
    SCHEMA = RecordSchemaBuilder()   \
                    .add('camera_id', STRING)   \
                    .add('image', BINARY)    \
                    .add('ts', LONG) \
                    .build()
    PARSED_AVRO_SCHEMA = parse_schema(SCHEMA.avro_schema)

    def __init__(self, camera_id, image, ts):
        self.camera_id = camera_id
        self.image = image
        self.ts = ts

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
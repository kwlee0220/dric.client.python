# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dric.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import marmot_type_pb2 as marmot__type__pb2

from .marmot_type_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='dric.proto',
  package='dric.proto',
  syntax='proto3',
  serialized_options=b'\n\ndric.protoP\001',
  serialized_pb=b'\n\ndric.proto\x12\ndric.proto\x1a\x11marmot_type.proto\"&\n\x08\x45ndPoint\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"r\n\x10\x45ndPointResponse\x12)\n\tend_point\x18\x01 \x01(\x0b\x32\x14.dric.proto.EndPointH\x00\x12)\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x18.marmot.proto.ErrorProtoH\x00\x42\x08\n\x06\x65ither\"k\n\x0cJdbcEndPoint\x12\x0e\n\x06system\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x0f\n\x07\x64\x62_name\x18\x04 \x01(\t\x12\x0c\n\x04user\x18\x05 \x01(\t\x12\x10\n\x08password\x18\x06 \x01(\t\"*\n\nCameraInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08rtsp_url\x18\x02 \x01(\t\"x\n\x12\x43\x61meraInfoResponse\x12-\n\x0b\x63\x61mera_info\x18\x01 \x01(\x0b\x32\x16.dric.proto.CameraInfoH\x00\x12)\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x18.marmot.proto.ErrorProtoH\x00\x42\x08\n\x06\x65ither\",\n\x14ImageCoordinateProto\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"\'\n\x0f\x43oordinateProto\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\"n\n\x10\x42oundingBoxProto\x12,\n\x02tl\x18\x01 \x01(\x0b\x32 .dric.proto.ImageCoordinateProto\x12,\n\x02\x62r\x18\x02 \x01(\x0b\x32 .dric.proto.ImageCoordinateProto\"@\n\x10\x43\x61meraFrameProto\x12\x11\n\tcamera_id\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\x0c\x12\n\n\x02ts\x18\x03 \x01(\x03\"\x96\x01\n\x14ObjectBBoxTrackProto\x12\x11\n\tcamera_id\x18\x01 \x01(\t\x12\x0c\n\x04luid\x18\x02 \x01(\t\x12\x14\n\x0cobject_class\x18\x03 \x01(\t\x12*\n\x04\x62\x62ox\x18\x04 \x01(\x0b\x32\x1c.dric.proto.BoundingBoxProto\x12\x0f\n\x07heading\x18\x05 \x01(\x02\x12\n\n\x02ts\x18\x06 \x01(\x03\"\x97\x01\n\x10ObjectTrackProto\x12\x11\n\tcamera_id\x18\x01 \x01(\t\x12\x0c\n\x04luid\x18\x02 \x01(\t\x12\x14\n\x0cobject_class\x18\x03 \x01(\t\x12/\n\ncoordinate\x18\x04 \x01(\x0b\x32\x1b.dric.proto.CoordinateProto\x12\x0f\n\x07\x61zimuth\x18\x05 \x01(\x02\x12\n\n\x02ts\x18\x06 \x01(\x03\"9\n\rRotationProto\x12\x0b\n\x03yaw\x18\x01 \x01(\x01\x12\r\n\x05pitch\x18\x02 \x01(\x01\x12\x0c\n\x04roll\x18\x03 \x01(\x01\"3\n\x12\x43\x61meraFrameRequest\x12\x11\n\tcamera_id\x18\x01 \x01(\t\x12\n\n\x02ts\x18\x02 \x01(\x03\"y\n\x13\x43\x61meraFrameResponse\x12-\n\x05\x66rame\x18\x01 \x01(\x0b\x32\x1c.dric.proto.CameraFrameProtoH\x00\x12)\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x18.marmot.proto.ErrorProtoH\x00\x42\x08\n\x06\x65ither\"O\n\x17\x43\x61meraFrameRangeRequest\x12\x11\n\tcamera_id\x18\x01 \x01(\t\x12\x10\n\x08start_ts\x18\x02 \x01(\x03\x12\x0f\n\x07stop_ts\x18\x03 \x01(\x03\x32]\n\x0c\x44rICPlatform\x12M\n\x12getServiceEndPoint\x12\x19.marmot.proto.StringProto\x1a\x1c.dric.proto.EndPointResponse2\x0f\n\rDrICDataStore2\xac\x02\n\x0f\x44rICVideoServer\x12?\n\taddCamera\x12\x16.dric.proto.CameraInfo\x1a\x1a.marmot.proto.VoidResponse\x12\x45\n\x0cremoveCamera\x12\x19.marmot.proto.StringProto\x1a\x1a.marmot.proto.VoidResponse\x12\x46\n\tgetCamera\x12\x19.marmot.proto.StringProto\x1a\x1e.dric.proto.CameraInfoResponse\x12I\n\x0cgetCameraAll\x12\x17.marmot.proto.VoidProto\x1a\x1e.dric.proto.CameraInfoResponse0\x01\x42\x0e\n\ndric.protoP\x01P\x00\x62\x06proto3'
  ,
  dependencies=[marmot__type__pb2.DESCRIPTOR,],
  public_dependencies=[marmot__type__pb2.DESCRIPTOR,])




_ENDPOINT = _descriptor.Descriptor(
  name='EndPoint',
  full_name='dric.proto.EndPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='dric.proto.EndPoint.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='dric.proto.EndPoint.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=83,
)


_ENDPOINTRESPONSE = _descriptor.Descriptor(
  name='EndPointResponse',
  full_name='dric.proto.EndPointResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='end_point', full_name='dric.proto.EndPointResponse.end_point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dric.proto.EndPointResponse.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='either', full_name='dric.proto.EndPointResponse.either',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=85,
  serialized_end=199,
)


_JDBCENDPOINT = _descriptor.Descriptor(
  name='JdbcEndPoint',
  full_name='dric.proto.JdbcEndPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='system', full_name='dric.proto.JdbcEndPoint.system', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='dric.proto.JdbcEndPoint.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='dric.proto.JdbcEndPoint.port', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='db_name', full_name='dric.proto.JdbcEndPoint.db_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='dric.proto.JdbcEndPoint.user', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='dric.proto.JdbcEndPoint.password', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=201,
  serialized_end=308,
)


_CAMERAINFO = _descriptor.Descriptor(
  name='CameraInfo',
  full_name='dric.proto.CameraInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dric.proto.CameraInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rtsp_url', full_name='dric.proto.CameraInfo.rtsp_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=310,
  serialized_end=352,
)


_CAMERAINFORESPONSE = _descriptor.Descriptor(
  name='CameraInfoResponse',
  full_name='dric.proto.CameraInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='camera_info', full_name='dric.proto.CameraInfoResponse.camera_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dric.proto.CameraInfoResponse.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='either', full_name='dric.proto.CameraInfoResponse.either',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=354,
  serialized_end=474,
)


_IMAGECOORDINATEPROTO = _descriptor.Descriptor(
  name='ImageCoordinateProto',
  full_name='dric.proto.ImageCoordinateProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='dric.proto.ImageCoordinateProto.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='dric.proto.ImageCoordinateProto.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=476,
  serialized_end=520,
)


_COORDINATEPROTO = _descriptor.Descriptor(
  name='CoordinateProto',
  full_name='dric.proto.CoordinateProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='dric.proto.CoordinateProto.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='dric.proto.CoordinateProto.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=522,
  serialized_end=561,
)


_BOUNDINGBOXPROTO = _descriptor.Descriptor(
  name='BoundingBoxProto',
  full_name='dric.proto.BoundingBoxProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tl', full_name='dric.proto.BoundingBoxProto.tl', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='br', full_name='dric.proto.BoundingBoxProto.br', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=563,
  serialized_end=673,
)


_CAMERAFRAMEPROTO = _descriptor.Descriptor(
  name='CameraFrameProto',
  full_name='dric.proto.CameraFrameProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='camera_id', full_name='dric.proto.CameraFrameProto.camera_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='dric.proto.CameraFrameProto.image', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='dric.proto.CameraFrameProto.ts', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=675,
  serialized_end=739,
)


_OBJECTBBOXTRACKPROTO = _descriptor.Descriptor(
  name='ObjectBBoxTrackProto',
  full_name='dric.proto.ObjectBBoxTrackProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='camera_id', full_name='dric.proto.ObjectBBoxTrackProto.camera_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='luid', full_name='dric.proto.ObjectBBoxTrackProto.luid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_class', full_name='dric.proto.ObjectBBoxTrackProto.object_class', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bbox', full_name='dric.proto.ObjectBBoxTrackProto.bbox', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading', full_name='dric.proto.ObjectBBoxTrackProto.heading', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='dric.proto.ObjectBBoxTrackProto.ts', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=742,
  serialized_end=892,
)


_OBJECTTRACKPROTO = _descriptor.Descriptor(
  name='ObjectTrackProto',
  full_name='dric.proto.ObjectTrackProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='camera_id', full_name='dric.proto.ObjectTrackProto.camera_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='luid', full_name='dric.proto.ObjectTrackProto.luid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_class', full_name='dric.proto.ObjectTrackProto.object_class', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coordinate', full_name='dric.proto.ObjectTrackProto.coordinate', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='azimuth', full_name='dric.proto.ObjectTrackProto.azimuth', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='dric.proto.ObjectTrackProto.ts', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=895,
  serialized_end=1046,
)


_ROTATIONPROTO = _descriptor.Descriptor(
  name='RotationProto',
  full_name='dric.proto.RotationProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='yaw', full_name='dric.proto.RotationProto.yaw', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='dric.proto.RotationProto.pitch', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roll', full_name='dric.proto.RotationProto.roll', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1048,
  serialized_end=1105,
)


_CAMERAFRAMEREQUEST = _descriptor.Descriptor(
  name='CameraFrameRequest',
  full_name='dric.proto.CameraFrameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='camera_id', full_name='dric.proto.CameraFrameRequest.camera_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='dric.proto.CameraFrameRequest.ts', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1107,
  serialized_end=1158,
)


_CAMERAFRAMERESPONSE = _descriptor.Descriptor(
  name='CameraFrameResponse',
  full_name='dric.proto.CameraFrameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame', full_name='dric.proto.CameraFrameResponse.frame', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dric.proto.CameraFrameResponse.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='either', full_name='dric.proto.CameraFrameResponse.either',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1160,
  serialized_end=1281,
)


_CAMERAFRAMERANGEREQUEST = _descriptor.Descriptor(
  name='CameraFrameRangeRequest',
  full_name='dric.proto.CameraFrameRangeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='camera_id', full_name='dric.proto.CameraFrameRangeRequest.camera_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_ts', full_name='dric.proto.CameraFrameRangeRequest.start_ts', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_ts', full_name='dric.proto.CameraFrameRangeRequest.stop_ts', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1283,
  serialized_end=1362,
)

_ENDPOINTRESPONSE.fields_by_name['end_point'].message_type = _ENDPOINT
_ENDPOINTRESPONSE.fields_by_name['error'].message_type = marmot__type__pb2._ERRORPROTO
_ENDPOINTRESPONSE.oneofs_by_name['either'].fields.append(
  _ENDPOINTRESPONSE.fields_by_name['end_point'])
_ENDPOINTRESPONSE.fields_by_name['end_point'].containing_oneof = _ENDPOINTRESPONSE.oneofs_by_name['either']
_ENDPOINTRESPONSE.oneofs_by_name['either'].fields.append(
  _ENDPOINTRESPONSE.fields_by_name['error'])
_ENDPOINTRESPONSE.fields_by_name['error'].containing_oneof = _ENDPOINTRESPONSE.oneofs_by_name['either']
_CAMERAINFORESPONSE.fields_by_name['camera_info'].message_type = _CAMERAINFO
_CAMERAINFORESPONSE.fields_by_name['error'].message_type = marmot__type__pb2._ERRORPROTO
_CAMERAINFORESPONSE.oneofs_by_name['either'].fields.append(
  _CAMERAINFORESPONSE.fields_by_name['camera_info'])
_CAMERAINFORESPONSE.fields_by_name['camera_info'].containing_oneof = _CAMERAINFORESPONSE.oneofs_by_name['either']
_CAMERAINFORESPONSE.oneofs_by_name['either'].fields.append(
  _CAMERAINFORESPONSE.fields_by_name['error'])
_CAMERAINFORESPONSE.fields_by_name['error'].containing_oneof = _CAMERAINFORESPONSE.oneofs_by_name['either']
_BOUNDINGBOXPROTO.fields_by_name['tl'].message_type = _IMAGECOORDINATEPROTO
_BOUNDINGBOXPROTO.fields_by_name['br'].message_type = _IMAGECOORDINATEPROTO
_OBJECTBBOXTRACKPROTO.fields_by_name['bbox'].message_type = _BOUNDINGBOXPROTO
_OBJECTTRACKPROTO.fields_by_name['coordinate'].message_type = _COORDINATEPROTO
_CAMERAFRAMERESPONSE.fields_by_name['frame'].message_type = _CAMERAFRAMEPROTO
_CAMERAFRAMERESPONSE.fields_by_name['error'].message_type = marmot__type__pb2._ERRORPROTO
_CAMERAFRAMERESPONSE.oneofs_by_name['either'].fields.append(
  _CAMERAFRAMERESPONSE.fields_by_name['frame'])
_CAMERAFRAMERESPONSE.fields_by_name['frame'].containing_oneof = _CAMERAFRAMERESPONSE.oneofs_by_name['either']
_CAMERAFRAMERESPONSE.oneofs_by_name['either'].fields.append(
  _CAMERAFRAMERESPONSE.fields_by_name['error'])
_CAMERAFRAMERESPONSE.fields_by_name['error'].containing_oneof = _CAMERAFRAMERESPONSE.oneofs_by_name['either']
DESCRIPTOR.message_types_by_name['EndPoint'] = _ENDPOINT
DESCRIPTOR.message_types_by_name['EndPointResponse'] = _ENDPOINTRESPONSE
DESCRIPTOR.message_types_by_name['JdbcEndPoint'] = _JDBCENDPOINT
DESCRIPTOR.message_types_by_name['CameraInfo'] = _CAMERAINFO
DESCRIPTOR.message_types_by_name['CameraInfoResponse'] = _CAMERAINFORESPONSE
DESCRIPTOR.message_types_by_name['ImageCoordinateProto'] = _IMAGECOORDINATEPROTO
DESCRIPTOR.message_types_by_name['CoordinateProto'] = _COORDINATEPROTO
DESCRIPTOR.message_types_by_name['BoundingBoxProto'] = _BOUNDINGBOXPROTO
DESCRIPTOR.message_types_by_name['CameraFrameProto'] = _CAMERAFRAMEPROTO
DESCRIPTOR.message_types_by_name['ObjectBBoxTrackProto'] = _OBJECTBBOXTRACKPROTO
DESCRIPTOR.message_types_by_name['ObjectTrackProto'] = _OBJECTTRACKPROTO
DESCRIPTOR.message_types_by_name['RotationProto'] = _ROTATIONPROTO
DESCRIPTOR.message_types_by_name['CameraFrameRequest'] = _CAMERAFRAMEREQUEST
DESCRIPTOR.message_types_by_name['CameraFrameResponse'] = _CAMERAFRAMERESPONSE
DESCRIPTOR.message_types_by_name['CameraFrameRangeRequest'] = _CAMERAFRAMERANGEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EndPoint = _reflection.GeneratedProtocolMessageType('EndPoint', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINT,
  '__module__' : 'dric_pb2'
  # @@protoc_insertion_point(class_scope:dric.proto.EndPoint)
  })
_sym_db.RegisterMessage(EndPoint)

EndPointResponse = _reflection.GeneratedProtocolMessageType('EndPointResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINTRESPONSE,
  '__module__' : 'dric_pb2'
  # @@protoc_insertion_point(class_scope:dric.proto.EndPointResponse)
  })
_sym_db.RegisterMessage(EndPointResponse)

JdbcEndPoint = _reflection.GeneratedProtocolMessageType('JdbcEndPoint', (_message.Message,), {
  'DESCRIPTOR' : _JDBCENDPOINT,
  '__module__' : 'dric_pb2'
  # @@protoc_insertion_point(class_scope:dric.proto.JdbcEndPoint)
  })
_sym_db.RegisterMessage(JdbcEndPoint)

CameraInfo = _reflection.GeneratedProtocolMessageType('CameraInfo', (_message.Message,), {
  'DESCRIPTOR' : _CAMERAINFO,
  '__module__' : 'dric_pb2'
  # @@protoc_insertion_point(class_scope:dric.proto.CameraInfo)
  })
_sym_db.RegisterMessage(CameraInfo)

CameraInfoResponse = _reflection.GeneratedProtocolMessageType('CameraInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _CAMERAINFORESPONSE,
  '__module__' : 'dric_pb2'
  # @@protoc_insertion_point(class_scope:dric.proto.CameraInfoResponse)
  })
_sym_db.RegisterMessage(CameraInfoResponse)

ImageCoordinateProto = _reflection.GeneratedProtocolMessageType('ImageCoordinateProto', (_message.Message,), {
  'DESCRIPTOR' : _IMAGECOORDINATEPROTO,
  '__module__' : 'dric_pb2'
  # @@protoc_insertion_point(class_scope:dric.proto.ImageCoordinateProto)
  })
_sym_db.RegisterMessage(ImageCoordinateProto)

CoordinateProto = _reflection.GeneratedProtocolMessageType('CoordinateProto', (_message.Message,), {
  'DESCRIPTOR' : _COORDINATEPROTO,
  '__module__' : 'dric_pb2'
  # @@protoc_insertion_point(class_scope:dric.proto.CoordinateProto)
  })
_sym_db.RegisterMessage(CoordinateProto)

BoundingBoxProto = _reflection.GeneratedProtocolMessageType('BoundingBoxProto', (_message.Message,), {
  'DESCRIPTOR' : _BOUNDINGBOXPROTO,
  '__module__' : 'dric_pb2'
  # @@protoc_insertion_point(class_scope:dric.proto.BoundingBoxProto)
  })
_sym_db.RegisterMessage(BoundingBoxProto)

CameraFrameProto = _reflection.GeneratedProtocolMessageType('CameraFrameProto', (_message.Message,), {
  'DESCRIPTOR' : _CAMERAFRAMEPROTO,
  '__module__' : 'dric_pb2'
  # @@protoc_insertion_point(class_scope:dric.proto.CameraFrameProto)
  })
_sym_db.RegisterMessage(CameraFrameProto)

ObjectBBoxTrackProto = _reflection.GeneratedProtocolMessageType('ObjectBBoxTrackProto', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTBBOXTRACKPROTO,
  '__module__' : 'dric_pb2'
  # @@protoc_insertion_point(class_scope:dric.proto.ObjectBBoxTrackProto)
  })
_sym_db.RegisterMessage(ObjectBBoxTrackProto)

ObjectTrackProto = _reflection.GeneratedProtocolMessageType('ObjectTrackProto', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTTRACKPROTO,
  '__module__' : 'dric_pb2'
  # @@protoc_insertion_point(class_scope:dric.proto.ObjectTrackProto)
  })
_sym_db.RegisterMessage(ObjectTrackProto)

RotationProto = _reflection.GeneratedProtocolMessageType('RotationProto', (_message.Message,), {
  'DESCRIPTOR' : _ROTATIONPROTO,
  '__module__' : 'dric_pb2'
  # @@protoc_insertion_point(class_scope:dric.proto.RotationProto)
  })
_sym_db.RegisterMessage(RotationProto)

CameraFrameRequest = _reflection.GeneratedProtocolMessageType('CameraFrameRequest', (_message.Message,), {
  'DESCRIPTOR' : _CAMERAFRAMEREQUEST,
  '__module__' : 'dric_pb2'
  # @@protoc_insertion_point(class_scope:dric.proto.CameraFrameRequest)
  })
_sym_db.RegisterMessage(CameraFrameRequest)

CameraFrameResponse = _reflection.GeneratedProtocolMessageType('CameraFrameResponse', (_message.Message,), {
  'DESCRIPTOR' : _CAMERAFRAMERESPONSE,
  '__module__' : 'dric_pb2'
  # @@protoc_insertion_point(class_scope:dric.proto.CameraFrameResponse)
  })
_sym_db.RegisterMessage(CameraFrameResponse)

CameraFrameRangeRequest = _reflection.GeneratedProtocolMessageType('CameraFrameRangeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CAMERAFRAMERANGEREQUEST,
  '__module__' : 'dric_pb2'
  # @@protoc_insertion_point(class_scope:dric.proto.CameraFrameRangeRequest)
  })
_sym_db.RegisterMessage(CameraFrameRangeRequest)


DESCRIPTOR._options = None

_DRICPLATFORM = _descriptor.ServiceDescriptor(
  name='DrICPlatform',
  full_name='dric.proto.DrICPlatform',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1364,
  serialized_end=1457,
  methods=[
  _descriptor.MethodDescriptor(
    name='getServiceEndPoint',
    full_name='dric.proto.DrICPlatform.getServiceEndPoint',
    index=0,
    containing_service=None,
    input_type=marmot__type__pb2._STRINGPROTO,
    output_type=_ENDPOINTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DRICPLATFORM)

DESCRIPTOR.services_by_name['DrICPlatform'] = _DRICPLATFORM


_DRICDATASTORE = _descriptor.ServiceDescriptor(
  name='DrICDataStore',
  full_name='dric.proto.DrICDataStore',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=1459,
  serialized_end=1474,
  methods=[
])
_sym_db.RegisterServiceDescriptor(_DRICDATASTORE)

DESCRIPTOR.services_by_name['DrICDataStore'] = _DRICDATASTORE


_DRICVIDEOSERVER = _descriptor.ServiceDescriptor(
  name='DrICVideoServer',
  full_name='dric.proto.DrICVideoServer',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=1477,
  serialized_end=1777,
  methods=[
  _descriptor.MethodDescriptor(
    name='addCamera',
    full_name='dric.proto.DrICVideoServer.addCamera',
    index=0,
    containing_service=None,
    input_type=_CAMERAINFO,
    output_type=marmot__type__pb2._VOIDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='removeCamera',
    full_name='dric.proto.DrICVideoServer.removeCamera',
    index=1,
    containing_service=None,
    input_type=marmot__type__pb2._STRINGPROTO,
    output_type=marmot__type__pb2._VOIDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getCamera',
    full_name='dric.proto.DrICVideoServer.getCamera',
    index=2,
    containing_service=None,
    input_type=marmot__type__pb2._STRINGPROTO,
    output_type=_CAMERAINFORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getCameraAll',
    full_name='dric.proto.DrICVideoServer.getCameraAll',
    index=3,
    containing_service=None,
    input_type=marmot__type__pb2._VOIDPROTO,
    output_type=_CAMERAINFORESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DRICVIDEOSERVER)

DESCRIPTOR.services_by_name['DrICVideoServer'] = _DRICVIDEOSERVER

# @@protoc_insertion_point(module_scope)
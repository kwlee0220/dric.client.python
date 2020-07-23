# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stream.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import base_pb2 as base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stream.proto',
  package='proto.stream',
  syntax='proto3',
  serialized_options=b'\n\014proto.streamP\001',
  serialized_pb=b'\n\x0cstream.proto\x12\x0cproto.stream\x1a\nbase.proto\"\xb2\x01\n\tUpMessage\x12\x10\n\x06header\x18\x01 \x01(\x0cH\x00\x12\x0f\n\x05\x62lock\x18\x02 \x01(\x0cH\x00\x12\"\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x11.proto.ErrorProtoH\x00\x12\x1f\n\x03\x65os\x18\x04 \x01(\x0b\x32\x10.proto.VoidProtoH\x00\x12!\n\x05\x64ummy\x18\x05 \x01(\x0b\x32\x10.proto.VoidProtoH\x00\x12\x10\n\x06offset\x18\x06 \x01(\x04H\x00\x42\x08\n\x06\x65ither\"\xb4\x01\n\x0b\x44ownMessage\x12\x10\n\x06result\x18\x01 \x01(\x0cH\x00\x12\x0f\n\x05\x62lock\x18\x02 \x01(\x0cH\x00\x12\"\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x11.proto.ErrorProtoH\x00\x12\x1f\n\x03\x65os\x18\x04 \x01(\x0b\x32\x10.proto.VoidProtoH\x00\x12!\n\x05\x64ummy\x18\x05 \x01(\x0b\x32\x10.proto.VoidProtoH\x00\x12\x10\n\x06offset\x18\x06 \x01(\x04H\x00\x42\x08\n\x06\x65ither\"z\n\x15MultiChannelUpMessage\x12\x12\n\nchannel_id\x18\x01 \x01(\x05\x12\'\n\x04type\x18\x02 \x01(\x0e\x32\x19.proto.stream.MessageType\x12$\n\x03msg\x18\x03 \x01(\x0b\x32\x17.proto.stream.UpMessage\"~\n\x17MultiChannelDownMessage\x12\x12\n\nchannel_id\x18\x01 \x01(\x05\x12\'\n\x04type\x18\x02 \x01(\x0e\x32\x19.proto.stream.MessageType\x12&\n\x03msg\x18\x03 \x01(\x0b\x32\x19.proto.stream.DownMessage\"6\n\x16UploadServerCancelTest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x05*2\n\x0bMessageType\x12\x08\n\x04\x44\x41TA\x10\x00\x12\x0e\n\nGRPC_ERROR\x10\x01\x12\t\n\x05\x43LOSE\x10\x02\x32\xc4\x02\n\rStreamService\x12\x42\n\x08\x64ownload\x12\x17.proto.stream.UpMessage\x1a\x19.proto.stream.DownMessage(\x01\x30\x01\x12>\n\x06upload\x12\x17.proto.stream.UpMessage\x1a\x19.proto.stream.DownMessage(\x01\x12_\n\rupAndDownload\x12#.proto.stream.MultiChannelUpMessage\x1a%.proto.stream.MultiChannelDownMessage(\x01\x30\x01\x12N\n\x14upload_server_cancel\x12\x17.proto.stream.UpMessage\x1a\x19.proto.stream.DownMessage(\x01\x30\x01\x42\x10\n\x0cproto.streamP\x01\x62\x06proto3'
  ,
  dependencies=[base__pb2.DESCRIPTOR,])

_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='proto.stream.MessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DATA', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRPC_ERROR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=714,
  serialized_end=764,
)
_sym_db.RegisterEnumDescriptor(_MESSAGETYPE)

MessageType = enum_type_wrapper.EnumTypeWrapper(_MESSAGETYPE)
DATA = 0
GRPC_ERROR = 1
CLOSE = 2



_UPMESSAGE = _descriptor.Descriptor(
  name='UpMessage',
  full_name='proto.stream.UpMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.stream.UpMessage.header', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block', full_name='proto.stream.UpMessage.block', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='proto.stream.UpMessage.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eos', full_name='proto.stream.UpMessage.eos', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dummy', full_name='proto.stream.UpMessage.dummy', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='proto.stream.UpMessage.offset', index=5,
      number=6, type=4, cpp_type=4, label=1,
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
    _descriptor.OneofDescriptor(
      name='either', full_name='proto.stream.UpMessage.either',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=43,
  serialized_end=221,
)


_DOWNMESSAGE = _descriptor.Descriptor(
  name='DownMessage',
  full_name='proto.stream.DownMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='proto.stream.DownMessage.result', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block', full_name='proto.stream.DownMessage.block', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='proto.stream.DownMessage.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eos', full_name='proto.stream.DownMessage.eos', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dummy', full_name='proto.stream.DownMessage.dummy', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='proto.stream.DownMessage.offset', index=5,
      number=6, type=4, cpp_type=4, label=1,
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
    _descriptor.OneofDescriptor(
      name='either', full_name='proto.stream.DownMessage.either',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=224,
  serialized_end=404,
)


_MULTICHANNELUPMESSAGE = _descriptor.Descriptor(
  name='MultiChannelUpMessage',
  full_name='proto.stream.MultiChannelUpMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='proto.stream.MultiChannelUpMessage.channel_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='proto.stream.MultiChannelUpMessage.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='proto.stream.MultiChannelUpMessage.msg', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=406,
  serialized_end=528,
)


_MULTICHANNELDOWNMESSAGE = _descriptor.Descriptor(
  name='MultiChannelDownMessage',
  full_name='proto.stream.MultiChannelDownMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='proto.stream.MultiChannelDownMessage.channel_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='proto.stream.MultiChannelDownMessage.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='proto.stream.MultiChannelDownMessage.msg', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=530,
  serialized_end=656,
)


_UPLOADSERVERCANCELTEST = _descriptor.Descriptor(
  name='UploadServerCancelTest',
  full_name='proto.stream.UploadServerCancelTest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='proto.stream.UploadServerCancelTest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='proto.stream.UploadServerCancelTest.offset', index=1,
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
  serialized_start=658,
  serialized_end=712,
)

_UPMESSAGE.fields_by_name['error'].message_type = base__pb2._ERRORPROTO
_UPMESSAGE.fields_by_name['eos'].message_type = base__pb2._VOIDPROTO
_UPMESSAGE.fields_by_name['dummy'].message_type = base__pb2._VOIDPROTO
_UPMESSAGE.oneofs_by_name['either'].fields.append(
  _UPMESSAGE.fields_by_name['header'])
_UPMESSAGE.fields_by_name['header'].containing_oneof = _UPMESSAGE.oneofs_by_name['either']
_UPMESSAGE.oneofs_by_name['either'].fields.append(
  _UPMESSAGE.fields_by_name['block'])
_UPMESSAGE.fields_by_name['block'].containing_oneof = _UPMESSAGE.oneofs_by_name['either']
_UPMESSAGE.oneofs_by_name['either'].fields.append(
  _UPMESSAGE.fields_by_name['error'])
_UPMESSAGE.fields_by_name['error'].containing_oneof = _UPMESSAGE.oneofs_by_name['either']
_UPMESSAGE.oneofs_by_name['either'].fields.append(
  _UPMESSAGE.fields_by_name['eos'])
_UPMESSAGE.fields_by_name['eos'].containing_oneof = _UPMESSAGE.oneofs_by_name['either']
_UPMESSAGE.oneofs_by_name['either'].fields.append(
  _UPMESSAGE.fields_by_name['dummy'])
_UPMESSAGE.fields_by_name['dummy'].containing_oneof = _UPMESSAGE.oneofs_by_name['either']
_UPMESSAGE.oneofs_by_name['either'].fields.append(
  _UPMESSAGE.fields_by_name['offset'])
_UPMESSAGE.fields_by_name['offset'].containing_oneof = _UPMESSAGE.oneofs_by_name['either']
_DOWNMESSAGE.fields_by_name['error'].message_type = base__pb2._ERRORPROTO
_DOWNMESSAGE.fields_by_name['eos'].message_type = base__pb2._VOIDPROTO
_DOWNMESSAGE.fields_by_name['dummy'].message_type = base__pb2._VOIDPROTO
_DOWNMESSAGE.oneofs_by_name['either'].fields.append(
  _DOWNMESSAGE.fields_by_name['result'])
_DOWNMESSAGE.fields_by_name['result'].containing_oneof = _DOWNMESSAGE.oneofs_by_name['either']
_DOWNMESSAGE.oneofs_by_name['either'].fields.append(
  _DOWNMESSAGE.fields_by_name['block'])
_DOWNMESSAGE.fields_by_name['block'].containing_oneof = _DOWNMESSAGE.oneofs_by_name['either']
_DOWNMESSAGE.oneofs_by_name['either'].fields.append(
  _DOWNMESSAGE.fields_by_name['error'])
_DOWNMESSAGE.fields_by_name['error'].containing_oneof = _DOWNMESSAGE.oneofs_by_name['either']
_DOWNMESSAGE.oneofs_by_name['either'].fields.append(
  _DOWNMESSAGE.fields_by_name['eos'])
_DOWNMESSAGE.fields_by_name['eos'].containing_oneof = _DOWNMESSAGE.oneofs_by_name['either']
_DOWNMESSAGE.oneofs_by_name['either'].fields.append(
  _DOWNMESSAGE.fields_by_name['dummy'])
_DOWNMESSAGE.fields_by_name['dummy'].containing_oneof = _DOWNMESSAGE.oneofs_by_name['either']
_DOWNMESSAGE.oneofs_by_name['either'].fields.append(
  _DOWNMESSAGE.fields_by_name['offset'])
_DOWNMESSAGE.fields_by_name['offset'].containing_oneof = _DOWNMESSAGE.oneofs_by_name['either']
_MULTICHANNELUPMESSAGE.fields_by_name['type'].enum_type = _MESSAGETYPE
_MULTICHANNELUPMESSAGE.fields_by_name['msg'].message_type = _UPMESSAGE
_MULTICHANNELDOWNMESSAGE.fields_by_name['type'].enum_type = _MESSAGETYPE
_MULTICHANNELDOWNMESSAGE.fields_by_name['msg'].message_type = _DOWNMESSAGE
DESCRIPTOR.message_types_by_name['UpMessage'] = _UPMESSAGE
DESCRIPTOR.message_types_by_name['DownMessage'] = _DOWNMESSAGE
DESCRIPTOR.message_types_by_name['MultiChannelUpMessage'] = _MULTICHANNELUPMESSAGE
DESCRIPTOR.message_types_by_name['MultiChannelDownMessage'] = _MULTICHANNELDOWNMESSAGE
DESCRIPTOR.message_types_by_name['UploadServerCancelTest'] = _UPLOADSERVERCANCELTEST
DESCRIPTOR.enum_types_by_name['MessageType'] = _MESSAGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpMessage = _reflection.GeneratedProtocolMessageType('UpMessage', (_message.Message,), {
  'DESCRIPTOR' : _UPMESSAGE,
  '__module__' : 'stream_pb2'
  # @@protoc_insertion_point(class_scope:proto.stream.UpMessage)
  })
_sym_db.RegisterMessage(UpMessage)

DownMessage = _reflection.GeneratedProtocolMessageType('DownMessage', (_message.Message,), {
  'DESCRIPTOR' : _DOWNMESSAGE,
  '__module__' : 'stream_pb2'
  # @@protoc_insertion_point(class_scope:proto.stream.DownMessage)
  })
_sym_db.RegisterMessage(DownMessage)

MultiChannelUpMessage = _reflection.GeneratedProtocolMessageType('MultiChannelUpMessage', (_message.Message,), {
  'DESCRIPTOR' : _MULTICHANNELUPMESSAGE,
  '__module__' : 'stream_pb2'
  # @@protoc_insertion_point(class_scope:proto.stream.MultiChannelUpMessage)
  })
_sym_db.RegisterMessage(MultiChannelUpMessage)

MultiChannelDownMessage = _reflection.GeneratedProtocolMessageType('MultiChannelDownMessage', (_message.Message,), {
  'DESCRIPTOR' : _MULTICHANNELDOWNMESSAGE,
  '__module__' : 'stream_pb2'
  # @@protoc_insertion_point(class_scope:proto.stream.MultiChannelDownMessage)
  })
_sym_db.RegisterMessage(MultiChannelDownMessage)

UploadServerCancelTest = _reflection.GeneratedProtocolMessageType('UploadServerCancelTest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADSERVERCANCELTEST,
  '__module__' : 'stream_pb2'
  # @@protoc_insertion_point(class_scope:proto.stream.UploadServerCancelTest)
  })
_sym_db.RegisterMessage(UploadServerCancelTest)


DESCRIPTOR._options = None

_STREAMSERVICE = _descriptor.ServiceDescriptor(
  name='StreamService',
  full_name='proto.stream.StreamService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=767,
  serialized_end=1091,
  methods=[
  _descriptor.MethodDescriptor(
    name='download',
    full_name='proto.stream.StreamService.download',
    index=0,
    containing_service=None,
    input_type=_UPMESSAGE,
    output_type=_DOWNMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='upload',
    full_name='proto.stream.StreamService.upload',
    index=1,
    containing_service=None,
    input_type=_UPMESSAGE,
    output_type=_DOWNMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='upAndDownload',
    full_name='proto.stream.StreamService.upAndDownload',
    index=2,
    containing_service=None,
    input_type=_MULTICHANNELUPMESSAGE,
    output_type=_MULTICHANNELDOWNMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='upload_server_cancel',
    full_name='proto.stream.StreamService.upload_server_cancel',
    index=3,
    containing_service=None,
    input_type=_UPMESSAGE,
    output_type=_DOWNMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMSERVICE)

DESCRIPTOR.services_by_name['StreamService'] = _STREAMSERVICE

# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ngrpc.proto\"\x06\n\x04Null\"\x1e\n\tTimestamp\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x32\x33\n\x0bGRPCService\x12$\n\rGetServerTime\x12\x05.Null\x1a\n.Timestamp\"\x00\x62\x06proto3')
)




_NULL = _descriptor.Descriptor(
  name='Null',
  full_name='Null',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=14,
  serialized_end=20,
)


_TIMESTAMP = _descriptor.Descriptor(
  name='Timestamp',
  full_name='Timestamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Timestamp.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
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
  serialized_start=22,
  serialized_end=52,
)

DESCRIPTOR.message_types_by_name['Null'] = _NULL
DESCRIPTOR.message_types_by_name['Timestamp'] = _TIMESTAMP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Null = _reflection.GeneratedProtocolMessageType('Null', (_message.Message,), {
  'DESCRIPTOR' : _NULL,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:Null)
  })
_sym_db.RegisterMessage(Null)

Timestamp = _reflection.GeneratedProtocolMessageType('Timestamp', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMP,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:Timestamp)
  })
_sym_db.RegisterMessage(Timestamp)



_GRPCSERVICE = _descriptor.ServiceDescriptor(
  name='GRPCService',
  full_name='GRPCService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=54,
  serialized_end=105,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetServerTime',
    full_name='GRPCService.GetServerTime',
    index=0,
    containing_service=None,
    input_type=_NULL,
    output_type=_TIMESTAMP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRPCSERVICE)

DESCRIPTOR.services_by_name['GRPCService'] = _GRPCSERVICE

# @@protoc_insertion_point(module_scope)

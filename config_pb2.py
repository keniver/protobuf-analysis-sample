# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x0c\x63onfig.proto\"W\n\x0eNetworkSetting\x12\n\n\x02ip\x18\x01 \x02(\t\x12\x0c\n\x04mask\x18\x02 \x02(\t\x12\x0f\n\x07gateway\x18\x03 \x02(\t\x12\x0c\n\x04\x64ns1\x18\x04 \x02(\t\x12\x0c\n\x04\x64ns2\x18\x05 \x01(\t\"<\n\x07\x41\x63\x63ount\x12\x10\n\x08username\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\x12\r\n\x05level\x18\x03 \x02(\x05\"\x9f\x01\n\x06\x43onfig\x12\x16\n\x0e\x63onfig_version\x18\x01 \x02(\t\x12\x18\n\x10\x66irmware_version\x18\x02 \x02(\t\x12\x1d\n\x15\x64\x65vice_identification\x18\x03 \x02(\t\x12(\n\x0fnetwork_setting\x18\x04 \x02(\x0b\x32\x0f.NetworkSetting\x12\x1a\n\x08\x61\x63\x63ounts\x18\x05 \x03(\x0b\x32\x08.Account'
)




_NETWORKSETTING = _descriptor.Descriptor(
  name='NetworkSetting',
  full_name='NetworkSetting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='NetworkSetting.ip', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mask', full_name='NetworkSetting.mask', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gateway', full_name='NetworkSetting.gateway', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dns1', full_name='NetworkSetting.dns1', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dns2', full_name='NetworkSetting.dns2', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=103,
)


_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='Account.username', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='Account.password', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='Account.level', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=165,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config_version', full_name='Config.config_version', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='firmware_version', full_name='Config.firmware_version', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_identification', full_name='Config.device_identification', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_setting', full_name='Config.network_setting', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accounts', full_name='Config.accounts', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=327,
)

_CONFIG.fields_by_name['network_setting'].message_type = _NETWORKSETTING
_CONFIG.fields_by_name['accounts'].message_type = _ACCOUNT
DESCRIPTOR.message_types_by_name['NetworkSetting'] = _NETWORKSETTING
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NetworkSetting = _reflection.GeneratedProtocolMessageType('NetworkSetting', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKSETTING,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:NetworkSetting)
  })
_sym_db.RegisterMessage(NetworkSetting)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:Account)
  })
_sym_db.RegisterMessage(Account)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:Config)
  })
_sym_db.RegisterMessage(Config)


# @@protoc_insertion_point(module_scope)
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TestLabConfigMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TestLabConfigMessage.proto',
  package='android.test.lab',
  serialized_pb='\n\x1aTestLabConfigMessage.proto\x12\x10\x61ndroid.test.lab\"b\n\x10LabConfigMessage\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\r\n\x05owner\x18\x02 \x01(\x0c\x12\x31\n\x04host\x18\x0b \x03(\x0b\x32#.android.test.lab.HostConfigMessage\"\x8e\x01\n\x11HostConfigMessage\x12\x10\n\x08hostname\x18\x01 \x01(\x0c\x12\n\n\x02ip\x18\x02 \x01(\x0c\x12\x0e\n\x06script\x18\x03 \x01(\x0c\x12\x14\n\x0csetup_script\x18\x04 \x01(\x0c\x12\x35\n\x06\x64\x65vice\x18\x0b \x03(\x0b\x32%.android.test.lab.DeviceConfigMessage\"E\n\x13\x44\x65viceConfigMessage\x12\x0e\n\x06serial\x18\x01 \x01(\x0c\x12\r\n\x05index\x18\x02 \x01(\x05\x12\x0f\n\x07product\x18\x0b \x01(\x0c')




_LABCONFIGMESSAGE = _descriptor.Descriptor(
  name='LabConfigMessage',
  full_name='android.test.lab.LabConfigMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='android.test.lab.LabConfigMessage.name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='owner', full_name='android.test.lab.LabConfigMessage.owner', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='android.test.lab.LabConfigMessage.host', index=2,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=48,
  serialized_end=146,
)


_HOSTCONFIGMESSAGE = _descriptor.Descriptor(
  name='HostConfigMessage',
  full_name='android.test.lab.HostConfigMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostname', full_name='android.test.lab.HostConfigMessage.hostname', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip', full_name='android.test.lab.HostConfigMessage.ip', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='script', full_name='android.test.lab.HostConfigMessage.script', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='setup_script', full_name='android.test.lab.HostConfigMessage.setup_script', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device', full_name='android.test.lab.HostConfigMessage.device', index=4,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=149,
  serialized_end=291,
)


_DEVICECONFIGMESSAGE = _descriptor.Descriptor(
  name='DeviceConfigMessage',
  full_name='android.test.lab.DeviceConfigMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serial', full_name='android.test.lab.DeviceConfigMessage.serial', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='android.test.lab.DeviceConfigMessage.index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='product', full_name='android.test.lab.DeviceConfigMessage.product', index=2,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=293,
  serialized_end=362,
)

_LABCONFIGMESSAGE.fields_by_name['host'].message_type = _HOSTCONFIGMESSAGE
_HOSTCONFIGMESSAGE.fields_by_name['device'].message_type = _DEVICECONFIGMESSAGE
DESCRIPTOR.message_types_by_name['LabConfigMessage'] = _LABCONFIGMESSAGE
DESCRIPTOR.message_types_by_name['HostConfigMessage'] = _HOSTCONFIGMESSAGE
DESCRIPTOR.message_types_by_name['DeviceConfigMessage'] = _DEVICECONFIGMESSAGE

class LabConfigMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LABCONFIGMESSAGE

  # @@protoc_insertion_point(class_scope:android.test.lab.LabConfigMessage)

class HostConfigMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HOSTCONFIGMESSAGE

  # @@protoc_insertion_point(class_scope:android.test.lab.HostConfigMessage)

class DeviceConfigMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DEVICECONFIGMESSAGE

  # @@protoc_insertion_point(class_scope:android.test.lab.DeviceConfigMessage)


# @@protoc_insertion_point(module_scope)

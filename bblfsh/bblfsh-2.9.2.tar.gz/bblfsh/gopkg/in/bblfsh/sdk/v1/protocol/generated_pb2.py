# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generated.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.gogo.protobuf.gogoproto import gogo_pb2 as github_dot_com_dot_gogo_dot_protobuf_dot_gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
import importlib
gopkg_dot_in_dot_bblfsh_dot_sdk_dot_v1_dot_uast_dot_generated__pb2 = importlib.import_module('gopkg.in.bblfsh.sdk.v1.uast.generated_pb2')
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='generated.proto',
  package='gopkg.in.bblfsh.sdk.v1.protocol',
  syntax='proto3',
  serialized_pb=_b('\n\x0fgenerated.proto\x12\x1fgopkg.in.bblfsh.sdk.v1.protocol\x1a-github.com/gogo/protobuf/gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a+gopkg.in/bblfsh/sdk.v1/uast/generated.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc6\x01\n\x12NativeParseRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12;\n\x08\x65ncoding\x18\x04 \x01(\x0e\x32).gopkg.in.bblfsh.sdk.v1.protocol.Encoding\x12\x34\n\x07timeout\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01:\x08\x88\xa0\x1f\x00\xf0\xa1\x1f\x00\"\xca\x01\n\x13NativeParseResponse\x12\x37\n\x06status\x18\x01 \x01(\x0e\x32\'.gopkg.in.bblfsh.sdk.v1.protocol.Status\x12\x0e\n\x06\x65rrors\x18\x02 \x03(\t\x12\x34\n\x07\x65lapsed\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x14\n\x03\x61st\x18\x04 \x01(\tB\x07\xe2\xde\x1f\x03\x41ST\x12\x10\n\x08language\x18\x05 \x01(\t:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xf0\xa1\x1f\x00\"\xc0\x01\n\x0cParseRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12;\n\x08\x65ncoding\x18\x04 \x01(\x0e\x32).gopkg.in.bblfsh.sdk.v1.protocol.Encoding\x12\x34\n\x07timeout\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01:\x08\x88\xa0\x1f\x00\xf0\xa1\x1f\x00\"\xe9\x01\n\rParseResponse\x12\x37\n\x06status\x18\x01 \x01(\x0e\x32\'.gopkg.in.bblfsh.sdk.v1.protocol.Status\x12\x0e\n\x06\x65rrors\x18\x02 \x03(\t\x12\x34\n\x07\x65lapsed\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x39\n\x04uast\x18\x04 \x01(\x0b\x32!.gopkg.in.bblfsh.sdk.v1.uast.NodeB\x08\xe2\xde\x1f\x04UAST\x12\x10\n\x08language\x18\x05 \x01(\t:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xf0\xa1\x1f\x00\"\x1a\n\x0eVersionRequest:\x08\x88\xa0\x1f\x00\xf0\xa1\x1f\x00\"\xe0\x01\n\x0fVersionResponse\x12\x37\n\x06status\x18\x01 \x01(\x0e\x32\'.gopkg.in.bblfsh.sdk.v1.protocol.Status\x12\x0e\n\x06\x65rrors\x18\x02 \x03(\t\x12\x34\n\x07\x65lapsed\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x33\n\x05\x62uild\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01:\x08\x88\xa0\x1f\x00\xf0\xa1\x1f\x00*D\n\x08\x45ncoding\x12\x12\n\x04UTF8\x10\x00\x1a\x08\x8a\x9d \x04UTF8\x12\x16\n\x06\x42\x41SE64\x10\x01\x1a\n\x8a\x9d \x06\x42\x61se64\x1a\x0c\xc0\xa4\x1e\x00\x88\xa3\x1e\x00\xa8\xa4\x1e\x00*R\n\x06Status\x12\x0e\n\x02OK\x10\x00\x1a\x06\x8a\x9d \x02Ok\x12\x14\n\x05\x45RROR\x10\x01\x1a\t\x8a\x9d \x05\x45rror\x12\x14\n\x05\x46\x41TAL\x10\x02\x1a\t\x8a\x9d \x05\x46\x61tal\x1a\x0c\xc0\xa4\x1e\x00\x88\xa3\x1e\x00\xa8\xa4\x1e\x00\x32\xe1\x02\n\x0fProtocolService\x12x\n\x0bNativeParse\x12\x33.gopkg.in.bblfsh.sdk.v1.protocol.NativeParseRequest\x1a\x34.gopkg.in.bblfsh.sdk.v1.protocol.NativeParseResponse\x12\x66\n\x05Parse\x12-.gopkg.in.bblfsh.sdk.v1.protocol.ParseRequest\x1a..gopkg.in.bblfsh.sdk.v1.protocol.ParseResponse\x12l\n\x07Version\x12/.gopkg.in.bblfsh.sdk.v1.protocol.VersionRequest\x1a\x30.gopkg.in.bblfsh.sdk.v1.protocol.VersionResponseB\x12Z\x08protocol\xa0\xe3\x1e\x01\xe0\xe2\x1e\x00\x62\x06proto3')
  ,
  dependencies=[github_dot_com_dot_gogo_dot_protobuf_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,gopkg_dot_in_dot_bblfsh_dot_sdk_dot_v1_dot_uast_dot_generated__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_ENCODING = _descriptor.EnumDescriptor(
  name='Encoding',
  full_name='gopkg.in.bblfsh.sdk.v1.protocol.Encoding',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UTF8', index=0, number=0,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \004UTF8')),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BASE64', index=1, number=1,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \006Base64')),
      type=None),
  ],
  containing_type=None,
  options=_descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\300\244\036\000\210\243\036\000\250\244\036\000')),
  serialized_start=1301,
  serialized_end=1369,
)
_sym_db.RegisterEnumDescriptor(_ENCODING)

Encoding = enum_type_wrapper.EnumTypeWrapper(_ENCODING)
_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='gopkg.in.bblfsh.sdk.v1.protocol.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \002Ok')),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \005Error')),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FATAL', index=2, number=2,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \005Fatal')),
      type=None),
  ],
  containing_type=None,
  options=_descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\300\244\036\000\210\243\036\000\250\244\036\000')),
  serialized_start=1371,
  serialized_end=1453,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
UTF8 = 0
BASE64 = 1
OK = 0
ERROR = 1
FATAL = 2



_NATIVEPARSEREQUEST = _descriptor.Descriptor(
  name='NativeParseRequest',
  full_name='gopkg.in.bblfsh.sdk.v1.protocol.NativeParseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='gopkg.in.bblfsh.sdk.v1.protocol.NativeParseRequest.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='gopkg.in.bblfsh.sdk.v1.protocol.NativeParseRequest.language', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='gopkg.in.bblfsh.sdk.v1.protocol.NativeParseRequest.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoding', full_name='gopkg.in.bblfsh.sdk.v1.protocol.NativeParseRequest.encoding', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='gopkg.in.bblfsh.sdk.v1.protocol.NativeParseRequest.timeout', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\360\241\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=408,
)


_NATIVEPARSERESPONSE = _descriptor.Descriptor(
  name='NativeParseResponse',
  full_name='gopkg.in.bblfsh.sdk.v1.protocol.NativeParseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='gopkg.in.bblfsh.sdk.v1.protocol.NativeParseResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errors', full_name='gopkg.in.bblfsh.sdk.v1.protocol.NativeParseResponse.errors', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elapsed', full_name='gopkg.in.bblfsh.sdk.v1.protocol.NativeParseResponse.elapsed', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ast', full_name='gopkg.in.bblfsh.sdk.v1.protocol.NativeParseResponse.ast', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\003AST')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='gopkg.in.bblfsh.sdk.v1.protocol.NativeParseResponse.language', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\230\240\037\000\360\241\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=613,
)


_PARSEREQUEST = _descriptor.Descriptor(
  name='ParseRequest',
  full_name='gopkg.in.bblfsh.sdk.v1.protocol.ParseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='gopkg.in.bblfsh.sdk.v1.protocol.ParseRequest.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='gopkg.in.bblfsh.sdk.v1.protocol.ParseRequest.language', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='gopkg.in.bblfsh.sdk.v1.protocol.ParseRequest.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoding', full_name='gopkg.in.bblfsh.sdk.v1.protocol.ParseRequest.encoding', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='gopkg.in.bblfsh.sdk.v1.protocol.ParseRequest.timeout', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\360\241\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=616,
  serialized_end=808,
)


_PARSERESPONSE = _descriptor.Descriptor(
  name='ParseResponse',
  full_name='gopkg.in.bblfsh.sdk.v1.protocol.ParseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='gopkg.in.bblfsh.sdk.v1.protocol.ParseResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errors', full_name='gopkg.in.bblfsh.sdk.v1.protocol.ParseResponse.errors', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elapsed', full_name='gopkg.in.bblfsh.sdk.v1.protocol.ParseResponse.elapsed', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uast', full_name='gopkg.in.bblfsh.sdk.v1.protocol.ParseResponse.uast', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\004UAST')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='gopkg.in.bblfsh.sdk.v1.protocol.ParseResponse.language', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\230\240\037\000\360\241\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=811,
  serialized_end=1044,
)


_VERSIONREQUEST = _descriptor.Descriptor(
  name='VersionRequest',
  full_name='gopkg.in.bblfsh.sdk.v1.protocol.VersionRequest',
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\360\241\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1046,
  serialized_end=1072,
)


_VERSIONRESPONSE = _descriptor.Descriptor(
  name='VersionResponse',
  full_name='gopkg.in.bblfsh.sdk.v1.protocol.VersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='gopkg.in.bblfsh.sdk.v1.protocol.VersionResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errors', full_name='gopkg.in.bblfsh.sdk.v1.protocol.VersionResponse.errors', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elapsed', full_name='gopkg.in.bblfsh.sdk.v1.protocol.VersionResponse.elapsed', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='gopkg.in.bblfsh.sdk.v1.protocol.VersionResponse.version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build', full_name='gopkg.in.bblfsh.sdk.v1.protocol.VersionResponse.build', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\220\337\037\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\360\241\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1075,
  serialized_end=1299,
)

_NATIVEPARSEREQUEST.fields_by_name['encoding'].enum_type = _ENCODING
_NATIVEPARSEREQUEST.fields_by_name['timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_NATIVEPARSERESPONSE.fields_by_name['status'].enum_type = _STATUS
_NATIVEPARSERESPONSE.fields_by_name['elapsed'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_PARSEREQUEST.fields_by_name['encoding'].enum_type = _ENCODING
_PARSEREQUEST.fields_by_name['timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_PARSERESPONSE.fields_by_name['status'].enum_type = _STATUS
_PARSERESPONSE.fields_by_name['elapsed'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_PARSERESPONSE.fields_by_name['uast'].message_type = gopkg_dot_in_dot_bblfsh_dot_sdk_dot_v1_dot_uast_dot_generated__pb2._NODE
_VERSIONRESPONSE.fields_by_name['status'].enum_type = _STATUS
_VERSIONRESPONSE.fields_by_name['elapsed'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_VERSIONRESPONSE.fields_by_name['build'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['NativeParseRequest'] = _NATIVEPARSEREQUEST
DESCRIPTOR.message_types_by_name['NativeParseResponse'] = _NATIVEPARSERESPONSE
DESCRIPTOR.message_types_by_name['ParseRequest'] = _PARSEREQUEST
DESCRIPTOR.message_types_by_name['ParseResponse'] = _PARSERESPONSE
DESCRIPTOR.message_types_by_name['VersionRequest'] = _VERSIONREQUEST
DESCRIPTOR.message_types_by_name['VersionResponse'] = _VERSIONRESPONSE
DESCRIPTOR.enum_types_by_name['Encoding'] = _ENCODING
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NativeParseRequest = _reflection.GeneratedProtocolMessageType('NativeParseRequest', (_message.Message,), dict(
  DESCRIPTOR = _NATIVEPARSEREQUEST,
  __module__ = 'generated_pb2'
  # @@protoc_insertion_point(class_scope:gopkg.in.bblfsh.sdk.v1.protocol.NativeParseRequest)
  ))
_sym_db.RegisterMessage(NativeParseRequest)

NativeParseResponse = _reflection.GeneratedProtocolMessageType('NativeParseResponse', (_message.Message,), dict(
  DESCRIPTOR = _NATIVEPARSERESPONSE,
  __module__ = 'generated_pb2'
  # @@protoc_insertion_point(class_scope:gopkg.in.bblfsh.sdk.v1.protocol.NativeParseResponse)
  ))
_sym_db.RegisterMessage(NativeParseResponse)

ParseRequest = _reflection.GeneratedProtocolMessageType('ParseRequest', (_message.Message,), dict(
  DESCRIPTOR = _PARSEREQUEST,
  __module__ = 'generated_pb2'
  # @@protoc_insertion_point(class_scope:gopkg.in.bblfsh.sdk.v1.protocol.ParseRequest)
  ))
_sym_db.RegisterMessage(ParseRequest)

ParseResponse = _reflection.GeneratedProtocolMessageType('ParseResponse', (_message.Message,), dict(
  DESCRIPTOR = _PARSERESPONSE,
  __module__ = 'generated_pb2'
  # @@protoc_insertion_point(class_scope:gopkg.in.bblfsh.sdk.v1.protocol.ParseResponse)
  ))
_sym_db.RegisterMessage(ParseResponse)

VersionRequest = _reflection.GeneratedProtocolMessageType('VersionRequest', (_message.Message,), dict(
  DESCRIPTOR = _VERSIONREQUEST,
  __module__ = 'generated_pb2'
  # @@protoc_insertion_point(class_scope:gopkg.in.bblfsh.sdk.v1.protocol.VersionRequest)
  ))
_sym_db.RegisterMessage(VersionRequest)

VersionResponse = _reflection.GeneratedProtocolMessageType('VersionResponse', (_message.Message,), dict(
  DESCRIPTOR = _VERSIONRESPONSE,
  __module__ = 'generated_pb2'
  # @@protoc_insertion_point(class_scope:gopkg.in.bblfsh.sdk.v1.protocol.VersionResponse)
  ))
_sym_db.RegisterMessage(VersionResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\010protocol\240\343\036\001\340\342\036\000'))
_ENCODING.has_options = True
_ENCODING._options = _descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\300\244\036\000\210\243\036\000\250\244\036\000'))
_ENCODING.values_by_name["UTF8"].has_options = True
_ENCODING.values_by_name["UTF8"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \004UTF8'))
_ENCODING.values_by_name["BASE64"].has_options = True
_ENCODING.values_by_name["BASE64"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \006Base64'))
_STATUS.has_options = True
_STATUS._options = _descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\300\244\036\000\210\243\036\000\250\244\036\000'))
_STATUS.values_by_name["OK"].has_options = True
_STATUS.values_by_name["OK"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \002Ok'))
_STATUS.values_by_name["ERROR"].has_options = True
_STATUS.values_by_name["ERROR"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \005Error'))
_STATUS.values_by_name["FATAL"].has_options = True
_STATUS.values_by_name["FATAL"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \005Fatal'))
_NATIVEPARSEREQUEST.fields_by_name['timeout'].has_options = True
_NATIVEPARSEREQUEST.fields_by_name['timeout']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001'))
_NATIVEPARSEREQUEST.has_options = True
_NATIVEPARSEREQUEST._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\360\241\037\000'))
_NATIVEPARSERESPONSE.fields_by_name['elapsed'].has_options = True
_NATIVEPARSERESPONSE.fields_by_name['elapsed']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001'))
_NATIVEPARSERESPONSE.fields_by_name['ast'].has_options = True
_NATIVEPARSERESPONSE.fields_by_name['ast']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\003AST'))
_NATIVEPARSERESPONSE.has_options = True
_NATIVEPARSERESPONSE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\230\240\037\000\360\241\037\000'))
_PARSEREQUEST.fields_by_name['timeout'].has_options = True
_PARSEREQUEST.fields_by_name['timeout']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001'))
_PARSEREQUEST.has_options = True
_PARSEREQUEST._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\360\241\037\000'))
_PARSERESPONSE.fields_by_name['elapsed'].has_options = True
_PARSERESPONSE.fields_by_name['elapsed']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001'))
_PARSERESPONSE.fields_by_name['uast'].has_options = True
_PARSERESPONSE.fields_by_name['uast']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\004UAST'))
_PARSERESPONSE.has_options = True
_PARSERESPONSE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\230\240\037\000\360\241\037\000'))
_VERSIONREQUEST.has_options = True
_VERSIONREQUEST._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\360\241\037\000'))
_VERSIONRESPONSE.fields_by_name['elapsed'].has_options = True
_VERSIONRESPONSE.fields_by_name['elapsed']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001'))
_VERSIONRESPONSE.fields_by_name['build'].has_options = True
_VERSIONRESPONSE.fields_by_name['build']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\220\337\037\001'))
_VERSIONRESPONSE.has_options = True
_VERSIONRESPONSE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\240\037\000\360\241\037\000'))

_PROTOCOLSERVICE = _descriptor.ServiceDescriptor(
  name='ProtocolService',
  full_name='gopkg.in.bblfsh.sdk.v1.protocol.ProtocolService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1456,
  serialized_end=1809,
  methods=[
  _descriptor.MethodDescriptor(
    name='NativeParse',
    full_name='gopkg.in.bblfsh.sdk.v1.protocol.ProtocolService.NativeParse',
    index=0,
    containing_service=None,
    input_type=_NATIVEPARSEREQUEST,
    output_type=_NATIVEPARSERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Parse',
    full_name='gopkg.in.bblfsh.sdk.v1.protocol.ProtocolService.Parse',
    index=1,
    containing_service=None,
    input_type=_PARSEREQUEST,
    output_type=_PARSERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Version',
    full_name='gopkg.in.bblfsh.sdk.v1.protocol.ProtocolService.Version',
    index=2,
    containing_service=None,
    input_type=_VERSIONREQUEST,
    output_type=_VERSIONRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROTOCOLSERVICE)

DESCRIPTOR.services_by_name['ProtocolService'] = _PROTOCOLSERVICE

# @@protoc_insertion_point(module_scope)

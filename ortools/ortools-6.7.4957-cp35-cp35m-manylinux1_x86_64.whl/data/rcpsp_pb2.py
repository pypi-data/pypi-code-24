# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ortools/data/rcpsp.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ortools/data/rcpsp.proto',
  package='operations_research.data.rcpsp',
  syntax='proto3',
  serialized_pb=_b('\n\x18ortools/data/rcpsp.proto\x12\x1eoperations_research.data.rcpsp\"\\\n\x08Resource\x12\x14\n\x0cmax_capacity\x18\x01 \x01(\x05\x12\x14\n\x0cmin_capacity\x18\x02 \x01(\x05\x12\x11\n\trenewable\x18\x03 \x01(\x08\x12\x11\n\tunit_cost\x18\x04 \x01(\x05\">\n\x06Recipe\x12\x10\n\x08\x64uration\x18\x01 \x01(\x05\x12\x0f\n\x07\x64\x65mands\x18\x02 \x03(\x05\x12\x11\n\tresources\x18\x03 \x03(\x05\"%\n\x0fPerRecipeDelays\x12\x12\n\nmin_delays\x18\x01 \x03(\x05\"\\\n\x12PerSuccessorDelays\x12\x46\n\rrecipe_delays\x18\x01 \x03(\x0b\x32/.operations_research.data.rcpsp.PerRecipeDelays\"\xa1\x01\n\x04Task\x12\x12\n\nsuccessors\x18\x01 \x03(\x05\x12\x37\n\x07recipes\x18\x02 \x03(\x0b\x32&.operations_research.data.rcpsp.Recipe\x12L\n\x10successor_delays\x18\x03 \x03(\x0b\x32\x32.operations_research.data.rcpsp.PerSuccessorDelays\"\xf7\x02\n\x0cRcpspProblem\x12;\n\tresources\x18\x01 \x03(\x0b\x32(.operations_research.data.rcpsp.Resource\x12\x33\n\x05tasks\x18\x02 \x03(\x0b\x32$.operations_research.data.rcpsp.Task\x12\x1c\n\x14is_consumer_producer\x18\x03 \x01(\x08\x12\x1e\n\x16is_resource_investment\x18\x04 \x01(\x08\x12\x14\n\x0cis_rcpsp_max\x18\x05 \x01(\x08\x12\x10\n\x08\x64\x65\x61\x64line\x18\x06 \x01(\x05\x12\x0f\n\x07horizon\x18\x07 \x01(\x05\x12\x14\n\x0crelease_date\x18\x08 \x01(\x05\x12\x16\n\x0etardiness_cost\x18\t \x01(\x05\x12\x10\n\x08mpm_time\x18\n \x01(\x05\x12\x0c\n\x04seed\x18\x0b \x01(\x03\x12\x10\n\x08\x62\x61sedata\x18\x0c \x01(\t\x12\x10\n\x08\x64ue_date\x18\r \x01(\x05\x12\x0c\n\x04name\x18\x0e \x01(\tB=\n\x1d\x63om.google.ortools.data.rcpspP\x01\xaa\x02\x19Google.OrTools.Data.Rcpspb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RESOURCE = _descriptor.Descriptor(
  name='Resource',
  full_name='operations_research.data.rcpsp.Resource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_capacity', full_name='operations_research.data.rcpsp.Resource.max_capacity', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_capacity', full_name='operations_research.data.rcpsp.Resource.min_capacity', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='renewable', full_name='operations_research.data.rcpsp.Resource.renewable', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_cost', full_name='operations_research.data.rcpsp.Resource.unit_cost', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=152,
)


_RECIPE = _descriptor.Descriptor(
  name='Recipe',
  full_name='operations_research.data.rcpsp.Recipe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='duration', full_name='operations_research.data.rcpsp.Recipe.duration', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='demands', full_name='operations_research.data.rcpsp.Recipe.demands', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resources', full_name='operations_research.data.rcpsp.Recipe.resources', index=2,
      number=3, type=5, cpp_type=1, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=216,
)


_PERRECIPEDELAYS = _descriptor.Descriptor(
  name='PerRecipeDelays',
  full_name='operations_research.data.rcpsp.PerRecipeDelays',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_delays', full_name='operations_research.data.rcpsp.PerRecipeDelays.min_delays', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=255,
)


_PERSUCCESSORDELAYS = _descriptor.Descriptor(
  name='PerSuccessorDelays',
  full_name='operations_research.data.rcpsp.PerSuccessorDelays',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recipe_delays', full_name='operations_research.data.rcpsp.PerSuccessorDelays.recipe_delays', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=349,
)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='operations_research.data.rcpsp.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='successors', full_name='operations_research.data.rcpsp.Task.successors', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recipes', full_name='operations_research.data.rcpsp.Task.recipes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='successor_delays', full_name='operations_research.data.rcpsp.Task.successor_delays', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=352,
  serialized_end=513,
)


_RCPSPPROBLEM = _descriptor.Descriptor(
  name='RcpspProblem',
  full_name='operations_research.data.rcpsp.RcpspProblem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='operations_research.data.rcpsp.RcpspProblem.resources', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tasks', full_name='operations_research.data.rcpsp.RcpspProblem.tasks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_consumer_producer', full_name='operations_research.data.rcpsp.RcpspProblem.is_consumer_producer', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_resource_investment', full_name='operations_research.data.rcpsp.RcpspProblem.is_resource_investment', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_rcpsp_max', full_name='operations_research.data.rcpsp.RcpspProblem.is_rcpsp_max', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deadline', full_name='operations_research.data.rcpsp.RcpspProblem.deadline', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='horizon', full_name='operations_research.data.rcpsp.RcpspProblem.horizon', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='release_date', full_name='operations_research.data.rcpsp.RcpspProblem.release_date', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tardiness_cost', full_name='operations_research.data.rcpsp.RcpspProblem.tardiness_cost', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mpm_time', full_name='operations_research.data.rcpsp.RcpspProblem.mpm_time', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seed', full_name='operations_research.data.rcpsp.RcpspProblem.seed', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basedata', full_name='operations_research.data.rcpsp.RcpspProblem.basedata', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='due_date', full_name='operations_research.data.rcpsp.RcpspProblem.due_date', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='operations_research.data.rcpsp.RcpspProblem.name', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=516,
  serialized_end=891,
)

_PERSUCCESSORDELAYS.fields_by_name['recipe_delays'].message_type = _PERRECIPEDELAYS
_TASK.fields_by_name['recipes'].message_type = _RECIPE
_TASK.fields_by_name['successor_delays'].message_type = _PERSUCCESSORDELAYS
_RCPSPPROBLEM.fields_by_name['resources'].message_type = _RESOURCE
_RCPSPPROBLEM.fields_by_name['tasks'].message_type = _TASK
DESCRIPTOR.message_types_by_name['Resource'] = _RESOURCE
DESCRIPTOR.message_types_by_name['Recipe'] = _RECIPE
DESCRIPTOR.message_types_by_name['PerRecipeDelays'] = _PERRECIPEDELAYS
DESCRIPTOR.message_types_by_name['PerSuccessorDelays'] = _PERSUCCESSORDELAYS
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['RcpspProblem'] = _RCPSPPROBLEM

Resource = _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCE,
  __module__ = 'ortools.data.rcpsp_pb2'
  # @@protoc_insertion_point(class_scope:operations_research.data.rcpsp.Resource)
  ))
_sym_db.RegisterMessage(Resource)

Recipe = _reflection.GeneratedProtocolMessageType('Recipe', (_message.Message,), dict(
  DESCRIPTOR = _RECIPE,
  __module__ = 'ortools.data.rcpsp_pb2'
  # @@protoc_insertion_point(class_scope:operations_research.data.rcpsp.Recipe)
  ))
_sym_db.RegisterMessage(Recipe)

PerRecipeDelays = _reflection.GeneratedProtocolMessageType('PerRecipeDelays', (_message.Message,), dict(
  DESCRIPTOR = _PERRECIPEDELAYS,
  __module__ = 'ortools.data.rcpsp_pb2'
  # @@protoc_insertion_point(class_scope:operations_research.data.rcpsp.PerRecipeDelays)
  ))
_sym_db.RegisterMessage(PerRecipeDelays)

PerSuccessorDelays = _reflection.GeneratedProtocolMessageType('PerSuccessorDelays', (_message.Message,), dict(
  DESCRIPTOR = _PERSUCCESSORDELAYS,
  __module__ = 'ortools.data.rcpsp_pb2'
  # @@protoc_insertion_point(class_scope:operations_research.data.rcpsp.PerSuccessorDelays)
  ))
_sym_db.RegisterMessage(PerSuccessorDelays)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), dict(
  DESCRIPTOR = _TASK,
  __module__ = 'ortools.data.rcpsp_pb2'
  # @@protoc_insertion_point(class_scope:operations_research.data.rcpsp.Task)
  ))
_sym_db.RegisterMessage(Task)

RcpspProblem = _reflection.GeneratedProtocolMessageType('RcpspProblem', (_message.Message,), dict(
  DESCRIPTOR = _RCPSPPROBLEM,
  __module__ = 'ortools.data.rcpsp_pb2'
  # @@protoc_insertion_point(class_scope:operations_research.data.rcpsp.RcpspProblem)
  ))
_sym_db.RegisterMessage(RcpspProblem)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\035com.google.ortools.data.rcpspP\001\252\002\031Google.OrTools.Data.Rcpsp'))
# @@protoc_insertion_point(module_scope)

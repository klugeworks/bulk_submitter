# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tokenizer_job.proto

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
  name='tokenizer_job.proto',
  package='kluge.bulk_submitter',
  serialized_pb=_b('\n\x13tokenizer_job.proto\x12\x14kluge.bulk_submitter\"\xa2\x02\n\x13TokenizerJobMessage\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\x12\x11\n\x05\x63hunk\x18\x03 \x01(\x05:\x02-1\x12\x11\n\taudio_uri\x18\x05 \x01(\t\x12\x11\n\tmarks_uri\x18\x06 \x01(\t\x12\x11\n\traw_audio\x18\x08 \x01(\x0c\x12\x45\n\x06\x66ormat\x18\t \x01(\x0e\x32\x35.kluge.bulk_submitter.TokenizerJobMessage.AudioFormat\x12\x13\n\x0bsample_rate\x18\n \x01(\x05\x12\x13\n\x0bsample_size\x18\x0b \x01(\x05\"/\n\x0b\x41udioFormat\x12\x07\n\x03WAV\x10\x00\x12\x06\n\x02UL\x10\x01\x12\x06\n\x02LU\x10\x02\x12\x07\n\x03SPH\x10\x03\x42\x46\n+com.bbn.JCube.hlt.speech.analytic.tokenizerB\x15PBTokenizerJobMessageH\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_TOKENIZERJOBMESSAGE_AUDIOFORMAT = _descriptor.EnumDescriptor(
  name='AudioFormat',
  full_name='kluge.bulk_submitter.TokenizerJobMessage.AudioFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WAV', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LU', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPH', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=289,
  serialized_end=336,
)
_sym_db.RegisterEnumDescriptor(_TOKENIZERJOBMESSAGE_AUDIOFORMAT)


_TOKENIZERJOBMESSAGE = _descriptor.Descriptor(
  name='TokenizerJobMessage',
  full_name='kluge.bulk_submitter.TokenizerJobMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='kluge.bulk_submitter.TokenizerJobMessage.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language', full_name='kluge.bulk_submitter.TokenizerJobMessage.language', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chunk', full_name='kluge.bulk_submitter.TokenizerJobMessage.chunk', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_uri', full_name='kluge.bulk_submitter.TokenizerJobMessage.audio_uri', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='marks_uri', full_name='kluge.bulk_submitter.TokenizerJobMessage.marks_uri', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_audio', full_name='kluge.bulk_submitter.TokenizerJobMessage.raw_audio', index=5,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='format', full_name='kluge.bulk_submitter.TokenizerJobMessage.format', index=6,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sample_rate', full_name='kluge.bulk_submitter.TokenizerJobMessage.sample_rate', index=7,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sample_size', full_name='kluge.bulk_submitter.TokenizerJobMessage.sample_size', index=8,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TOKENIZERJOBMESSAGE_AUDIOFORMAT,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=336,
)

_TOKENIZERJOBMESSAGE.fields_by_name['format'].enum_type = _TOKENIZERJOBMESSAGE_AUDIOFORMAT
_TOKENIZERJOBMESSAGE_AUDIOFORMAT.containing_type = _TOKENIZERJOBMESSAGE
DESCRIPTOR.message_types_by_name['TokenizerJobMessage'] = _TOKENIZERJOBMESSAGE

TokenizerJobMessage = _reflection.GeneratedProtocolMessageType('TokenizerJobMessage', (_message.Message,), dict(
  DESCRIPTOR = _TOKENIZERJOBMESSAGE,
  __module__ = 'tokenizer_job_pb2'
  # @@protoc_insertion_point(class_scope:kluge.bulk_submitter.TokenizerJobMessage)
  ))
_sym_db.RegisterMessage(TokenizerJobMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n+com.bbn.JCube.hlt.speech.analytic.tokenizerB\025PBTokenizerJobMessageH\001'))
# @@protoc_insertion_point(module_scope)
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: train.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'train.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0btrain.proto\"1\n\x0cTrainRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x10\n\x08train_id\x18\x02 \x01(\t\"1\n\rTrainResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2:\n\x0cTrainService\x12*\n\tBookTrain\x12\r.TrainRequest\x1a\x0e.TrainResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'train_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TRAINREQUEST']._serialized_start=15
  _globals['_TRAINREQUEST']._serialized_end=64
  _globals['_TRAINRESPONSE']._serialized_start=66
  _globals['_TRAINRESPONSE']._serialized_end=115
  _globals['_TRAINSERVICE']._serialized_start=117
  _globals['_TRAINSERVICE']._serialized_end=175
# @@protoc_insertion_point(module_scope)

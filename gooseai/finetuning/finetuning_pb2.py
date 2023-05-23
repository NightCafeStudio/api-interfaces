# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: finetuning.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x66inetuning.proto\x12\x07gooseai\"\xf1\x01\n\x0f\x46ineTuningModel\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12%\n\x04mode\x18\x04 \x01(\x0e\x32\x17.gooseai.FineTuningMode\x12\x18\n\x0bobject_name\x18\x05 \x01(\tH\x00\x88\x01\x01\x12\x12\n\nproject_id\x18\x06 \x01(\t\x12\x10\n\x08\x64uration\x18\x07 \x01(\x01\x12)\n\x06status\x18\x08 \x01(\x0e\x32\x19.gooseai.FineTuningStatus\x12\x11\n\tengine_id\x18\t \x01(\tB\x0e\n\x0c_object_name\"\xa8\x01\n\x12\x43reateModelRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\x04mode\x18\x02 \x01(\x0e\x32\x17.gooseai.FineTuningModeH\x00\x88\x01\x01\x12\x18\n\x0bobject_name\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x12\n\nproject_id\x18\x04 \x01(\t\x12\x11\n\tengine_id\x18\x05 \x01(\tB\x07\n\x05_modeB\x0e\n\x0c_object_name\">\n\x13\x43reateModelResponse\x12\'\n\x05model\x18\x01 \x01(\x0b\x32\x18.gooseai.FineTuningModel\"\x1d\n\x0fGetModelRequest\x12\n\n\x02id\x18\x01 \x01(\t\";\n\x10GetModelResponse\x12\'\n\x05model\x18\x01 \x01(\x0b\x32\x18.gooseai.FineTuningModel\"\xb4\x01\n\x12UpdateModelRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12*\n\x04mode\x18\x03 \x01(\x0e\x32\x17.gooseai.FineTuningModeH\x00\x88\x01\x01\x12\x18\n\x0bobject_name\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x12\n\nproject_id\x18\x05 \x01(\t\x12\x11\n\tengine_id\x18\x06 \x01(\tB\x07\n\x05_modeB\x0e\n\x0c_object_name\">\n\x13UpdateModelResponse\x12\'\n\x05model\x18\x01 \x01(\x0b\x32\x18.gooseai.FineTuningModel\" \n\x12\x44\x65leteModelRequest\x12\n\n\x02id\x18\x01 \x01(\t\">\n\x13\x44\x65leteModelResponse\x12\'\n\x05model\x18\x01 \x01(\x0b\x32\x18.gooseai.FineTuningModel\"\"\n\x14ResubmitModelRequest\x12\n\n\x02id\x18\x01 \x01(\t\"@\n\x15ResubmitModelResponse\x12\'\n\x05model\x18\x01 \x01(\x0b\x32\x18.gooseai.FineTuningModel\">\n\x11ListModelsRequest\x12\x10\n\x06org_id\x18\x01 \x01(\tH\x00\x12\x11\n\x07user_id\x18\x02 \x01(\tH\x00\x42\x04\n\x02id\">\n\x12ListModelsResponse\x12(\n\x06models\x18\x01 \x03(\x0b\x32\x18.gooseai.FineTuningModel*\x86\x01\n\x0e\x46ineTuningMode\x12 \n\x1c\x46INE_TUNING_MODE_UNSPECIFIED\x10\x00\x12\x19\n\x15\x46INE_TUNING_MODE_FACE\x10\x01\x12\x1a\n\x16\x46INE_TUNING_MODE_STYLE\x10\x02\x12\x1b\n\x17\x46INE_TUNING_MODE_OBJECT\x10\x03*\xb9\x01\n\x10\x46ineTuningStatus\x12\"\n\x1e\x46INE_TUNING_STATUS_NOT_STARTED\x10\x00\x12\x1e\n\x1a\x46INE_TUNING_STATUS_RUNNING\x10\x01\x12 \n\x1c\x46INE_TUNING_STATUS_COMPLETED\x10\x02\x12\x1d\n\x19\x46INE_TUNING_STATUS_FAILED\x10\x03\x12 \n\x1c\x46INE_TUNING_STATUS_SUBMITTED\x10\x04\x32\xc9\x03\n\x11\x46ineTuningService\x12H\n\x0b\x43reateModel\x12\x1b.gooseai.CreateModelRequest\x1a\x1c.gooseai.CreateModelResponse\x12?\n\x08GetModel\x12\x18.gooseai.GetModelRequest\x1a\x19.gooseai.GetModelResponse\x12H\n\x0bUpdateModel\x12\x1b.gooseai.UpdateModelRequest\x1a\x1c.gooseai.UpdateModelResponse\x12H\n\x0b\x44\x65leteModel\x12\x1b.gooseai.DeleteModelRequest\x1a\x1c.gooseai.DeleteModelResponse\x12N\n\rResubmitModel\x12\x1d.gooseai.ResubmitModelRequest\x1a\x1e.gooseai.ResubmitModelResponse\x12\x45\n\nListModels\x12\x1a.gooseai.ListModelsRequest\x1a\x1b.gooseai.ListModelsResponseB;Z9github.com/stability-ai/api-interfaces/gooseai/finetuningb\x06proto3')

_FINETUNINGMODE = DESCRIPTOR.enum_types_by_name['FineTuningMode']
FineTuningMode = enum_type_wrapper.EnumTypeWrapper(_FINETUNINGMODE)
_FINETUNINGSTATUS = DESCRIPTOR.enum_types_by_name['FineTuningStatus']
FineTuningStatus = enum_type_wrapper.EnumTypeWrapper(_FINETUNINGSTATUS)
FINE_TUNING_MODE_UNSPECIFIED = 0
FINE_TUNING_MODE_FACE = 1
FINE_TUNING_MODE_STYLE = 2
FINE_TUNING_MODE_OBJECT = 3
FINE_TUNING_STATUS_NOT_STARTED = 0
FINE_TUNING_STATUS_RUNNING = 1
FINE_TUNING_STATUS_COMPLETED = 2
FINE_TUNING_STATUS_FAILED = 3
FINE_TUNING_STATUS_SUBMITTED = 4


_FINETUNINGMODEL = DESCRIPTOR.message_types_by_name['FineTuningModel']
_CREATEMODELREQUEST = DESCRIPTOR.message_types_by_name['CreateModelRequest']
_CREATEMODELRESPONSE = DESCRIPTOR.message_types_by_name['CreateModelResponse']
_GETMODELREQUEST = DESCRIPTOR.message_types_by_name['GetModelRequest']
_GETMODELRESPONSE = DESCRIPTOR.message_types_by_name['GetModelResponse']
_UPDATEMODELREQUEST = DESCRIPTOR.message_types_by_name['UpdateModelRequest']
_UPDATEMODELRESPONSE = DESCRIPTOR.message_types_by_name['UpdateModelResponse']
_DELETEMODELREQUEST = DESCRIPTOR.message_types_by_name['DeleteModelRequest']
_DELETEMODELRESPONSE = DESCRIPTOR.message_types_by_name['DeleteModelResponse']
_RESUBMITMODELREQUEST = DESCRIPTOR.message_types_by_name['ResubmitModelRequest']
_RESUBMITMODELRESPONSE = DESCRIPTOR.message_types_by_name['ResubmitModelResponse']
_LISTMODELSREQUEST = DESCRIPTOR.message_types_by_name['ListModelsRequest']
_LISTMODELSRESPONSE = DESCRIPTOR.message_types_by_name['ListModelsResponse']
FineTuningModel = _reflection.GeneratedProtocolMessageType('FineTuningModel', (_message.Message,), {
  'DESCRIPTOR' : _FINETUNINGMODEL,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.FineTuningModel)
  })
_sym_db.RegisterMessage(FineTuningModel)

CreateModelRequest = _reflection.GeneratedProtocolMessageType('CreateModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMODELREQUEST,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.CreateModelRequest)
  })
_sym_db.RegisterMessage(CreateModelRequest)

CreateModelResponse = _reflection.GeneratedProtocolMessageType('CreateModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMODELRESPONSE,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.CreateModelResponse)
  })
_sym_db.RegisterMessage(CreateModelResponse)

GetModelRequest = _reflection.GeneratedProtocolMessageType('GetModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELREQUEST,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.GetModelRequest)
  })
_sym_db.RegisterMessage(GetModelRequest)

GetModelResponse = _reflection.GeneratedProtocolMessageType('GetModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELRESPONSE,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.GetModelResponse)
  })
_sym_db.RegisterMessage(GetModelResponse)

UpdateModelRequest = _reflection.GeneratedProtocolMessageType('UpdateModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMODELREQUEST,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.UpdateModelRequest)
  })
_sym_db.RegisterMessage(UpdateModelRequest)

UpdateModelResponse = _reflection.GeneratedProtocolMessageType('UpdateModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMODELRESPONSE,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.UpdateModelResponse)
  })
_sym_db.RegisterMessage(UpdateModelResponse)

DeleteModelRequest = _reflection.GeneratedProtocolMessageType('DeleteModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMODELREQUEST,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.DeleteModelRequest)
  })
_sym_db.RegisterMessage(DeleteModelRequest)

DeleteModelResponse = _reflection.GeneratedProtocolMessageType('DeleteModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMODELRESPONSE,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.DeleteModelResponse)
  })
_sym_db.RegisterMessage(DeleteModelResponse)

ResubmitModelRequest = _reflection.GeneratedProtocolMessageType('ResubmitModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESUBMITMODELREQUEST,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ResubmitModelRequest)
  })
_sym_db.RegisterMessage(ResubmitModelRequest)

ResubmitModelResponse = _reflection.GeneratedProtocolMessageType('ResubmitModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESUBMITMODELRESPONSE,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ResubmitModelResponse)
  })
_sym_db.RegisterMessage(ResubmitModelResponse)

ListModelsRequest = _reflection.GeneratedProtocolMessageType('ListModelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTMODELSREQUEST,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ListModelsRequest)
  })
_sym_db.RegisterMessage(ListModelsRequest)

ListModelsResponse = _reflection.GeneratedProtocolMessageType('ListModelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMODELSRESPONSE,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ListModelsResponse)
  })
_sym_db.RegisterMessage(ListModelsResponse)

_FINETUNINGSERVICE = DESCRIPTOR.services_by_name['FineTuningService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z9github.com/stability-ai/api-interfaces/gooseai/finetuning'
  _FINETUNINGMODE._serialized_start=1176
  _FINETUNINGMODE._serialized_end=1310
  _FINETUNINGSTATUS._serialized_start=1313
  _FINETUNINGSTATUS._serialized_end=1498
  _FINETUNINGMODEL._serialized_start=30
  _FINETUNINGMODEL._serialized_end=271
  _CREATEMODELREQUEST._serialized_start=274
  _CREATEMODELREQUEST._serialized_end=442
  _CREATEMODELRESPONSE._serialized_start=444
  _CREATEMODELRESPONSE._serialized_end=506
  _GETMODELREQUEST._serialized_start=508
  _GETMODELREQUEST._serialized_end=537
  _GETMODELRESPONSE._serialized_start=539
  _GETMODELRESPONSE._serialized_end=598
  _UPDATEMODELREQUEST._serialized_start=601
  _UPDATEMODELREQUEST._serialized_end=781
  _UPDATEMODELRESPONSE._serialized_start=783
  _UPDATEMODELRESPONSE._serialized_end=845
  _DELETEMODELREQUEST._serialized_start=847
  _DELETEMODELREQUEST._serialized_end=879
  _DELETEMODELRESPONSE._serialized_start=881
  _DELETEMODELRESPONSE._serialized_end=943
  _RESUBMITMODELREQUEST._serialized_start=945
  _RESUBMITMODELREQUEST._serialized_end=979
  _RESUBMITMODELRESPONSE._serialized_start=981
  _RESUBMITMODELRESPONSE._serialized_end=1045
  _LISTMODELSREQUEST._serialized_start=1047
  _LISTMODELSREQUEST._serialized_end=1109
  _LISTMODELSRESPONSE._serialized_start=1111
  _LISTMODELSRESPONSE._serialized_end=1173
  _FINETUNINGSERVICE._serialized_start=1501
  _FINETUNINGSERVICE._serialized_end=1958
# @@protoc_insertion_point(module_scope)

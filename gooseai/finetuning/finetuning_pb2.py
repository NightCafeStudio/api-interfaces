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


import dashboard_pb2 as dashboard__pb2
import project_pb2 as project__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x66inetuning.proto\x12\x07gooseai\x1a\x0f\x64\x61shboard.proto\x1a\rproject.proto\"\x8e\x02\n\rFineTuningJob\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1b\n\x04user\x18\x02 \x01(\x0b\x32\r.gooseai.User\x12\x12\n\nmodel_name\x18\x03 \x01(\t\x12*\n\x04mode\x18\x04 \x01(\x0e\x32\x17.gooseai.FineTuningModeH\x00\x88\x01\x01\x12\x18\n\x0bobject_name\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\x12\n\nproject_id\x18\x06 \x01(\t\x12\x17\n\x0fjob_output_path\x18\x07 \x01(\t\x12\x10\n\x08\x64uration\x18\x08 \x01(\x01\x12\"\n\x06status\x18\t \x01(\x0e\x32\x12.gooseai.JobStatusB\x07\n\x05_modeB\x0e\n\x0c_object_name\"\xa3\x01\n\x1a\x43reateFineTuningJobRequest\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12*\n\x04mode\x18\x02 \x01(\x0e\x32\x17.gooseai.FineTuningModeH\x00\x88\x01\x01\x12\x18\n\x0bobject_name\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x12\n\nproject_id\x18\x04 \x01(\tB\x07\n\x05_modeB\x0e\n\x0c_object_name\"\xaf\x01\n\x1aUpdateFineTuningJobRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nmodel_name\x18\x02 \x01(\t\x12*\n\x04mode\x18\x03 \x01(\x0e\x32\x17.gooseai.FineTuningModeH\x00\x88\x01\x01\x12\x18\n\x0bobject_name\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x12\n\nproject_id\x18\x05 \x01(\tB\x07\n\x05_modeB\x0e\n\x0c_object_name\"&\n\x18\x46ineTuningJobRequestById\x12\n\n\x02id\x18\x01 \x01(\t\"E\n\x13\x46ineTuningJobStatus\x12\n\n\x02id\x18\x01 \x01(\t\x12\"\n\x06status\x18\x02 \x01(\x0e\x32\x12.gooseai.JobStatus\"\xa5\x01\n\x15JobStatusNotification\x12\x0e\n\x06org_id\x18\x01 \x01(\t\x12\x1c\n\x14\x66ine_tune_request_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\"\n\x06status\x18\x04 \x01(\x0e\x32\x12.gooseai.JobStatus\x12\x17\n\x0fjob_output_path\x18\x05 \x01(\t\x12\x10\n\x08\x64uration\x18\x06 \x01(\x01\".\n\x1bProcessNotificationResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"*\n\x1cResubmitFineTuningJobRequest\x12\n\n\x02id\x18\x01 \x01(\t*\x8b\x01\n\x0e\x46ineTuningMode\x12%\n!FINE_TUNING_MODE_NONE_UNSPECIFIED\x10\x00\x12\x19\n\x15\x46INE_TUNING_MODE_FACE\x10\x01\x12\x1a\n\x16\x46INE_TUNING_MODE_STYLE\x10\x02\x12\x1b\n\x17\x46INE_TUNING_MODE_OBJECT\x10\x03*|\n\tJobStatus\x12&\n\"JOB_STATUS_NOT_STARTED_UNSPECIFIED\x10\x00\x12\x16\n\x12JOB_STATUS_RUNNING\x10\x01\x12\x18\n\x14JOB_STATUS_COMPLETED\x10\x02\x12\x15\n\x11JOB_STATUS_FAILED\x10\x03\x32\xf2\x04\n\x11\x46ineTuningService\x12R\n\x13\x43reateFineTuningJob\x12#.gooseai.CreateFineTuningJobRequest\x1a\x16.gooseai.FineTuningJob\x12Q\n\x14GetFineTuningJobById\x12!.gooseai.FineTuningJobRequestById\x1a\x16.gooseai.FineTuningJob\x12R\n\x13UpdateFineTuningJob\x12#.gooseai.UpdateFineTuningJobRequest\x1a\x16.gooseai.FineTuningJob\x12P\n\x13\x44\x65leteFineTuningJob\x12!.gooseai.FineTuningJobRequestById\x1a\x16.gooseai.FineTuningJob\x12[\n\x18GetFineTuningJobProgress\x12!.gooseai.FineTuningJobRequestById\x1a\x1c.gooseai.FineTuningJobStatus\x12[\n\x13ProcessNotification\x12\x1e.gooseai.JobStatusNotification\x1a$.gooseai.ProcessNotificationResponse\x12V\n\x15ResubmitFineTuningJob\x12%.gooseai.ResubmitFineTuningJobRequest\x1a\x16.gooseai.FineTuningJobB;Z9github.com/stability-ai/api-interfaces/gooseai/finetuningb\x06proto3')

_FINETUNINGMODE = DESCRIPTOR.enum_types_by_name['FineTuningMode']
FineTuningMode = enum_type_wrapper.EnumTypeWrapper(_FINETUNINGMODE)
_JOBSTATUS = DESCRIPTOR.enum_types_by_name['JobStatus']
JobStatus = enum_type_wrapper.EnumTypeWrapper(_JOBSTATUS)
FINE_TUNING_MODE_NONE_UNSPECIFIED = 0
FINE_TUNING_MODE_FACE = 1
FINE_TUNING_MODE_STYLE = 2
FINE_TUNING_MODE_OBJECT = 3
JOB_STATUS_NOT_STARTED_UNSPECIFIED = 0
JOB_STATUS_RUNNING = 1
JOB_STATUS_COMPLETED = 2
JOB_STATUS_FAILED = 3


_FINETUNINGJOB = DESCRIPTOR.message_types_by_name['FineTuningJob']
_CREATEFINETUNINGJOBREQUEST = DESCRIPTOR.message_types_by_name['CreateFineTuningJobRequest']
_UPDATEFINETUNINGJOBREQUEST = DESCRIPTOR.message_types_by_name['UpdateFineTuningJobRequest']
_FINETUNINGJOBREQUESTBYID = DESCRIPTOR.message_types_by_name['FineTuningJobRequestById']
_FINETUNINGJOBSTATUS = DESCRIPTOR.message_types_by_name['FineTuningJobStatus']
_JOBSTATUSNOTIFICATION = DESCRIPTOR.message_types_by_name['JobStatusNotification']
_PROCESSNOTIFICATIONRESPONSE = DESCRIPTOR.message_types_by_name['ProcessNotificationResponse']
_RESUBMITFINETUNINGJOBREQUEST = DESCRIPTOR.message_types_by_name['ResubmitFineTuningJobRequest']
FineTuningJob = _reflection.GeneratedProtocolMessageType('FineTuningJob', (_message.Message,), {
  'DESCRIPTOR' : _FINETUNINGJOB,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.FineTuningJob)
  })
_sym_db.RegisterMessage(FineTuningJob)

CreateFineTuningJobRequest = _reflection.GeneratedProtocolMessageType('CreateFineTuningJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEFINETUNINGJOBREQUEST,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.CreateFineTuningJobRequest)
  })
_sym_db.RegisterMessage(CreateFineTuningJobRequest)

UpdateFineTuningJobRequest = _reflection.GeneratedProtocolMessageType('UpdateFineTuningJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEFINETUNINGJOBREQUEST,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.UpdateFineTuningJobRequest)
  })
_sym_db.RegisterMessage(UpdateFineTuningJobRequest)

FineTuningJobRequestById = _reflection.GeneratedProtocolMessageType('FineTuningJobRequestById', (_message.Message,), {
  'DESCRIPTOR' : _FINETUNINGJOBREQUESTBYID,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.FineTuningJobRequestById)
  })
_sym_db.RegisterMessage(FineTuningJobRequestById)

FineTuningJobStatus = _reflection.GeneratedProtocolMessageType('FineTuningJobStatus', (_message.Message,), {
  'DESCRIPTOR' : _FINETUNINGJOBSTATUS,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.FineTuningJobStatus)
  })
_sym_db.RegisterMessage(FineTuningJobStatus)

JobStatusNotification = _reflection.GeneratedProtocolMessageType('JobStatusNotification', (_message.Message,), {
  'DESCRIPTOR' : _JOBSTATUSNOTIFICATION,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.JobStatusNotification)
  })
_sym_db.RegisterMessage(JobStatusNotification)

ProcessNotificationResponse = _reflection.GeneratedProtocolMessageType('ProcessNotificationResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSNOTIFICATIONRESPONSE,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ProcessNotificationResponse)
  })
_sym_db.RegisterMessage(ProcessNotificationResponse)

ResubmitFineTuningJobRequest = _reflection.GeneratedProtocolMessageType('ResubmitFineTuningJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESUBMITFINETUNINGJOBREQUEST,
  '__module__' : 'finetuning_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ResubmitFineTuningJobRequest)
  })
_sym_db.RegisterMessage(ResubmitFineTuningJobRequest)

_FINETUNINGSERVICE = DESCRIPTOR.services_by_name['FineTuningService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z9github.com/stability-ai/api-interfaces/gooseai/finetuning'
  _FINETUNINGMODE._serialized_start=1050
  _FINETUNINGMODE._serialized_end=1189
  _JOBSTATUS._serialized_start=1191
  _JOBSTATUS._serialized_end=1315
  _FINETUNINGJOB._serialized_start=62
  _FINETUNINGJOB._serialized_end=332
  _CREATEFINETUNINGJOBREQUEST._serialized_start=335
  _CREATEFINETUNINGJOBREQUEST._serialized_end=498
  _UPDATEFINETUNINGJOBREQUEST._serialized_start=501
  _UPDATEFINETUNINGJOBREQUEST._serialized_end=676
  _FINETUNINGJOBREQUESTBYID._serialized_start=678
  _FINETUNINGJOBREQUESTBYID._serialized_end=716
  _FINETUNINGJOBSTATUS._serialized_start=718
  _FINETUNINGJOBSTATUS._serialized_end=787
  _JOBSTATUSNOTIFICATION._serialized_start=790
  _JOBSTATUSNOTIFICATION._serialized_end=955
  _PROCESSNOTIFICATIONRESPONSE._serialized_start=957
  _PROCESSNOTIFICATIONRESPONSE._serialized_end=1003
  _RESUBMITFINETUNINGJOBREQUEST._serialized_start=1005
  _RESUBMITFINETUNINGJOBREQUEST._serialized_end=1047
  _FINETUNINGSERVICE._serialized_start=1318
  _FINETUNINGSERVICE._serialized_end=1944
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rproject.proto\x12\x07gooseai\"\x92\x01\n\x0cProjectAsset\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12%\n\x03use\x18\x03 \x01(\x0e\x32\x18.gooseai.ProjectAssetUse\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0c\n\x04size\x18\x05 \x01(\x04\x12\x12\n\ncreated_at\x18\x06 \x01(\x04\x12\x12\n\nupdated_at\x18\x07 \x01(\x04\"\x88\x02\n\x07Project\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x10\n\x08owner_id\x18\x03 \x01(\t\x12&\n\x06\x61\x63\x63\x65ss\x18\x04 \x01(\x0e\x32\x16.gooseai.ProjectAccess\x12&\n\x06status\x18\x05 \x01(\x0e\x32\x16.gooseai.ProjectStatus\x12\x0c\n\x04size\x18\x06 \x01(\x04\x12#\n\x04\x66ile\x18\x07 \x01(\x0b\x32\x15.gooseai.ProjectAsset\x12\x12\n\ncreated_at\x18\x08 \x01(\x04\x12\x12\n\nupdated_at\x18\t \x01(\x04\x12%\n\x06\x61ssets\x18\n \x03(\x0b\x32\x15.gooseai.ProjectAsset\"\xcc\x01\n\x14\x43reateProjectRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x15\n\x08owner_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12&\n\x06\x61\x63\x63\x65ss\x18\x03 \x01(\x0e\x32\x16.gooseai.ProjectAccess\x12&\n\x06status\x18\x04 \x01(\x0e\x32\x16.gooseai.ProjectStatus\x12(\n\x04\x66ile\x18\x05 \x01(\x0b\x32\x15.gooseai.ProjectAssetH\x01\x88\x01\x01\x42\x0b\n\t_owner_idB\x07\n\x05_file\"\x87\x02\n\x14UpdateProjectRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08owner_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05title\x18\x03 \x01(\tH\x01\x88\x01\x01\x12+\n\x06\x61\x63\x63\x65ss\x18\x04 \x01(\x0e\x32\x16.gooseai.ProjectAccessH\x02\x88\x01\x01\x12+\n\x06status\x18\x05 \x01(\x0e\x32\x16.gooseai.ProjectStatusH\x03\x88\x01\x01\x12(\n\x04\x66ile\x18\x06 \x01(\x0b\x32\x15.gooseai.ProjectAssetH\x04\x88\x01\x01\x42\x0b\n\t_owner_idB\x08\n\x06_titleB\t\n\x07_accessB\t\n\x07_statusB\x07\n\x05_file\"8\n\x12ListProjectRequest\x12\x15\n\x08owner_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_owner_id\"C\n\x11GetProjectRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08owner_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_owner_id\"F\n\x14\x44\x65leteProjectRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08owner_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_owner_id*F\n\rProjectAccess\x12\x1a\n\x16PROJECT_ACCESS_PRIVATE\x10\x00\x12\x19\n\x15PROJECT_ACCESS_PUBLIC\x10\x01*c\n\rProjectStatus\x12\x1b\n\x17PROJECT_STATUS_INACTIVE\x10\x00\x12\x19\n\x15PROJECT_STATUS_ACTIVE\x10\x01\x12\x1a\n\x16PROJECT_STATUS_DELETED\x10\x02*\xb0\x01\n\x0fProjectAssetUse\x12\x1f\n\x1bPROJECT_ASSET_USE_UNDEFINED\x10\x00\x12\x1b\n\x17PROJECT_ASSET_USE_INPUT\x10\x01\x12\x1c\n\x18PROJECT_ASSET_USE_OUTPUT\x10\x02\x12\"\n\x1ePROJECT_ASSET_USE_INTERMEDIATE\x10\x03\x12\x1d\n\x19PROJECT_ASSET_USE_PROJECT\x10\x04\x32\xb9\x02\n\x0eProjectService\x12;\n\x06\x43reate\x12\x1d.gooseai.CreateProjectRequest\x1a\x10.gooseai.Project\"\x00\x12;\n\x06Update\x12\x1d.gooseai.UpdateProjectRequest\x1a\x10.gooseai.Project\"\x00\x12\x39\n\x04List\x12\x1b.gooseai.ListProjectRequest\x1a\x10.gooseai.Project\"\x00\x30\x01\x12\x35\n\x03Get\x12\x1a.gooseai.GetProjectRequest\x1a\x10.gooseai.Project\"\x00\x12;\n\x06\x44\x65lete\x12\x1d.gooseai.DeleteProjectRequest\x1a\x10.gooseai.Project\"\x00\x42\x0cZ\n./;projectb\x06proto3')

_PROJECTACCESS = DESCRIPTOR.enum_types_by_name['ProjectAccess']
ProjectAccess = enum_type_wrapper.EnumTypeWrapper(_PROJECTACCESS)
_PROJECTSTATUS = DESCRIPTOR.enum_types_by_name['ProjectStatus']
ProjectStatus = enum_type_wrapper.EnumTypeWrapper(_PROJECTSTATUS)
_PROJECTASSETUSE = DESCRIPTOR.enum_types_by_name['ProjectAssetUse']
ProjectAssetUse = enum_type_wrapper.EnumTypeWrapper(_PROJECTASSETUSE)
PROJECT_ACCESS_PRIVATE = 0
PROJECT_ACCESS_PUBLIC = 1
PROJECT_STATUS_INACTIVE = 0
PROJECT_STATUS_ACTIVE = 1
PROJECT_STATUS_DELETED = 2
PROJECT_ASSET_USE_UNDEFINED = 0
PROJECT_ASSET_USE_INPUT = 1
PROJECT_ASSET_USE_OUTPUT = 2
PROJECT_ASSET_USE_INTERMEDIATE = 3
PROJECT_ASSET_USE_PROJECT = 4


_PROJECTASSET = DESCRIPTOR.message_types_by_name['ProjectAsset']
_PROJECT = DESCRIPTOR.message_types_by_name['Project']
_CREATEPROJECTREQUEST = DESCRIPTOR.message_types_by_name['CreateProjectRequest']
_UPDATEPROJECTREQUEST = DESCRIPTOR.message_types_by_name['UpdateProjectRequest']
_LISTPROJECTREQUEST = DESCRIPTOR.message_types_by_name['ListProjectRequest']
_GETPROJECTREQUEST = DESCRIPTOR.message_types_by_name['GetProjectRequest']
_DELETEPROJECTREQUEST = DESCRIPTOR.message_types_by_name['DeleteProjectRequest']
ProjectAsset = _reflection.GeneratedProtocolMessageType('ProjectAsset', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTASSET,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ProjectAsset)
  })
_sym_db.RegisterMessage(ProjectAsset)

Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), {
  'DESCRIPTOR' : _PROJECT,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Project)
  })
_sym_db.RegisterMessage(Project)

CreateProjectRequest = _reflection.GeneratedProtocolMessageType('CreateProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPROJECTREQUEST,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.CreateProjectRequest)
  })
_sym_db.RegisterMessage(CreateProjectRequest)

UpdateProjectRequest = _reflection.GeneratedProtocolMessageType('UpdateProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROJECTREQUEST,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.UpdateProjectRequest)
  })
_sym_db.RegisterMessage(UpdateProjectRequest)

ListProjectRequest = _reflection.GeneratedProtocolMessageType('ListProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROJECTREQUEST,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ListProjectRequest)
  })
_sym_db.RegisterMessage(ListProjectRequest)

GetProjectRequest = _reflection.GeneratedProtocolMessageType('GetProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTREQUEST,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.GetProjectRequest)
  })
_sym_db.RegisterMessage(GetProjectRequest)

DeleteProjectRequest = _reflection.GeneratedProtocolMessageType('DeleteProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPROJECTREQUEST,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.DeleteProjectRequest)
  })
_sym_db.RegisterMessage(DeleteProjectRequest)

_PROJECTSERVICE = DESCRIPTOR.services_by_name['ProjectService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\n./;project'
  _PROJECTACCESS._serialized_start=1114
  _PROJECTACCESS._serialized_end=1184
  _PROJECTSTATUS._serialized_start=1186
  _PROJECTSTATUS._serialized_end=1285
  _PROJECTASSETUSE._serialized_start=1288
  _PROJECTASSETUSE._serialized_end=1464
  _PROJECTASSET._serialized_start=27
  _PROJECTASSET._serialized_end=173
  _PROJECT._serialized_start=176
  _PROJECT._serialized_end=440
  _CREATEPROJECTREQUEST._serialized_start=443
  _CREATEPROJECTREQUEST._serialized_end=647
  _UPDATEPROJECTREQUEST._serialized_start=650
  _UPDATEPROJECTREQUEST._serialized_end=913
  _LISTPROJECTREQUEST._serialized_start=915
  _LISTPROJECTREQUEST._serialized_end=971
  _GETPROJECTREQUEST._serialized_start=973
  _GETPROJECTREQUEST._serialized_end=1040
  _DELETEPROJECTREQUEST._serialized_start=1042
  _DELETEPROJECTREQUEST._serialized_end=1112
  _PROJECTSERVICE._serialized_start=1467
  _PROJECTSERVICE._serialized_end=1780
# @@protoc_insertion_point(module_scope)

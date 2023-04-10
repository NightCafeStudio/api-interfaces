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


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
import generation_pb2 as generation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rproject.proto\x12\x07gooseai\x1a\x1cgoogle/protobuf/struct.proto\x1a google/protobuf/field_mask.proto\x1a\x10generation.proto\"\xea\x01\n\x0cProjectAsset\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12%\n\x03use\x18\x03 \x01(\x0e\x32\x18.gooseai.ProjectAssetUse\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0c\n\x04size\x18\x05 \x01(\x04\x12\x12\n\ncreated_at\x18\x06 \x01(\x04\x12\x12\n\nupdated_at\x18\x07 \x01(\x04\x12!\n\x07request\x18\x08 \x01(\x0b\x32\x10.gooseai.Request\x12*\n\x04tags\x18\t \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x88\x01\x01\x42\x07\n\x05_tags\"\x88\x02\n\x07Project\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x10\n\x08owner_id\x18\x03 \x01(\t\x12&\n\x06\x61\x63\x63\x65ss\x18\x04 \x01(\x0e\x32\x16.gooseai.ProjectAccess\x12&\n\x06status\x18\x05 \x01(\x0e\x32\x16.gooseai.ProjectStatus\x12\x0c\n\x04size\x18\x06 \x01(\x04\x12#\n\x04\x66ile\x18\x07 \x01(\x0b\x32\x15.gooseai.ProjectAsset\x12\x12\n\ncreated_at\x18\x08 \x01(\x04\x12\x12\n\nupdated_at\x18\t \x01(\x04\x12%\n\x06\x61ssets\x18\n \x03(\x0b\x32\x15.gooseai.ProjectAsset\"\xcc\x01\n\x14\x43reateProjectRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x15\n\x08owner_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12&\n\x06\x61\x63\x63\x65ss\x18\x03 \x01(\x0e\x32\x16.gooseai.ProjectAccess\x12&\n\x06status\x18\x04 \x01(\x0e\x32\x16.gooseai.ProjectStatus\x12(\n\x04\x66ile\x18\x05 \x01(\x0b\x32\x15.gooseai.ProjectAssetH\x01\x88\x01\x01\x42\x0b\n\t_owner_idB\x07\n\x05_file\"\x87\x02\n\x14UpdateProjectRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08owner_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05title\x18\x03 \x01(\tH\x01\x88\x01\x01\x12+\n\x06\x61\x63\x63\x65ss\x18\x04 \x01(\x0e\x32\x16.gooseai.ProjectAccessH\x02\x88\x01\x01\x12+\n\x06status\x18\x05 \x01(\x0e\x32\x16.gooseai.ProjectStatusH\x03\x88\x01\x01\x12(\n\x04\x66ile\x18\x06 \x01(\x0b\x32\x15.gooseai.ProjectAssetH\x04\x88\x01\x01\x42\x0b\n\t_owner_idB\x08\n\x06_titleB\t\n\x07_accessB\t\n\x07_statusB\x07\n\x05_file\"8\n\x12ListProjectRequest\x12\x15\n\x08owner_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_owner_id\"C\n\x11GetProjectRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08owner_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_owner_id\"F\n\x14\x44\x65leteProjectRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08owner_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_owner_id\"\x96\x02\n\x12QueryAssetsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08owner_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05since\x18\x03 \x01(\x04H\x01\x88\x01\x01\x12\x12\n\x05until\x18\x04 \x01(\x04H\x02\x88\x01\x01\x12\x12\n\x05limit\x18\x05 \x01(\x04H\x03\x88\x01\x01\x12\x16\n\tstart_key\x18\x06 \x01(\tH\x04\x88\x01\x01\x12%\n\x03use\x18\x07 \x03(\x0e\x32\x18.gooseai.ProjectAssetUse\x12)\n\x08sort_dir\x18\x08 \x01(\x0e\x32\x17.gooseai.ProjectSortDirB\x0b\n\t_owner_idB\x08\n\x06_sinceB\x08\n\x06_untilB\x08\n\x06_limitB\x0c\n\n_start_key\"\x9d\x01\n\x13UpdateAssetsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08owner_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12%\n\x06\x61ssets\x18\x03 \x03(\x0b\x32\x15.gooseai.ProjectAsset\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x0b\n\t_owner_id\"G\n\x14UpdateAssetsResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08owner_id\x18\x02 \x01(\t\x12\x11\n\tasset_ids\x18\x03 \x03(\t\"`\n\x13QueryAssetsResponse\x12%\n\x06\x61ssets\x18\x01 \x03(\x0b\x32\x15.gooseai.ProjectAsset\x12\x15\n\x08last_key\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_last_key\"X\n\x13\x44\x65leteAssetsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08owner_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x11\n\tasset_ids\x18\x03 \x03(\tB\x0b\n\t_owner_id\"G\n\x14\x44\x65leteAssetsResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08owner_id\x18\x02 \x01(\t\x12\x11\n\tasset_ids\x18\x03 \x03(\t*F\n\rProjectAccess\x12\x1a\n\x16PROJECT_ACCESS_PRIVATE\x10\x00\x12\x19\n\x15PROJECT_ACCESS_PUBLIC\x10\x01*c\n\rProjectStatus\x12\x1b\n\x17PROJECT_STATUS_INACTIVE\x10\x00\x12\x19\n\x15PROJECT_STATUS_ACTIVE\x10\x01\x12\x1a\n\x16PROJECT_STATUS_DELETED\x10\x02*\xb0\x01\n\x0fProjectAssetUse\x12\x1f\n\x1bPROJECT_ASSET_USE_UNDEFINED\x10\x00\x12\x1b\n\x17PROJECT_ASSET_USE_INPUT\x10\x01\x12\x1c\n\x18PROJECT_ASSET_USE_OUTPUT\x10\x02\x12\"\n\x1ePROJECT_ASSET_USE_INTERMEDIATE\x10\x03\x12\x1d\n\x19PROJECT_ASSET_USE_PROJECT\x10\x04*g\n\x0eProjectSortDir\x12 \n\x1cPROJECT_SORT_DIR_UNSPECIFIED\x10\x00\x12\x18\n\x14PROJECT_SORT_DIR_ASC\x10\x01\x12\x19\n\x15PROJECT_SORT_DIR_DESC\x10\x02\x32\xa3\x04\n\x0eProjectService\x12;\n\x06\x43reate\x12\x1d.gooseai.CreateProjectRequest\x1a\x10.gooseai.Project\"\x00\x12;\n\x06Update\x12\x1d.gooseai.UpdateProjectRequest\x1a\x10.gooseai.Project\"\x00\x12\x39\n\x04List\x12\x1b.gooseai.ListProjectRequest\x1a\x10.gooseai.Project\"\x00\x30\x01\x12\x35\n\x03Get\x12\x1a.gooseai.GetProjectRequest\x1a\x10.gooseai.Project\"\x00\x12;\n\x06\x44\x65lete\x12\x1d.gooseai.DeleteProjectRequest\x1a\x10.gooseai.Project\"\x00\x12M\n\x0cUpdateAssets\x12\x1c.gooseai.UpdateAssetsRequest\x1a\x1d.gooseai.UpdateAssetsResponse\"\x00\x12J\n\x0bQueryAssets\x12\x1b.gooseai.QueryAssetsRequest\x1a\x1c.gooseai.QueryAssetsResponse\"\x00\x12M\n\x0c\x44\x65leteAssets\x12\x1c.gooseai.DeleteAssetsRequest\x1a\x1d.gooseai.DeleteAssetsResponse\"\x00\x42\x38Z6github.com/stability-ai/api-interfaces/gooseai/projectb\x06proto3')

_PROJECTACCESS = DESCRIPTOR.enum_types_by_name['ProjectAccess']
ProjectAccess = enum_type_wrapper.EnumTypeWrapper(_PROJECTACCESS)
_PROJECTSTATUS = DESCRIPTOR.enum_types_by_name['ProjectStatus']
ProjectStatus = enum_type_wrapper.EnumTypeWrapper(_PROJECTSTATUS)
_PROJECTASSETUSE = DESCRIPTOR.enum_types_by_name['ProjectAssetUse']
ProjectAssetUse = enum_type_wrapper.EnumTypeWrapper(_PROJECTASSETUSE)
_PROJECTSORTDIR = DESCRIPTOR.enum_types_by_name['ProjectSortDir']
ProjectSortDir = enum_type_wrapper.EnumTypeWrapper(_PROJECTSORTDIR)
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
PROJECT_SORT_DIR_UNSPECIFIED = 0
PROJECT_SORT_DIR_ASC = 1
PROJECT_SORT_DIR_DESC = 2


_PROJECTASSET = DESCRIPTOR.message_types_by_name['ProjectAsset']
_PROJECT = DESCRIPTOR.message_types_by_name['Project']
_CREATEPROJECTREQUEST = DESCRIPTOR.message_types_by_name['CreateProjectRequest']
_UPDATEPROJECTREQUEST = DESCRIPTOR.message_types_by_name['UpdateProjectRequest']
_LISTPROJECTREQUEST = DESCRIPTOR.message_types_by_name['ListProjectRequest']
_GETPROJECTREQUEST = DESCRIPTOR.message_types_by_name['GetProjectRequest']
_DELETEPROJECTREQUEST = DESCRIPTOR.message_types_by_name['DeleteProjectRequest']
_QUERYASSETSREQUEST = DESCRIPTOR.message_types_by_name['QueryAssetsRequest']
_UPDATEASSETSREQUEST = DESCRIPTOR.message_types_by_name['UpdateAssetsRequest']
_UPDATEASSETSRESPONSE = DESCRIPTOR.message_types_by_name['UpdateAssetsResponse']
_QUERYASSETSRESPONSE = DESCRIPTOR.message_types_by_name['QueryAssetsResponse']
_DELETEASSETSREQUEST = DESCRIPTOR.message_types_by_name['DeleteAssetsRequest']
_DELETEASSETSRESPONSE = DESCRIPTOR.message_types_by_name['DeleteAssetsResponse']
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

QueryAssetsRequest = _reflection.GeneratedProtocolMessageType('QueryAssetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYASSETSREQUEST,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.QueryAssetsRequest)
  })
_sym_db.RegisterMessage(QueryAssetsRequest)

UpdateAssetsRequest = _reflection.GeneratedProtocolMessageType('UpdateAssetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEASSETSREQUEST,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.UpdateAssetsRequest)
  })
_sym_db.RegisterMessage(UpdateAssetsRequest)

UpdateAssetsResponse = _reflection.GeneratedProtocolMessageType('UpdateAssetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEASSETSRESPONSE,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.UpdateAssetsResponse)
  })
_sym_db.RegisterMessage(UpdateAssetsResponse)

QueryAssetsResponse = _reflection.GeneratedProtocolMessageType('QueryAssetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYASSETSRESPONSE,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.QueryAssetsResponse)
  })
_sym_db.RegisterMessage(QueryAssetsResponse)

DeleteAssetsRequest = _reflection.GeneratedProtocolMessageType('DeleteAssetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEASSETSREQUEST,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.DeleteAssetsRequest)
  })
_sym_db.RegisterMessage(DeleteAssetsRequest)

DeleteAssetsResponse = _reflection.GeneratedProtocolMessageType('DeleteAssetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEASSETSRESPONSE,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.DeleteAssetsResponse)
  })
_sym_db.RegisterMessage(DeleteAssetsResponse)

_PROJECTSERVICE = DESCRIPTOR.services_by_name['ProjectService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6github.com/stability-ai/api-interfaces/gooseai/project'
  _PROJECTACCESS._serialized_start=2059
  _PROJECTACCESS._serialized_end=2129
  _PROJECTSTATUS._serialized_start=2131
  _PROJECTSTATUS._serialized_end=2230
  _PROJECTASSETUSE._serialized_start=2233
  _PROJECTASSETUSE._serialized_end=2409
  _PROJECTSORTDIR._serialized_start=2411
  _PROJECTSORTDIR._serialized_end=2514
  _PROJECTASSET._serialized_start=109
  _PROJECTASSET._serialized_end=343
  _PROJECT._serialized_start=346
  _PROJECT._serialized_end=610
  _CREATEPROJECTREQUEST._serialized_start=613
  _CREATEPROJECTREQUEST._serialized_end=817
  _UPDATEPROJECTREQUEST._serialized_start=820
  _UPDATEPROJECTREQUEST._serialized_end=1083
  _LISTPROJECTREQUEST._serialized_start=1085
  _LISTPROJECTREQUEST._serialized_end=1141
  _GETPROJECTREQUEST._serialized_start=1143
  _GETPROJECTREQUEST._serialized_end=1210
  _DELETEPROJECTREQUEST._serialized_start=1212
  _DELETEPROJECTREQUEST._serialized_end=1282
  _QUERYASSETSREQUEST._serialized_start=1285
  _QUERYASSETSREQUEST._serialized_end=1563
  _UPDATEASSETSREQUEST._serialized_start=1566
  _UPDATEASSETSREQUEST._serialized_end=1723
  _UPDATEASSETSRESPONSE._serialized_start=1725
  _UPDATEASSETSRESPONSE._serialized_end=1796
  _QUERYASSETSRESPONSE._serialized_start=1798
  _QUERYASSETSRESPONSE._serialized_end=1894
  _DELETEASSETSREQUEST._serialized_start=1896
  _DELETEASSETSREQUEST._serialized_end=1984
  _DELETEASSETSRESPONSE._serialized_start=1986
  _DELETEASSETSRESPONSE._serialized_end=2057
  _PROJECTSERVICE._serialized_start=2517
  _PROJECTSERVICE._serialized_end=3064
# @@protoc_insertion_point(module_scope)

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.26.0
// 	protoc        v3.19.5
// source: finetuning.proto

package finetuning

import (
	dashboard "github.com/stability-ai/api-interfaces/gooseai/dashboard"
	_ "github.com/stability-ai/api-interfaces/gooseai/project"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type FineTuningMode int32

const (
	FineTuningMode_NONE   FineTuningMode = 0
	FineTuningMode_FACE   FineTuningMode = 1
	FineTuningMode_STYLE  FineTuningMode = 2
	FineTuningMode_OBJECT FineTuningMode = 3
)

// Enum value maps for FineTuningMode.
var (
	FineTuningMode_name = map[int32]string{
		0: "NONE",
		1: "FACE",
		2: "STYLE",
		3: "OBJECT",
	}
	FineTuningMode_value = map[string]int32{
		"NONE":   0,
		"FACE":   1,
		"STYLE":  2,
		"OBJECT": 3,
	}
)

func (x FineTuningMode) Enum() *FineTuningMode {
	p := new(FineTuningMode)
	*p = x
	return p
}

func (x FineTuningMode) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (FineTuningMode) Descriptor() protoreflect.EnumDescriptor {
	return file_finetuning_proto_enumTypes[0].Descriptor()
}

func (FineTuningMode) Type() protoreflect.EnumType {
	return &file_finetuning_proto_enumTypes[0]
}

func (x FineTuningMode) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use FineTuningMode.Descriptor instead.
func (FineTuningMode) EnumDescriptor() ([]byte, []int) {
	return file_finetuning_proto_rawDescGZIP(), []int{0}
}

type FineTuningJob struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id            string          `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`                                              // uuid unique identifier
	User          *dashboard.User `protobuf:"bytes,2,opt,name=user,proto3" json:"user,omitempty"`                                          // user who created the job
	ModelName     string          `protobuf:"bytes,3,opt,name=model_name,json=modelName,proto3" json:"model_name,omitempty"`               // a readable model name
	Mode          *FineTuningMode `protobuf:"varint,4,opt,name=mode,proto3,enum=gooseai.FineTuningMode,oneof" json:"mode,omitempty"`       // the mode of the job
	ObjectName    *string         `protobuf:"bytes,5,opt,name=object_name,json=objectName,proto3,oneof" json:"object_name,omitempty"`      // freeform text description of object
	ProjectId     string          `protobuf:"bytes,6,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`               // the list of assets to be used for fine tuning
	JobOutputPath string          `protobuf:"bytes,7,opt,name=job_output_path,json=jobOutputPath,proto3" json:"job_output_path,omitempty"` // the path to the output of the job
}

func (x *FineTuningJob) Reset() {
	*x = FineTuningJob{}
	if protoimpl.UnsafeEnabled {
		mi := &file_finetuning_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FineTuningJob) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FineTuningJob) ProtoMessage() {}

func (x *FineTuningJob) ProtoReflect() protoreflect.Message {
	mi := &file_finetuning_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FineTuningJob.ProtoReflect.Descriptor instead.
func (*FineTuningJob) Descriptor() ([]byte, []int) {
	return file_finetuning_proto_rawDescGZIP(), []int{0}
}

func (x *FineTuningJob) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *FineTuningJob) GetUser() *dashboard.User {
	if x != nil {
		return x.User
	}
	return nil
}

func (x *FineTuningJob) GetModelName() string {
	if x != nil {
		return x.ModelName
	}
	return ""
}

func (x *FineTuningJob) GetMode() FineTuningMode {
	if x != nil && x.Mode != nil {
		return *x.Mode
	}
	return FineTuningMode_NONE
}

func (x *FineTuningJob) GetObjectName() string {
	if x != nil && x.ObjectName != nil {
		return *x.ObjectName
	}
	return ""
}

func (x *FineTuningJob) GetProjectId() string {
	if x != nil {
		return x.ProjectId
	}
	return ""
}

func (x *FineTuningJob) GetJobOutputPath() string {
	if x != nil {
		return x.JobOutputPath
	}
	return ""
}

type CreateFineTuningJobRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ModelName  string          `protobuf:"bytes,1,opt,name=model_name,json=modelName,proto3" json:"model_name,omitempty"`          // a readable model name
	Mode       *FineTuningMode `protobuf:"varint,2,opt,name=mode,proto3,enum=gooseai.FineTuningMode,oneof" json:"mode,omitempty"`  // the mode of the job
	ObjectName *string         `protobuf:"bytes,3,opt,name=object_name,json=objectName,proto3,oneof" json:"object_name,omitempty"` // freeform text description of object
	ProjectId  string          `protobuf:"bytes,4,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`          // the list of assets to be used for fine tuning, grouped by project_id
}

func (x *CreateFineTuningJobRequest) Reset() {
	*x = CreateFineTuningJobRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_finetuning_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *CreateFineTuningJobRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreateFineTuningJobRequest) ProtoMessage() {}

func (x *CreateFineTuningJobRequest) ProtoReflect() protoreflect.Message {
	mi := &file_finetuning_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreateFineTuningJobRequest.ProtoReflect.Descriptor instead.
func (*CreateFineTuningJobRequest) Descriptor() ([]byte, []int) {
	return file_finetuning_proto_rawDescGZIP(), []int{1}
}

func (x *CreateFineTuningJobRequest) GetModelName() string {
	if x != nil {
		return x.ModelName
	}
	return ""
}

func (x *CreateFineTuningJobRequest) GetMode() FineTuningMode {
	if x != nil && x.Mode != nil {
		return *x.Mode
	}
	return FineTuningMode_NONE
}

func (x *CreateFineTuningJobRequest) GetObjectName() string {
	if x != nil && x.ObjectName != nil {
		return *x.ObjectName
	}
	return ""
}

func (x *CreateFineTuningJobRequest) GetProjectId() string {
	if x != nil {
		return x.ProjectId
	}
	return ""
}

type UpdateFineTuningJobRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id         string          `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	ModelName  string          `protobuf:"bytes,2,opt,name=model_name,json=modelName,proto3" json:"model_name,omitempty"`          // a readable model name
	Mode       *FineTuningMode `protobuf:"varint,3,opt,name=mode,proto3,enum=gooseai.FineTuningMode,oneof" json:"mode,omitempty"`  // the mode of the job
	ObjectName *string         `protobuf:"bytes,4,opt,name=object_name,json=objectName,proto3,oneof" json:"object_name,omitempty"` // freeform text description of object
	ProjectId  string          `protobuf:"bytes,5,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`          // the list of assets to be used for fine tuning, grouped by project_id
}

func (x *UpdateFineTuningJobRequest) Reset() {
	*x = UpdateFineTuningJobRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_finetuning_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *UpdateFineTuningJobRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdateFineTuningJobRequest) ProtoMessage() {}

func (x *UpdateFineTuningJobRequest) ProtoReflect() protoreflect.Message {
	mi := &file_finetuning_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdateFineTuningJobRequest.ProtoReflect.Descriptor instead.
func (*UpdateFineTuningJobRequest) Descriptor() ([]byte, []int) {
	return file_finetuning_proto_rawDescGZIP(), []int{2}
}

func (x *UpdateFineTuningJobRequest) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *UpdateFineTuningJobRequest) GetModelName() string {
	if x != nil {
		return x.ModelName
	}
	return ""
}

func (x *UpdateFineTuningJobRequest) GetMode() FineTuningMode {
	if x != nil && x.Mode != nil {
		return *x.Mode
	}
	return FineTuningMode_NONE
}

func (x *UpdateFineTuningJobRequest) GetObjectName() string {
	if x != nil && x.ObjectName != nil {
		return *x.ObjectName
	}
	return ""
}

func (x *UpdateFineTuningJobRequest) GetProjectId() string {
	if x != nil {
		return x.ProjectId
	}
	return ""
}

type FineTuningJobRequestById struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id string `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"` // the id of the job
}

func (x *FineTuningJobRequestById) Reset() {
	*x = FineTuningJobRequestById{}
	if protoimpl.UnsafeEnabled {
		mi := &file_finetuning_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FineTuningJobRequestById) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FineTuningJobRequestById) ProtoMessage() {}

func (x *FineTuningJobRequestById) ProtoReflect() protoreflect.Message {
	mi := &file_finetuning_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FineTuningJobRequestById.ProtoReflect.Descriptor instead.
func (*FineTuningJobRequestById) Descriptor() ([]byte, []int) {
	return file_finetuning_proto_rawDescGZIP(), []int{3}
}

func (x *FineTuningJobRequestById) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

type FineTuningJobProgress struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id       string `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`              // the id of the job that was checked
	Progress int32  `protobuf:"varint,2,opt,name=progress,proto3" json:"progress,omitempty"` // the percentage of progress
}

func (x *FineTuningJobProgress) Reset() {
	*x = FineTuningJobProgress{}
	if protoimpl.UnsafeEnabled {
		mi := &file_finetuning_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FineTuningJobProgress) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FineTuningJobProgress) ProtoMessage() {}

func (x *FineTuningJobProgress) ProtoReflect() protoreflect.Message {
	mi := &file_finetuning_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FineTuningJobProgress.ProtoReflect.Descriptor instead.
func (*FineTuningJobProgress) Descriptor() ([]byte, []int) {
	return file_finetuning_proto_rawDescGZIP(), []int{4}
}

func (x *FineTuningJobProgress) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *FineTuningJobProgress) GetProgress() int32 {
	if x != nil {
		return x.Progress
	}
	return 0
}

var File_finetuning_proto protoreflect.FileDescriptor

var file_finetuning_proto_rawDesc = []byte{
	0x0a, 0x10, 0x66, 0x69, 0x6e, 0x65, 0x74, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x12, 0x07, 0x67, 0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69, 0x1a, 0x0d, 0x70, 0x72, 0x6f,
	0x6a, 0x65, 0x63, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x0f, 0x64, 0x61, 0x73, 0x68,
	0x62, 0x6f, 0x61, 0x72, 0x64, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x99, 0x02, 0x0a, 0x0d,
	0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a, 0x6f, 0x62, 0x12, 0x0e, 0x0a,
	0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x02, 0x69, 0x64, 0x12, 0x21, 0x0a,
	0x04, 0x75, 0x73, 0x65, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x0d, 0x2e, 0x67, 0x6f,
	0x6f, 0x73, 0x65, 0x61, 0x69, 0x2e, 0x55, 0x73, 0x65, 0x72, 0x52, 0x04, 0x75, 0x73, 0x65, 0x72,
	0x12, 0x1d, 0x0a, 0x0a, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x03,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x4e, 0x61, 0x6d, 0x65, 0x12,
	0x30, 0x0a, 0x04, 0x6d, 0x6f, 0x64, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x17, 0x2e,
	0x67, 0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69, 0x2e, 0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69,
	0x6e, 0x67, 0x4d, 0x6f, 0x64, 0x65, 0x48, 0x00, 0x52, 0x04, 0x6d, 0x6f, 0x64, 0x65, 0x88, 0x01,
	0x01, 0x12, 0x24, 0x0a, 0x0b, 0x6f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x5f, 0x6e, 0x61, 0x6d, 0x65,
	0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x48, 0x01, 0x52, 0x0a, 0x6f, 0x62, 0x6a, 0x65, 0x63, 0x74,
	0x4e, 0x61, 0x6d, 0x65, 0x88, 0x01, 0x01, 0x12, 0x1d, 0x0a, 0x0a, 0x70, 0x72, 0x6f, 0x6a, 0x65,
	0x63, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x70, 0x72, 0x6f,
	0x6a, 0x65, 0x63, 0x74, 0x49, 0x64, 0x12, 0x26, 0x0a, 0x0f, 0x6a, 0x6f, 0x62, 0x5f, 0x6f, 0x75,
	0x74, 0x70, 0x75, 0x74, 0x5f, 0x70, 0x61, 0x74, 0x68, 0x18, 0x07, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x0d, 0x6a, 0x6f, 0x62, 0x4f, 0x75, 0x74, 0x70, 0x75, 0x74, 0x50, 0x61, 0x74, 0x68, 0x42, 0x07,
	0x0a, 0x05, 0x5f, 0x6d, 0x6f, 0x64, 0x65, 0x42, 0x0e, 0x0a, 0x0c, 0x5f, 0x6f, 0x62, 0x6a, 0x65,
	0x63, 0x74, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x22, 0xcb, 0x01, 0x0a, 0x1a, 0x43, 0x72, 0x65, 0x61,
	0x74, 0x65, 0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a, 0x6f, 0x62, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x1d, 0x0a, 0x0a, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x5f,
	0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x6d, 0x6f, 0x64, 0x65,
	0x6c, 0x4e, 0x61, 0x6d, 0x65, 0x12, 0x30, 0x0a, 0x04, 0x6d, 0x6f, 0x64, 0x65, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x0e, 0x32, 0x17, 0x2e, 0x67, 0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69, 0x2e, 0x46, 0x69,
	0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4d, 0x6f, 0x64, 0x65, 0x48, 0x00, 0x52, 0x04,
	0x6d, 0x6f, 0x64, 0x65, 0x88, 0x01, 0x01, 0x12, 0x24, 0x0a, 0x0b, 0x6f, 0x62, 0x6a, 0x65, 0x63,
	0x74, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x48, 0x01, 0x52, 0x0a,
	0x6f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x4e, 0x61, 0x6d, 0x65, 0x88, 0x01, 0x01, 0x12, 0x1d, 0x0a,
	0x0a, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x04, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x09, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x49, 0x64, 0x42, 0x07, 0x0a, 0x05,
	0x5f, 0x6d, 0x6f, 0x64, 0x65, 0x42, 0x0e, 0x0a, 0x0c, 0x5f, 0x6f, 0x62, 0x6a, 0x65, 0x63, 0x74,
	0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x22, 0xdb, 0x01, 0x0a, 0x1a, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65,
	0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a, 0x6f, 0x62, 0x52, 0x65, 0x71,
	0x75, 0x65, 0x73, 0x74, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x02, 0x69, 0x64, 0x12, 0x1d, 0x0a, 0x0a, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x5f, 0x6e, 0x61,
	0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x4e,
	0x61, 0x6d, 0x65, 0x12, 0x30, 0x0a, 0x04, 0x6d, 0x6f, 0x64, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28,
	0x0e, 0x32, 0x17, 0x2e, 0x67, 0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69, 0x2e, 0x46, 0x69, 0x6e, 0x65,
	0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4d, 0x6f, 0x64, 0x65, 0x48, 0x00, 0x52, 0x04, 0x6d, 0x6f,
	0x64, 0x65, 0x88, 0x01, 0x01, 0x12, 0x24, 0x0a, 0x0b, 0x6f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x5f,
	0x6e, 0x61, 0x6d, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x48, 0x01, 0x52, 0x0a, 0x6f, 0x62,
	0x6a, 0x65, 0x63, 0x74, 0x4e, 0x61, 0x6d, 0x65, 0x88, 0x01, 0x01, 0x12, 0x1d, 0x0a, 0x0a, 0x70,
	0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x09, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x49, 0x64, 0x42, 0x07, 0x0a, 0x05, 0x5f, 0x6d,
	0x6f, 0x64, 0x65, 0x42, 0x0e, 0x0a, 0x0c, 0x5f, 0x6f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x5f, 0x6e,
	0x61, 0x6d, 0x65, 0x22, 0x2a, 0x0a, 0x18, 0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e,
	0x67, 0x4a, 0x6f, 0x62, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x42, 0x79, 0x49, 0x64, 0x12,
	0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x02, 0x69, 0x64, 0x22,
	0x43, 0x0a, 0x15, 0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a, 0x6f, 0x62,
	0x50, 0x72, 0x6f, 0x67, 0x72, 0x65, 0x73, 0x73, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x02, 0x69, 0x64, 0x12, 0x1a, 0x0a, 0x08, 0x70, 0x72, 0x6f, 0x67,
	0x72, 0x65, 0x73, 0x73, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x08, 0x70, 0x72, 0x6f, 0x67,
	0x72, 0x65, 0x73, 0x73, 0x2a, 0x3b, 0x0a, 0x0e, 0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69,
	0x6e, 0x67, 0x4d, 0x6f, 0x64, 0x65, 0x12, 0x08, 0x0a, 0x04, 0x4e, 0x4f, 0x4e, 0x45, 0x10, 0x00,
	0x12, 0x08, 0x0a, 0x04, 0x46, 0x41, 0x43, 0x45, 0x10, 0x01, 0x12, 0x09, 0x0a, 0x05, 0x53, 0x54,
	0x59, 0x4c, 0x45, 0x10, 0x02, 0x12, 0x0a, 0x0a, 0x06, 0x4f, 0x42, 0x4a, 0x45, 0x43, 0x54, 0x10,
	0x03, 0x32, 0xbf, 0x03, 0x0a, 0x11, 0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67,
	0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x52, 0x0a, 0x13, 0x43, 0x72, 0x65, 0x61, 0x74,
	0x65, 0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a, 0x6f, 0x62, 0x12, 0x23,
	0x2e, 0x67, 0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x46,
	0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a, 0x6f, 0x62, 0x52, 0x65, 0x71, 0x75,
	0x65, 0x73, 0x74, 0x1a, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69, 0x2e, 0x46, 0x69,
	0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a, 0x6f, 0x62, 0x12, 0x51, 0x0a, 0x14, 0x47,
	0x65, 0x74, 0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a, 0x6f, 0x62, 0x42,
	0x79, 0x49, 0x64, 0x12, 0x21, 0x2e, 0x67, 0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69, 0x2e, 0x46, 0x69,
	0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a, 0x6f, 0x62, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x42, 0x79, 0x49, 0x64, 0x1a, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69,
	0x2e, 0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a, 0x6f, 0x62, 0x12, 0x52,
	0x0a, 0x13, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69,
	0x6e, 0x67, 0x4a, 0x6f, 0x62, 0x12, 0x23, 0x2e, 0x67, 0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69, 0x2e,
	0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67,
	0x4a, 0x6f, 0x62, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x16, 0x2e, 0x67, 0x6f, 0x6f,
	0x73, 0x65, 0x61, 0x69, 0x2e, 0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a,
	0x6f, 0x62, 0x12, 0x50, 0x0a, 0x13, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x46, 0x69, 0x6e, 0x65,
	0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a, 0x6f, 0x62, 0x12, 0x21, 0x2e, 0x67, 0x6f, 0x6f, 0x73,
	0x65, 0x61, 0x69, 0x2e, 0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a, 0x6f,
	0x62, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x42, 0x79, 0x49, 0x64, 0x1a, 0x16, 0x2e, 0x67,
	0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69, 0x2e, 0x46, 0x69, 0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e,
	0x67, 0x4a, 0x6f, 0x62, 0x12, 0x5d, 0x0a, 0x18, 0x47, 0x65, 0x74, 0x46, 0x69, 0x6e, 0x65, 0x54,
	0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a, 0x6f, 0x62, 0x50, 0x72, 0x6f, 0x67, 0x72, 0x65, 0x73, 0x73,
	0x12, 0x21, 0x2e, 0x67, 0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69, 0x2e, 0x46, 0x69, 0x6e, 0x65, 0x54,
	0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a, 0x6f, 0x62, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x42,
	0x79, 0x49, 0x64, 0x1a, 0x1e, 0x2e, 0x67, 0x6f, 0x6f, 0x73, 0x65, 0x61, 0x69, 0x2e, 0x46, 0x69,
	0x6e, 0x65, 0x54, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4a, 0x6f, 0x62, 0x50, 0x72, 0x6f, 0x67, 0x72,
	0x65, 0x73, 0x73, 0x42, 0x3b, 0x5a, 0x39, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f,
	0x6d, 0x2f, 0x73, 0x74, 0x61, 0x62, 0x69, 0x6c, 0x69, 0x74, 0x79, 0x2d, 0x61, 0x69, 0x2f, 0x61,
	0x70, 0x69, 0x2d, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x73, 0x2f, 0x67, 0x6f,
	0x6f, 0x73, 0x65, 0x61, 0x69, 0x2f, 0x66, 0x69, 0x6e, 0x65, 0x74, 0x75, 0x6e, 0x69, 0x6e, 0x67,
	0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_finetuning_proto_rawDescOnce sync.Once
	file_finetuning_proto_rawDescData = file_finetuning_proto_rawDesc
)

func file_finetuning_proto_rawDescGZIP() []byte {
	file_finetuning_proto_rawDescOnce.Do(func() {
		file_finetuning_proto_rawDescData = protoimpl.X.CompressGZIP(file_finetuning_proto_rawDescData)
	})
	return file_finetuning_proto_rawDescData
}

var file_finetuning_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_finetuning_proto_msgTypes = make([]protoimpl.MessageInfo, 5)
var file_finetuning_proto_goTypes = []interface{}{
	(FineTuningMode)(0),                // 0: gooseai.FineTuningMode
	(*FineTuningJob)(nil),              // 1: gooseai.FineTuningJob
	(*CreateFineTuningJobRequest)(nil), // 2: gooseai.CreateFineTuningJobRequest
	(*UpdateFineTuningJobRequest)(nil), // 3: gooseai.UpdateFineTuningJobRequest
	(*FineTuningJobRequestById)(nil),   // 4: gooseai.FineTuningJobRequestById
	(*FineTuningJobProgress)(nil),      // 5: gooseai.FineTuningJobProgress
	(*dashboard.User)(nil),             // 6: gooseai.User
}
var file_finetuning_proto_depIdxs = []int32{
	6, // 0: gooseai.FineTuningJob.user:type_name -> gooseai.User
	0, // 1: gooseai.FineTuningJob.mode:type_name -> gooseai.FineTuningMode
	0, // 2: gooseai.CreateFineTuningJobRequest.mode:type_name -> gooseai.FineTuningMode
	0, // 3: gooseai.UpdateFineTuningJobRequest.mode:type_name -> gooseai.FineTuningMode
	2, // 4: gooseai.FineTuningService.CreateFineTuningJob:input_type -> gooseai.CreateFineTuningJobRequest
	4, // 5: gooseai.FineTuningService.GetFineTuningJobById:input_type -> gooseai.FineTuningJobRequestById
	3, // 6: gooseai.FineTuningService.UpdateFineTuningJob:input_type -> gooseai.UpdateFineTuningJobRequest
	4, // 7: gooseai.FineTuningService.DeleteFineTuningJob:input_type -> gooseai.FineTuningJobRequestById
	4, // 8: gooseai.FineTuningService.GetFineTuningJobProgress:input_type -> gooseai.FineTuningJobRequestById
	1, // 9: gooseai.FineTuningService.CreateFineTuningJob:output_type -> gooseai.FineTuningJob
	1, // 10: gooseai.FineTuningService.GetFineTuningJobById:output_type -> gooseai.FineTuningJob
	1, // 11: gooseai.FineTuningService.UpdateFineTuningJob:output_type -> gooseai.FineTuningJob
	1, // 12: gooseai.FineTuningService.DeleteFineTuningJob:output_type -> gooseai.FineTuningJob
	5, // 13: gooseai.FineTuningService.GetFineTuningJobProgress:output_type -> gooseai.FineTuningJobProgress
	9, // [9:14] is the sub-list for method output_type
	4, // [4:9] is the sub-list for method input_type
	4, // [4:4] is the sub-list for extension type_name
	4, // [4:4] is the sub-list for extension extendee
	0, // [0:4] is the sub-list for field type_name
}

func init() { file_finetuning_proto_init() }
func file_finetuning_proto_init() {
	if File_finetuning_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_finetuning_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FineTuningJob); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_finetuning_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*CreateFineTuningJobRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_finetuning_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*UpdateFineTuningJobRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_finetuning_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FineTuningJobRequestById); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_finetuning_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FineTuningJobProgress); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	file_finetuning_proto_msgTypes[0].OneofWrappers = []interface{}{}
	file_finetuning_proto_msgTypes[1].OneofWrappers = []interface{}{}
	file_finetuning_proto_msgTypes[2].OneofWrappers = []interface{}{}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_finetuning_proto_rawDesc,
			NumEnums:      1,
			NumMessages:   5,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_finetuning_proto_goTypes,
		DependencyIndexes: file_finetuning_proto_depIdxs,
		EnumInfos:         file_finetuning_proto_enumTypes,
		MessageInfos:      file_finetuning_proto_msgTypes,
	}.Build()
	File_finetuning_proto = out.File
	file_finetuning_proto_rawDesc = nil
	file_finetuning_proto_goTypes = nil
	file_finetuning_proto_depIdxs = nil
}

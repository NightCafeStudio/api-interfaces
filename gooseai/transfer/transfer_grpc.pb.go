// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package transfer

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// TransferServiceClient is the client API for TransferService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type TransferServiceClient interface {
	Transfer(ctx context.Context, in *TransferRequest, opts ...grpc.CallOption) (*TransferResponse, error)
}

type transferServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewTransferServiceClient(cc grpc.ClientConnInterface) TransferServiceClient {
	return &transferServiceClient{cc}
}

func (c *transferServiceClient) Transfer(ctx context.Context, in *TransferRequest, opts ...grpc.CallOption) (*TransferResponse, error) {
	out := new(TransferResponse)
	err := c.cc.Invoke(ctx, "/gooseai.TransferService/Transfer", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// TransferServiceServer is the server API for TransferService service.
// All implementations must embed UnimplementedTransferServiceServer
// for forward compatibility
type TransferServiceServer interface {
	Transfer(context.Context, *TransferRequest) (*TransferResponse, error)
	mustEmbedUnimplementedTransferServiceServer()
}

// UnimplementedTransferServiceServer must be embedded to have forward compatible implementations.
type UnimplementedTransferServiceServer struct {
}

func (UnimplementedTransferServiceServer) Transfer(context.Context, *TransferRequest) (*TransferResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Transfer not implemented")
}
func (UnimplementedTransferServiceServer) mustEmbedUnimplementedTransferServiceServer() {}

// UnsafeTransferServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to TransferServiceServer will
// result in compilation errors.
type UnsafeTransferServiceServer interface {
	mustEmbedUnimplementedTransferServiceServer()
}

func RegisterTransferServiceServer(s grpc.ServiceRegistrar, srv TransferServiceServer) {
	s.RegisterService(&TransferService_ServiceDesc, srv)
}

func _TransferService_Transfer_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(TransferRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransferServiceServer).Transfer(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/gooseai.TransferService/Transfer",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransferServiceServer).Transfer(ctx, req.(*TransferRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// TransferService_ServiceDesc is the grpc.ServiceDesc for TransferService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var TransferService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "gooseai.TransferService",
	HandlerType: (*TransferServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Transfer",
			Handler:    _TransferService_Transfer_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "transfer.proto",
}

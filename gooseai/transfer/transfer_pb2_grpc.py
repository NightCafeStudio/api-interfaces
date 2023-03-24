# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import transfer_pb2 as transfer__pb2


class TransferServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Transfer = channel.unary_unary(
                '/gooseai.TransferService/Transfer',
                request_serializer=transfer__pb2.TransferRequest.SerializeToString,
                response_deserializer=transfer__pb2.TransferResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/gooseai.TransferService/Delete',
                request_serializer=transfer__pb2.DeleteRequest.SerializeToString,
                response_deserializer=transfer__pb2.DeleteResponse.FromString,
                )
        self.CleanupFineTuning = channel.unary_unary(
                '/gooseai.TransferService/CleanupFineTuning',
                request_serializer=transfer__pb2.CleanupFineTuningRequest.SerializeToString,
                response_deserializer=transfer__pb2.CleanupFineTuningResponse.FromString,
                )


class TransferServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Transfer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CleanupFineTuning(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransferServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Transfer': grpc.unary_unary_rpc_method_handler(
                    servicer.Transfer,
                    request_deserializer=transfer__pb2.TransferRequest.FromString,
                    response_serializer=transfer__pb2.TransferResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=transfer__pb2.DeleteRequest.FromString,
                    response_serializer=transfer__pb2.DeleteResponse.SerializeToString,
            ),
            'CleanupFineTuning': grpc.unary_unary_rpc_method_handler(
                    servicer.CleanupFineTuning,
                    request_deserializer=transfer__pb2.CleanupFineTuningRequest.FromString,
                    response_serializer=transfer__pb2.CleanupFineTuningResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gooseai.TransferService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TransferService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Transfer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.TransferService/Transfer',
            transfer__pb2.TransferRequest.SerializeToString,
            transfer__pb2.TransferResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.TransferService/Delete',
            transfer__pb2.DeleteRequest.SerializeToString,
            transfer__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CleanupFineTuning(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.TransferService/CleanupFineTuning',
            transfer__pb2.CleanupFineTuningRequest.SerializeToString,
            transfer__pb2.CleanupFineTuningResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

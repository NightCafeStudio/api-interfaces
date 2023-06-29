# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import finetuning_pb2 as finetuning__pb2


class FineTuningServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateModel = channel.unary_unary(
                '/gooseai.FineTuningService/CreateModel',
                request_serializer=finetuning__pb2.CreateModelRequest.SerializeToString,
                response_deserializer=finetuning__pb2.CreateModelResponse.FromString,
                )
        self.GetModel = channel.unary_unary(
                '/gooseai.FineTuningService/GetModel',
                request_serializer=finetuning__pb2.GetModelRequest.SerializeToString,
                response_deserializer=finetuning__pb2.GetModelResponse.FromString,
                )
        self.UpdateModel = channel.unary_unary(
                '/gooseai.FineTuningService/UpdateModel',
                request_serializer=finetuning__pb2.UpdateModelRequest.SerializeToString,
                response_deserializer=finetuning__pb2.UpdateModelResponse.FromString,
                )
        self.DeleteModel = channel.unary_unary(
                '/gooseai.FineTuningService/DeleteModel',
                request_serializer=finetuning__pb2.DeleteModelRequest.SerializeToString,
                response_deserializer=finetuning__pb2.DeleteModelResponse.FromString,
                )
        self.ResubmitModel = channel.unary_unary(
                '/gooseai.FineTuningService/ResubmitModel',
                request_serializer=finetuning__pb2.ResubmitModelRequest.SerializeToString,
                response_deserializer=finetuning__pb2.ResubmitModelResponse.FromString,
                )
        self.ListModels = channel.unary_unary(
                '/gooseai.FineTuningService/ListModels',
                request_serializer=finetuning__pb2.ListModelsRequest.SerializeToString,
                response_deserializer=finetuning__pb2.ListModelsResponse.FromString,
                )


class FineTuningServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateModel(self, request, context):
        """Create a new model and begin the fine tuning process
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetModel(self, request, context):
        """Get a FineTuningModel
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateModel(self, request, context):
        """Update a FineTuningModel by id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteModel(self, request, context):
        """Delete a fine tuned model
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResubmitModel(self, request, context):
        """Re-run training, does not create a new model
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListModels(self, request, context):
        """List all the fine tuned models for an organization or user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FineTuningServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateModel': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateModel,
                    request_deserializer=finetuning__pb2.CreateModelRequest.FromString,
                    response_serializer=finetuning__pb2.CreateModelResponse.SerializeToString,
            ),
            'GetModel': grpc.unary_unary_rpc_method_handler(
                    servicer.GetModel,
                    request_deserializer=finetuning__pb2.GetModelRequest.FromString,
                    response_serializer=finetuning__pb2.GetModelResponse.SerializeToString,
            ),
            'UpdateModel': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateModel,
                    request_deserializer=finetuning__pb2.UpdateModelRequest.FromString,
                    response_serializer=finetuning__pb2.UpdateModelResponse.SerializeToString,
            ),
            'DeleteModel': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteModel,
                    request_deserializer=finetuning__pb2.DeleteModelRequest.FromString,
                    response_serializer=finetuning__pb2.DeleteModelResponse.SerializeToString,
            ),
            'ResubmitModel': grpc.unary_unary_rpc_method_handler(
                    servicer.ResubmitModel,
                    request_deserializer=finetuning__pb2.ResubmitModelRequest.FromString,
                    response_serializer=finetuning__pb2.ResubmitModelResponse.SerializeToString,
            ),
            'ListModels': grpc.unary_unary_rpc_method_handler(
                    servicer.ListModels,
                    request_deserializer=finetuning__pb2.ListModelsRequest.FromString,
                    response_serializer=finetuning__pb2.ListModelsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gooseai.FineTuningService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FineTuningService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.FineTuningService/CreateModel',
            finetuning__pb2.CreateModelRequest.SerializeToString,
            finetuning__pb2.CreateModelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.FineTuningService/GetModel',
            finetuning__pb2.GetModelRequest.SerializeToString,
            finetuning__pb2.GetModelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.FineTuningService/UpdateModel',
            finetuning__pb2.UpdateModelRequest.SerializeToString,
            finetuning__pb2.UpdateModelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.FineTuningService/DeleteModel',
            finetuning__pb2.DeleteModelRequest.SerializeToString,
            finetuning__pb2.DeleteModelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResubmitModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.FineTuningService/ResubmitModel',
            finetuning__pb2.ResubmitModelRequest.SerializeToString,
            finetuning__pb2.ResubmitModelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListModels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.FineTuningService/ListModels',
            finetuning__pb2.ListModelsRequest.SerializeToString,
            finetuning__pb2.ListModelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

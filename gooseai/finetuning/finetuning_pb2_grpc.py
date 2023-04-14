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
        self.CreateFineTuningJob = channel.unary_unary(
                '/gooseai.FineTuningService/CreateFineTuningJob',
                request_serializer=finetuning__pb2.CreateFineTuningJobRequest.SerializeToString,
                response_deserializer=finetuning__pb2.CreateFineTuningJobResponse.FromString,
                )
        self.GetFineTuningJobById = channel.unary_unary(
                '/gooseai.FineTuningService/GetFineTuningJobById',
                request_serializer=finetuning__pb2.GetFineTuningJobByIdRequest.SerializeToString,
                response_deserializer=finetuning__pb2.GetFineTuningJobByIdResponse.FromString,
                )
        self.UpdateFineTuningJob = channel.unary_unary(
                '/gooseai.FineTuningService/UpdateFineTuningJob',
                request_serializer=finetuning__pb2.UpdateFineTuningJobRequest.SerializeToString,
                response_deserializer=finetuning__pb2.UpdateFineTuningJobResponse.FromString,
                )
        self.DeleteFineTuningJob = channel.unary_unary(
                '/gooseai.FineTuningService/DeleteFineTuningJob',
                request_serializer=finetuning__pb2.DeleteFineTuningJobRequest.SerializeToString,
                response_deserializer=finetuning__pb2.DeleteFineTuningJobResponse.FromString,
                )
        self.GetFineTuningJobStatus = channel.unary_unary(
                '/gooseai.FineTuningService/GetFineTuningJobStatus',
                request_serializer=finetuning__pb2.GetFineTuningJobStatusRequest.SerializeToString,
                response_deserializer=finetuning__pb2.GetFineTuningJobStatusResponse.FromString,
                )
        self.ResubmitFineTuningJob = channel.unary_unary(
                '/gooseai.FineTuningService/ResubmitFineTuningJob',
                request_serializer=finetuning__pb2.ResubmitFineTuningJobRequest.SerializeToString,
                response_deserializer=finetuning__pb2.ResubmitFineTuningJobResponse.FromString,
                )
        self.GetFineTuningJobsByUserId = channel.unary_unary(
                '/gooseai.FineTuningService/GetFineTuningJobsByUserId',
                request_serializer=finetuning__pb2.GetFineTuningJobsByUserIdRequest.SerializeToString,
                response_deserializer=finetuning__pb2.GetFineTuningJobsByUserIdResponse.FromString,
                )
        self.GetFineTuningJobsByOrgId = channel.unary_unary(
                '/gooseai.FineTuningService/GetFineTuningJobsByOrgId',
                request_serializer=finetuning__pb2.GetFineTuningJobsByOrgIdRequest.SerializeToString,
                response_deserializer=finetuning__pb2.GetFineTuningJobsByOrgIdResponse.FromString,
                )


class FineTuningServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateFineTuningJob(self, request, context):
        """Create a new project if it does not exist, and runs it
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFineTuningJobById(self, request, context):
        """Get a FineTuningJob by id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFineTuningJob(self, request, context):
        """Update a FineTuningJob by id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFineTuningJob(self, request, context):
        """Delete a FineTuningJob by id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFineTuningJobStatus(self, request, context):
        """Check the progress of a FineTuningJob by id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResubmitFineTuningJob(self, request, context):
        """Re-run training API call, does not create a new job in the DB
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFineTuningJobsByUserId(self, request, context):
        """Get a list of FineTuningJobs by user id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFineTuningJobsByOrgId(self, request, context):
        """Get a list of FineTuningJobs by org id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FineTuningServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateFineTuningJob': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFineTuningJob,
                    request_deserializer=finetuning__pb2.CreateFineTuningJobRequest.FromString,
                    response_serializer=finetuning__pb2.CreateFineTuningJobResponse.SerializeToString,
            ),
            'GetFineTuningJobById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFineTuningJobById,
                    request_deserializer=finetuning__pb2.GetFineTuningJobByIdRequest.FromString,
                    response_serializer=finetuning__pb2.GetFineTuningJobByIdResponse.SerializeToString,
            ),
            'UpdateFineTuningJob': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateFineTuningJob,
                    request_deserializer=finetuning__pb2.UpdateFineTuningJobRequest.FromString,
                    response_serializer=finetuning__pb2.UpdateFineTuningJobResponse.SerializeToString,
            ),
            'DeleteFineTuningJob': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFineTuningJob,
                    request_deserializer=finetuning__pb2.DeleteFineTuningJobRequest.FromString,
                    response_serializer=finetuning__pb2.DeleteFineTuningJobResponse.SerializeToString,
            ),
            'GetFineTuningJobStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFineTuningJobStatus,
                    request_deserializer=finetuning__pb2.GetFineTuningJobStatusRequest.FromString,
                    response_serializer=finetuning__pb2.GetFineTuningJobStatusResponse.SerializeToString,
            ),
            'ResubmitFineTuningJob': grpc.unary_unary_rpc_method_handler(
                    servicer.ResubmitFineTuningJob,
                    request_deserializer=finetuning__pb2.ResubmitFineTuningJobRequest.FromString,
                    response_serializer=finetuning__pb2.ResubmitFineTuningJobResponse.SerializeToString,
            ),
            'GetFineTuningJobsByUserId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFineTuningJobsByUserId,
                    request_deserializer=finetuning__pb2.GetFineTuningJobsByUserIdRequest.FromString,
                    response_serializer=finetuning__pb2.GetFineTuningJobsByUserIdResponse.SerializeToString,
            ),
            'GetFineTuningJobsByOrgId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFineTuningJobsByOrgId,
                    request_deserializer=finetuning__pb2.GetFineTuningJobsByOrgIdRequest.FromString,
                    response_serializer=finetuning__pb2.GetFineTuningJobsByOrgIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gooseai.FineTuningService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FineTuningService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateFineTuningJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.FineTuningService/CreateFineTuningJob',
            finetuning__pb2.CreateFineTuningJobRequest.SerializeToString,
            finetuning__pb2.CreateFineTuningJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFineTuningJobById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.FineTuningService/GetFineTuningJobById',
            finetuning__pb2.GetFineTuningJobByIdRequest.SerializeToString,
            finetuning__pb2.GetFineTuningJobByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateFineTuningJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.FineTuningService/UpdateFineTuningJob',
            finetuning__pb2.UpdateFineTuningJobRequest.SerializeToString,
            finetuning__pb2.UpdateFineTuningJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteFineTuningJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.FineTuningService/DeleteFineTuningJob',
            finetuning__pb2.DeleteFineTuningJobRequest.SerializeToString,
            finetuning__pb2.DeleteFineTuningJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFineTuningJobStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.FineTuningService/GetFineTuningJobStatus',
            finetuning__pb2.GetFineTuningJobStatusRequest.SerializeToString,
            finetuning__pb2.GetFineTuningJobStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResubmitFineTuningJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.FineTuningService/ResubmitFineTuningJob',
            finetuning__pb2.ResubmitFineTuningJobRequest.SerializeToString,
            finetuning__pb2.ResubmitFineTuningJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFineTuningJobsByUserId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.FineTuningService/GetFineTuningJobsByUserId',
            finetuning__pb2.GetFineTuningJobsByUserIdRequest.SerializeToString,
            finetuning__pb2.GetFineTuningJobsByUserIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFineTuningJobsByOrgId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gooseai.FineTuningService/GetFineTuningJobsByOrgId',
            finetuning__pb2.GetFineTuningJobsByOrgIdRequest.SerializeToString,
            finetuning__pb2.GetFineTuningJobsByOrgIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

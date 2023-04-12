// package: gooseai
// file: finetuning.proto

import * as finetuning_pb from "./finetuning_pb";
import {grpc} from "@improbable-eng/grpc-web";

type FineTuningServiceCreateFineTuningJob = {
  readonly methodName: string;
  readonly service: typeof FineTuningService;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof finetuning_pb.CreateFineTuningJobRequest;
  readonly responseType: typeof finetuning_pb.FineTuningJob;
};

type FineTuningServiceGetFineTuningJobById = {
  readonly methodName: string;
  readonly service: typeof FineTuningService;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof finetuning_pb.FineTuningJobRequestById;
  readonly responseType: typeof finetuning_pb.FineTuningJob;
};

type FineTuningServiceUpdateFineTuningJob = {
  readonly methodName: string;
  readonly service: typeof FineTuningService;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof finetuning_pb.UpdateFineTuningJobRequest;
  readonly responseType: typeof finetuning_pb.FineTuningJob;
};

type FineTuningServiceDeleteFineTuningJob = {
  readonly methodName: string;
  readonly service: typeof FineTuningService;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof finetuning_pb.FineTuningJobRequestById;
  readonly responseType: typeof finetuning_pb.FineTuningJob;
};

type FineTuningServiceGetFineTuningJobStatus = {
  readonly methodName: string;
  readonly service: typeof FineTuningService;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof finetuning_pb.FineTuningJobRequestById;
  readonly responseType: typeof finetuning_pb.FineTuningJobStatus;
};

type FineTuningServiceResubmitFineTuningJob = {
  readonly methodName: string;
  readonly service: typeof FineTuningService;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof finetuning_pb.ResubmitFineTuningJobRequest;
  readonly responseType: typeof finetuning_pb.FineTuningJob;
};

type FineTuningServiceGetJobsByUserId = {
  readonly methodName: string;
  readonly service: typeof FineTuningService;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof finetuning_pb.FineTuningJobRequestByUserId;
  readonly responseType: typeof finetuning_pb.FineTuningJobList;
};

type FineTuningServiceGetJobsByOrgId = {
  readonly methodName: string;
  readonly service: typeof FineTuningService;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof finetuning_pb.FineTuningJobRequestByOrgId;
  readonly responseType: typeof finetuning_pb.FineTuningJobList;
};

export class FineTuningService {
  static readonly serviceName: string;
  static readonly CreateFineTuningJob: FineTuningServiceCreateFineTuningJob;
  static readonly GetFineTuningJobById: FineTuningServiceGetFineTuningJobById;
  static readonly UpdateFineTuningJob: FineTuningServiceUpdateFineTuningJob;
  static readonly DeleteFineTuningJob: FineTuningServiceDeleteFineTuningJob;
  static readonly GetFineTuningJobStatus: FineTuningServiceGetFineTuningJobStatus;
  static readonly ResubmitFineTuningJob: FineTuningServiceResubmitFineTuningJob;
  static readonly GetJobsByUserId: FineTuningServiceGetJobsByUserId;
  static readonly GetJobsByOrgId: FineTuningServiceGetJobsByOrgId;
}

export type ServiceError = { message: string, code: number; metadata: grpc.Metadata }
export type Status = { details: string, code: number; metadata: grpc.Metadata }

interface UnaryResponse {
  cancel(): void;
}
interface ResponseStream<T> {
  cancel(): void;
  on(type: 'data', handler: (message: T) => void): ResponseStream<T>;
  on(type: 'end', handler: (status?: Status) => void): ResponseStream<T>;
  on(type: 'status', handler: (status: Status) => void): ResponseStream<T>;
}
interface RequestStream<T> {
  write(message: T): RequestStream<T>;
  end(): void;
  cancel(): void;
  on(type: 'end', handler: (status?: Status) => void): RequestStream<T>;
  on(type: 'status', handler: (status: Status) => void): RequestStream<T>;
}
interface BidirectionalStream<ReqT, ResT> {
  write(message: ReqT): BidirectionalStream<ReqT, ResT>;
  end(): void;
  cancel(): void;
  on(type: 'data', handler: (message: ResT) => void): BidirectionalStream<ReqT, ResT>;
  on(type: 'end', handler: (status?: Status) => void): BidirectionalStream<ReqT, ResT>;
  on(type: 'status', handler: (status: Status) => void): BidirectionalStream<ReqT, ResT>;
}

export class FineTuningServiceClient {
  readonly serviceHost: string;

  constructor(serviceHost: string, options?: grpc.RpcOptions);
  createFineTuningJob(
    requestMessage: finetuning_pb.CreateFineTuningJobRequest,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJob|null) => void
  ): UnaryResponse;
  createFineTuningJob(
    requestMessage: finetuning_pb.CreateFineTuningJobRequest,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJob|null) => void
  ): UnaryResponse;
  getFineTuningJobById(
    requestMessage: finetuning_pb.FineTuningJobRequestById,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJob|null) => void
  ): UnaryResponse;
  getFineTuningJobById(
    requestMessage: finetuning_pb.FineTuningJobRequestById,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJob|null) => void
  ): UnaryResponse;
  updateFineTuningJob(
    requestMessage: finetuning_pb.UpdateFineTuningJobRequest,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJob|null) => void
  ): UnaryResponse;
  updateFineTuningJob(
    requestMessage: finetuning_pb.UpdateFineTuningJobRequest,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJob|null) => void
  ): UnaryResponse;
  deleteFineTuningJob(
    requestMessage: finetuning_pb.FineTuningJobRequestById,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJob|null) => void
  ): UnaryResponse;
  deleteFineTuningJob(
    requestMessage: finetuning_pb.FineTuningJobRequestById,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJob|null) => void
  ): UnaryResponse;
  getFineTuningJobStatus(
    requestMessage: finetuning_pb.FineTuningJobRequestById,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJobStatus|null) => void
  ): UnaryResponse;
  getFineTuningJobStatus(
    requestMessage: finetuning_pb.FineTuningJobRequestById,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJobStatus|null) => void
  ): UnaryResponse;
  resubmitFineTuningJob(
    requestMessage: finetuning_pb.ResubmitFineTuningJobRequest,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJob|null) => void
  ): UnaryResponse;
  resubmitFineTuningJob(
    requestMessage: finetuning_pb.ResubmitFineTuningJobRequest,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJob|null) => void
  ): UnaryResponse;
  getJobsByUserId(
    requestMessage: finetuning_pb.FineTuningJobRequestByUserId,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJobList|null) => void
  ): UnaryResponse;
  getJobsByUserId(
    requestMessage: finetuning_pb.FineTuningJobRequestByUserId,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJobList|null) => void
  ): UnaryResponse;
  getJobsByOrgId(
    requestMessage: finetuning_pb.FineTuningJobRequestByOrgId,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJobList|null) => void
  ): UnaryResponse;
  getJobsByOrgId(
    requestMessage: finetuning_pb.FineTuningJobRequestByOrgId,
    callback: (error: ServiceError|null, responseMessage: finetuning_pb.FineTuningJobList|null) => void
  ): UnaryResponse;
}


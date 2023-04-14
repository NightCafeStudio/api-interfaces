// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var transfer_pb = require('./transfer_pb.js');

function serialize_gooseai_DeleteObjectsByPrefixRequest(arg) {
  if (!(arg instanceof transfer_pb.DeleteObjectsByPrefixRequest)) {
    throw new Error('Expected argument of type gooseai.DeleteObjectsByPrefixRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_gooseai_DeleteObjectsByPrefixRequest(buffer_arg) {
  return transfer_pb.DeleteObjectsByPrefixRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_gooseai_DeleteObjectsByPrefixResponse(arg) {
  if (!(arg instanceof transfer_pb.DeleteObjectsByPrefixResponse)) {
    throw new Error('Expected argument of type gooseai.DeleteObjectsByPrefixResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_gooseai_DeleteObjectsByPrefixResponse(buffer_arg) {
  return transfer_pb.DeleteObjectsByPrefixResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_gooseai_DeleteRequest(arg) {
  if (!(arg instanceof transfer_pb.DeleteRequest)) {
    throw new Error('Expected argument of type gooseai.DeleteRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_gooseai_DeleteRequest(buffer_arg) {
  return transfer_pb.DeleteRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_gooseai_DeleteResponse(arg) {
  if (!(arg instanceof transfer_pb.DeleteResponse)) {
    throw new Error('Expected argument of type gooseai.DeleteResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_gooseai_DeleteResponse(buffer_arg) {
  return transfer_pb.DeleteResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_gooseai_TransferRequest(arg) {
  if (!(arg instanceof transfer_pb.TransferRequest)) {
    throw new Error('Expected argument of type gooseai.TransferRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_gooseai_TransferRequest(buffer_arg) {
  return transfer_pb.TransferRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_gooseai_TransferResponse(arg) {
  if (!(arg instanceof transfer_pb.TransferResponse)) {
    throw new Error('Expected argument of type gooseai.TransferResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_gooseai_TransferResponse(buffer_arg) {
  return transfer_pb.TransferResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


var TransferServiceService = exports.TransferServiceService = {
  // Internal use only. 
// Initiates a transfer of assets between two Stability AI buckets.
transfer: {
    path: '/gooseai.TransferService/Transfer',
    requestStream: false,
    responseStream: false,
    requestType: transfer_pb.TransferRequest,
    responseType: transfer_pb.TransferResponse,
    requestSerialize: serialize_gooseai_TransferRequest,
    requestDeserialize: deserialize_gooseai_TransferRequest,
    responseSerialize: serialize_gooseai_TransferResponse,
    responseDeserialize: deserialize_gooseai_TransferResponse,
  },
  // Internal use only. 
// Deletes specific assets by key from Stability archive bucket.
delete: {
    path: '/gooseai.TransferService/Delete',
    requestStream: false,
    responseStream: false,
    requestType: transfer_pb.DeleteRequest,
    responseType: transfer_pb.DeleteResponse,
    requestSerialize: serialize_gooseai_DeleteRequest,
    requestDeserialize: deserialize_gooseai_DeleteRequest,
    responseSerialize: serialize_gooseai_DeleteResponse,
    responseDeserialize: deserialize_gooseai_DeleteResponse,
  },
  // Internal use only.
// Deletes objects from a bucket by prefix.
deleteObjectsByPrefix: {
    path: '/gooseai.TransferService/DeleteObjectsByPrefix',
    requestStream: false,
    responseStream: false,
    requestType: transfer_pb.DeleteObjectsByPrefixRequest,
    responseType: transfer_pb.DeleteObjectsByPrefixResponse,
    requestSerialize: serialize_gooseai_DeleteObjectsByPrefixRequest,
    requestDeserialize: deserialize_gooseai_DeleteObjectsByPrefixRequest,
    responseSerialize: serialize_gooseai_DeleteObjectsByPrefixResponse,
    responseDeserialize: deserialize_gooseai_DeleteObjectsByPrefixResponse,
  },
};

exports.TransferServiceClient = grpc.makeGenericClientConstructor(TransferServiceService);

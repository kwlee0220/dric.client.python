# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import base_pb2 as base__pb2
import dric_pb2 as dric__pb2


class DrICPlatformStub(object):
    """///////////////////////////////////////////////////////////////
    DrIC Platform request & response protos
    ///////////////////////////////////////////////////////////////

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getServiceEndPoint = channel.unary_unary(
                '/dric.DrICPlatform/getServiceEndPoint',
                request_serializer=base__pb2.StringProto.SerializeToString,
                response_deserializer=dric__pb2.EndPointResponse.FromString,
                )


class DrICPlatformServicer(object):
    """///////////////////////////////////////////////////////////////
    DrIC Platform request & response protos
    ///////////////////////////////////////////////////////////////

    """

    def getServiceEndPoint(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DrICPlatformServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getServiceEndPoint': grpc.unary_unary_rpc_method_handler(
                    servicer.getServiceEndPoint,
                    request_deserializer=base__pb2.StringProto.FromString,
                    response_serializer=dric__pb2.EndPointResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dric.DrICPlatform', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DrICPlatform(object):
    """///////////////////////////////////////////////////////////////
    DrIC Platform request & response protos
    ///////////////////////////////////////////////////////////////

    """

    @staticmethod
    def getServiceEndPoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dric.DrICPlatform/getServiceEndPoint',
            base__pb2.StringProto.SerializeToString,
            dric__pb2.EndPointResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class DrICDataStoreStub(object):
    """///////////////////////////////////////////////////////////////
    DrIC DataStore request & response protos
    ///////////////////////////////////////////////////////////////

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """


class DrICDataStoreServicer(object):
    """///////////////////////////////////////////////////////////////
    DrIC DataStore request & response protos
    ///////////////////////////////////////////////////////////////

    """


def add_DrICDataStoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dric.DrICDataStore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DrICDataStore(object):
    """///////////////////////////////////////////////////////////////
    DrIC DataStore request & response protos
    ///////////////////////////////////////////////////////////////

    """


class DrICVideoServerStub(object):
    """///////////////////////////////////////////////////////////////
    DrIC VideoServer request & response protos
    ///////////////////////////////////////////////////////////////

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.addCamera = channel.unary_unary(
                '/dric.DrICVideoServer/addCamera',
                request_serializer=dric__pb2.CameraInfo.SerializeToString,
                response_deserializer=base__pb2.VoidResponse.FromString,
                )
        self.removeCamera = channel.unary_unary(
                '/dric.DrICVideoServer/removeCamera',
                request_serializer=base__pb2.StringProto.SerializeToString,
                response_deserializer=base__pb2.VoidResponse.FromString,
                )
        self.getCamera = channel.unary_unary(
                '/dric.DrICVideoServer/getCamera',
                request_serializer=base__pb2.StringProto.SerializeToString,
                response_deserializer=dric__pb2.CameraInfo.FromString,
                )
        self.getCameraAll = channel.unary_stream(
                '/dric.DrICVideoServer/getCameraAll',
                request_serializer=base__pb2.VoidProto.SerializeToString,
                response_deserializer=dric__pb2.CameraInfo.FromString,
                )
        self.getCameraFrame = channel.unary_unary(
                '/dric.DrICVideoServer/getCameraFrame',
                request_serializer=dric__pb2.CameraFrameRequest.SerializeToString,
                response_deserializer=dric__pb2.CameraFrameResponse.FromString,
                )
        self.queryCameraFrames = channel.unary_stream(
                '/dric.DrICVideoServer/queryCameraFrames',
                request_serializer=dric__pb2.CameraFrameRangeRequest.SerializeToString,
                response_deserializer=dric__pb2.CameraFrameResponse.FromString,
                )


class DrICVideoServerServicer(object):
    """///////////////////////////////////////////////////////////////
    DrIC VideoServer request & response protos
    ///////////////////////////////////////////////////////////////

    """

    def addCamera(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def removeCamera(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getCamera(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getCameraAll(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getCameraFrame(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def queryCameraFrames(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DrICVideoServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'addCamera': grpc.unary_unary_rpc_method_handler(
                    servicer.addCamera,
                    request_deserializer=dric__pb2.CameraInfo.FromString,
                    response_serializer=base__pb2.VoidResponse.SerializeToString,
            ),
            'removeCamera': grpc.unary_unary_rpc_method_handler(
                    servicer.removeCamera,
                    request_deserializer=base__pb2.StringProto.FromString,
                    response_serializer=base__pb2.VoidResponse.SerializeToString,
            ),
            'getCamera': grpc.unary_unary_rpc_method_handler(
                    servicer.getCamera,
                    request_deserializer=base__pb2.StringProto.FromString,
                    response_serializer=dric__pb2.CameraInfo.SerializeToString,
            ),
            'getCameraAll': grpc.unary_stream_rpc_method_handler(
                    servicer.getCameraAll,
                    request_deserializer=base__pb2.VoidProto.FromString,
                    response_serializer=dric__pb2.CameraInfo.SerializeToString,
            ),
            'getCameraFrame': grpc.unary_unary_rpc_method_handler(
                    servicer.getCameraFrame,
                    request_deserializer=dric__pb2.CameraFrameRequest.FromString,
                    response_serializer=dric__pb2.CameraFrameResponse.SerializeToString,
            ),
            'queryCameraFrames': grpc.unary_stream_rpc_method_handler(
                    servicer.queryCameraFrames,
                    request_deserializer=dric__pb2.CameraFrameRangeRequest.FromString,
                    response_serializer=dric__pb2.CameraFrameResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dric.DrICVideoServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DrICVideoServer(object):
    """///////////////////////////////////////////////////////////////
    DrIC VideoServer request & response protos
    ///////////////////////////////////////////////////////////////

    """

    @staticmethod
    def addCamera(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dric.DrICVideoServer/addCamera',
            dric__pb2.CameraInfo.SerializeToString,
            base__pb2.VoidResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def removeCamera(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dric.DrICVideoServer/removeCamera',
            base__pb2.StringProto.SerializeToString,
            base__pb2.VoidResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getCamera(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dric.DrICVideoServer/getCamera',
            base__pb2.StringProto.SerializeToString,
            dric__pb2.CameraInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getCameraAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dric.DrICVideoServer/getCameraAll',
            base__pb2.VoidProto.SerializeToString,
            dric__pb2.CameraInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getCameraFrame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dric.DrICVideoServer/getCameraFrame',
            dric__pb2.CameraFrameRequest.SerializeToString,
            dric__pb2.CameraFrameResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def queryCameraFrames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dric.DrICVideoServer/queryCameraFrames',
            dric__pb2.CameraFrameRangeRequest.SerializeToString,
            dric__pb2.CameraFrameResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

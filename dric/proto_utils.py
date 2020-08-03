import grpc
from . import pb2

def get_either(proto, case):
    if proto.HasField(case):
        return getattr(proto, case)
    else:
        return None

class InvalidArgument(Exception):
    def __init__(self, details):
        self.details = details
class InvalidState(Exception):
    def __init__(self, details):
        self.details = details
class NotFound(Exception):
    def __init__(self, details):
        self.details = details
class AlreadyExists(Exception):
    def __init__(self, details):
        self.details = details
class Cancelled(Exception):
    def __init__(self, details):
        self.details = details
class Timeout(Exception):
    def __init__(self, details):
        self.details = details
class IoError(Exception):
    def __init__(self, details):
        self.details = details
class GrpcStatus(Exception):
    def __init__(self, details):
        self.details = details
class Internal(Exception):
    def __init__(self, details):
        self.details = details

def handle_pb_error(error):
    code = error.code
    if code == pb2.type.ErrorProto.Code.NOT_FOUND:
        raise NotFound(error.details)
    elif code == pb2.type.ErrorProto.Code.ALREADY_EXISTS:
        raise AlreadyExists(error.details)
    elif code == pb2.type.ErrorProto.Code.INVALID_ARGUMENT:
        raise InvalidArgument(error.details)
    elif code == pb2.type.ErrorProto.Code.INVALID_STATE:
        raise InvalidState(error.details)
    elif code == pb2.type.ErrorProto.Code.CANCELLED:
        raise Cancelled(error.details)
    elif code == pb2.type.ErrorProto.Code.TIMEOUT:
        raise Timeout(error.details)
    elif code == pb2.type.ErrorProto.Code.IO_ERROR:
        raise IoError(error.details)
    elif code == pb2.type.ErrorProto.Code.GRPC_STATUS:
        raise GrpcStatus(error.details)
    elif code == pb2.type.ErrorProto.Code.INTERNAL:
        raise Internal(error.details)
    else:
        raise SystemError(error.details)

def handle_string_response(string_resp):
    case = string_resp.WhichOneof('either')
    if case == 'error':
        handle_pb_error(string_resp.error)
    else:
        return string_resp.value.value

def handle_response(resp, field_name):
    case = resp.WhichOneof('either')
    if case == 'error':
        handle_pb_error(resp.error)
    else:
        return getattr(resp, field_name)

def from_value_proto(proto):
    case = proto.WhichOneof("value")
    if case == 'string_value':
        return proto.string_value
    elif case == 'double_value':
        return proto.double_value
    elif case == 'int_value':
        return proto.int_value
    elif case == 'float_value':
        return proto.float_value
    elif case == 'binary_value':
        return proto.binary_value
    elif case == 'boolean':
        return proto.boolean
    elif case == 'short_value':
        return proto.short_value
    elif case == 'byte_value':
        return proto.byte_value

    elif case == 'datetime_value':
        return proto.datetime_value
    
    elif case == 'geometry_value':
        case = proto.geometry_value.WhichOneof('either')
        if case == 'wkb':
            from shapely.wkb import loads
            return loads(proto.geometry_value.wkb)
        elif case == 'point':
            from shapely.geometry import Point
            pt = proto.geometry_value.point
            return Point(pt.x, pt.y)
        elif case == 'empty_geom_tc':
            pass
        else:
            raise ValueError('invalid Geometry')

    elif case == 'coordinate_value':
        coord_proto = proto.coordinate_value
        return Coordinate(coord_proto.x, coord_proto.y)

    elif case == 'envelope_value':
        envl = proto.envelope_value
        return Envelope(Coordinate(envl.tl.x, envl.tl.y), Coordinate(envl.br.x, envl.br.y))

    elif case == 'null_value':
        return proto.null_value

    else:
        raise ValueError("unknown ValueProto: case=%s" % case)
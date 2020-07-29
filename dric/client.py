import grpc
from . import marmot_type_pb2 as type_pb
from . import marmot_dataset_pb2_grpc as dataset_grpc
from . import dric_pb2_grpc as dric_grpc
from .dric_types import *

__platform = None
__channel = None
__dataset_server_stub = None

class NotConnected(Exception):
    def __init__(self, target):
        self.target = target
    def __str__(self):
        self.target

def connect(host='localhost', port=10703):
    global __platform
    __platform = DrICPlatform(host, port)

    marmot_ep = __platform.get_service_end_point('marmot_server')
    target = '{host}:{port}'.format(host=marmot_ep.host, port=marmot_ep.port)
    global __channel
    __channel = grpc.insecure_channel(target)
    global __dataset_server_stub
    __dataset_server_stub = dataset_grpc.DataSetServiceStub(__channel)

def disconnect():
    global __channel
    if __channel:
        __channel.close()
        __channel = None

def marmot_channel():
    if __channel:
        return __channel
    else:
        raise NotConnected('marmot_server')

def dataset_server_stub():
    if __dataset_server_stub:
        return __dataset_server_stub
    else:
        raise NotConnected('marmot_server')

def assert_platform():
    if __platform == None: raise NotConnected('dric_platform')
    return __platform

class DrICPlatform:
    def __init__(self, host, port):
        self.target = '{host}:{port}'.format(host=host, port=port)
    def with_stub(self, action):
        _logger.debug('connecting DrICPlatform({0})'.format(self.target))
        with grpc.insecure_channel(self.target) as channel:
            stub = dric_grpc.DrICPlatformStub(channel)
            return action(stub)

    def get_service_end_point(self, name):
        svc_name = type_pb.StringProto(value=name)
        resp = self.with_stub(lambda stub: stub.getServiceEndPoint(svc_name))
        case = resp.WhichOneof('either')
        if case == 'error':
            raise resp.error
        else:
            ep = resp.end_point
            _logger.debug('fetch: EndPoint[{0}] = {1}:{2}'.format(name,ep.host,ep.port))
            return ep

__service_end_points = {}
def get_service_point(id):
    ep = __service_end_points.get(id, None)
    if ep: return ep
    ep = assert_platform().get_service_end_point(id)
    __service_end_points[id] = ep
    return ep



import paho.mqtt.client as mqtt
from .mqtt import MqttTopic
from .dric_types import CameraFrame, ObjectBBoxTrack
__builtin_topic_infos = {"dric/camera_frames": CameraFrame,
                        "dric/bbox_tracks": ObjectBBoxTrack }

class TopicNotFound(Exception):
    def __init__(self, name):
        self.topic_name = name

def get_topic(topic, msg_handler=None):
    if not msg_handler:
        msg_handler = __builtin_topic_infos[topic]
        if not msg_handler:
            raise TopicNotFound(topic)
    topic_client = mqtt.Client()
    topic_server = get_service_point('topic_server')
    topic_client.connect(topic_server.host, topic_server.port)
    return MqttTopic(topic_client, topic, msg_handler)



import logging
_logger = logging.getLogger("dric")
_logger.setLevel(logging.WARN)
_logger.addHandler(logging.StreamHandler())
def set_log_level(level):
    _logger.setLevel(level)

if __name__ == '__main__':
    pass

import yaml
import paho.mqtt.client as mqtt
import grpc
import base_pb2
import dric_pb2_grpc
from dric.types import CameraFrame, ObjectBBoxTrack
from .topics import MqttTopic
import logging

__platform = None
__service_end_points = {}
__builtin_topic_infos = {"dric/camera_frames": CameraFrame,
                        "dric/bbox_tracks": ObjectBBoxTrack }
_logger = logging.getLogger("dric")
_logger.setLevel(logging.WARN)
_logger.addHandler(logging.StreamHandler())

class DrICPlatformNotConnected(Exception): pass
class TopicNotFound(Exception):
    def __init__(self, name): self.topic_name = name

def connect(host='localhost', port=10703):
    global __platform
    __platform = DrICPlatform(host, port)

def set_log_level(level):
    _logger.setLevel(level)

def get_service_point(id):
    ep = __service_end_points.get(id, None)
    if ep: return ep
    ep = assert_platform().get_service_end_point(id)
    __service_end_points[id] = ep
    return ep

def get_topic(topic, msg_handler=None):
    if not msg_handler:
        msg_handler = __builtin_topic_infos[topic]
        if not msg_handler:
            raise TopicNotFound(topic)
    topic_client = mqtt.Client()
    topic_server = get_service_point('topic_server')
    topic_client.connect(topic_server.host, topic_server.port)
    return MqttTopic(topic_client, topic, msg_handler)

def assert_platform():
    if __platform == None: raise DrICPlatformNotConnected()
    return __platform

class DrICPlatform:
    def __init__(self, host, port):
        self.target = '{host}:{port}'.format(host=host, port=port)
    def with_stub(self, action):
        _logger.debug('connecting DrICPlatform({0})'.format(self.target))
        with grpc.insecure_channel(self.target) as channel:
            stub = dric_pb2_grpc.DrICPlatformStub(channel)
            return action(stub)
    def get_service_end_point(self, name):
        svc_name = base_pb2.StringProto(value=name)
        ep_resp = self.with_stub(lambda stub: stub.getServiceEndPoint(svc_name))
        case = ep_resp.WhichOneof('either')
        if case == 'error':
            raise ep_resp.error
        else:
            ep = ep_resp.end_point
            _logger.debug('fetch: EndPoint[{0}] = {1}:{2}'.format(name,ep.host,ep.port))
            return ep

if __name__ == '__main__':
    pass
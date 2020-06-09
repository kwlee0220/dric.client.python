
import yaml
import paho.mqtt.client as mqtt
import google.protobuf.wrappers_pb2 as pb_builtin
import grpc
from . import dric_pb2_grpc
from dric.types import CameraFrame, ObjectBBoxTrack
from .topics import MqttTopic

__platform = None
__service_end_points = {}
__builtin_topic_infos = {"dric/camera_frames": CameraFrame,
                        "dric/bbox_tracks": ObjectBBoxTrack }

class DrICPlatformNotConnected(Exception): pass
class TopicNotFound(Exception):
    def __init__(self, name): self.topic_name = name

def connect(host='localhost', port=10703):
    global __platform
    __platform = DrICPlatform(host, port)

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
        with grpc.insecure_channel(self.target) as channel:
            stub = dric_pb2_grpc.DrICPlatformStub(channel)
            return action(stub)
    def get_service_end_point(self, name):
        svc_name = pb_builtin.StringValue(value=name)
        return self.with_stub(lambda stub: stub.getServiceEndPoint(svc_name))

if __name__ == '__main__':
    pass
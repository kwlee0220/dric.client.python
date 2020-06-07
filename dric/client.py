
import yaml
import paho.mqtt.client as mqtt
from .topics import MqttTopic
import grpc
from . import dric_pb2_grpc
#from dric.types import *
import google.protobuf.wrappers_pb2 as pb_builtin
    
class DrICClient:
    def __init__(self, host, port):
        self.platform = DrICPlatform(host, port)

    @classmethod
    def connect(self, host, port):
        return DrICClient(host, port)
    
    def get_topic(self, msg_type, topic):
        topic_client = self.get_topic_client()
        return MqttTopic(topic_client, msg_type, topic)

    def get_topic_client(self):
        ep = self.platform.get_service_end_point("topic_server")
        self.topic_client = mqtt.Client()
        self.topic_client.connect(ep.host, ep.port)
        return self.topic_client

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
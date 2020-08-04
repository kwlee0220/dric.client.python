import grpc
import cv2
# from .pb2 import marmot_type_pb2 as type_pb
# from .pb2 import marmot_dataset_pb2_grpc as dataset_grpc
# from .pb2 import dric_pb2_grpc as dric_grpc
# from .pb2 import proto_utils

__platform = None

class NotConnected(Exception):
    def __init__(self, target):
        self.target = target
    def __str__(self):
        self.target

def connect(host='localhost', port=10703):
    global __platform
    from .platform import DrICPlatform
    __platform = DrICPlatform(host, port)
    return __platform

def disconnect():
    global __platform
    if __platform:
        __platform.disconnect()
        __platform = None

def __get_platform():
    if __platform:
        return __platform
    else:
        raise NotConnected("dric_platform")

def data_server():
    return __get_platform().marmot_runtime.data_server

def get_dataset(ds_id):
    return data_server().get_dataset(ds_id)

class TopicNotFound(Exception):
    def __init__(self, name):
        self.topic_name = name

from .dric_types import CameraFrame, ObjectBBoxTrack
__builtin_topic_infos = {"dric/camera_frames": CameraFrame,
                        "dric/bbox_tracks": ObjectBBoxTrack }
from .mqtt import MqttTopic
def get_topic(topic, msg_handler=None):
    if not msg_handler:
        msg_handler = __builtin_topic_infos[topic]
        if not msg_handler:
            raise TopicNotFound(topic)
    topic_server = __get_platform().get_service_end_point('topic_server')
    return MqttTopic(topic_server.host, topic_server.port, topic, msg_handler)

import logging
_logger = logging.getLogger("dric")
_logger.setLevel(logging.WARN)
_logger.addHandler(logging.StreamHandler())

def set_log_level(level):
    _logger.setLevel(level)

if __name__ == '__main__':
    pass
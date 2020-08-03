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

import logging
_logger = logging.getLogger("dric")
_logger.setLevel(logging.WARN)
_logger.addHandler(logging.StreamHandler())

def set_log_level(level):
    _logger.setLevel(level)

if __name__ == '__main__':
    pass
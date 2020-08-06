import cv2
import dric.pb2 as pb2
from . import proto_utils
import logging

class DrICVideoServer:
    __logger = logging.getLogger("dric.video")
    __logger.setLevel(logging.WARN)
    __logger.addHandler(logging.StreamHandler())

    def __init__(self, host, port):
        self.target = '{host}:{port}'.format(host=host, port=port)

    def with_stub(self, action):
        type(self).__logger.debug('connecting DrICVideoServer({0})'.format(self.target))
        with grpc.insecure_channel(self.target) as channel:
            stub = pb2.dric.DrICVideoServerStub(channel)
            return action(stub)

    def get_camera(self, camera_id):
        id_proto = pb2.type.StringProto(value=camera_id)
        resp = self.with_stub(lambda stub: stub.getCamera(id_proto))
        camera = proto_utils.handle_response(resp, 'camera')
        type(self).__logger.debug('fetch camera: {0}'.format(camera.rtsp_url))
        return cv2.VideoCapture(camera.rtsp_url)
    
    @classmethod
    def set_log_level(cls, level):
        cls.__logger.setLevel(level)
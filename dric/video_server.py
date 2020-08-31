import grpc
from . import pb2
from . import proto_utils
import logging
import cv2

class DrICVideoServer:
    logger = logging.getLogger("dric.video")
    logger.setLevel(logging.WARN)

    def __init__(self, host, port):
        self.target = '{host}:{port}'.format(host=host, port=port)

    def with_stub(self, action):
        type(self).__logger.debug('connecting DrICVideoServer({0})'.format(self.target))
        with grpc.insecure_channel(self.target) as channel:
            stub = pb2.dric_grpc.DrICVideoServerStub(channel)
            return action(stub)

    def get_camera(self, camera_id):
        id_proto = pb2.type.StringProto(value=camera_id)
        resp = self.with_stub(lambda stub: stub.getCamera(id_proto))
        camera_info = proto_utils.handle_response(resp, 'camera_info')
        type(self).logger.debug('fetch camera: {0}'.format(camera_info.rtsp_url))
        return cv2.VideoCapture(camera_info.rtsp_url)

    def get_playback_stream(self, camera_id, start_time, stop_time):
        req = pb2.dric_pb2.PlaybackStreamRequest(camera_id = camera_id, start_time = start_time, stop_time = stop_time)
        resp = self.with_stub(lambda stub: stub.getPlaybackStream(req))
        stream_info = proto_utils.handle_response(resp, 'stream_info')
        type(self).logger.debug('playback_stream: camera={0}, rtsp={1}'.format(camera_id, stream_info.rtsp_url))
        return stream_info
    
    @classmethod
    def set_log_level(cls, level):
        cls.logger.setLevel(level)
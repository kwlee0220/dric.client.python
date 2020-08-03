import grpc
from . import pb2
# from .video_server import *

class DrICPlatform:
    import logging
    __logger = logging.getLogger("dric.platform")
    __logger.setLevel(logging.WARN)
    __logger.addHandler(logging.StreamHandler())

    def __init__(self, host, port):
        self.target = '{host}:{port}'.format(host=host, port=port)
        self.ep_cache = {}
        self.marmot = None

    def disconnect(self):
        if self.marmot:
            self.marmot.close()
            self.marmot = None

    def with_stub(self, action):
        type(self).__logger.debug('connecting DrICPlatform({0})'.format(self.target))
        with grpc.insecure_channel(self.target) as channel:
            stub = pb2.dric_grpc.DrICPlatformStub(channel)
            return action(stub)

    @property
    def marmot_runtime(self):
        if not self.marmot:
            marmot_ep = self.get_service_end_point('marmot_server')

            from .marmot_runtime import MarmotRuntime
            self.marmot = MarmotRuntime(marmot_ep.host, marmot_ep.port)
        return self.marmot

    @property
    def data_server(self):
        return self.marmot_runtime.data_server

    @property
    def video_server(self):
        ep = self.get_service_end_point('video_server')
        from .video_server import DrICVideoServer
        return DrICVideoServer(ep.host, ep.port)

    def get_service_end_point(self, name):
        ep = self.ep_cache.get(name, None)
        if ep: return ep

        svc_name = pb2.type.StringProto(value=name)
        resp = self.with_stub(lambda stub: stub.getServiceEndPoint(svc_name))
        from . import proto_utils
        ep = proto_utils.handle_response(resp, 'end_point')
        self.ep_cache[name] = ep

        type(self).__logger.debug('fetch: EndPoint[{0}] = {1}:{2}'.format(name, ep.host, ep.port))
        return ep
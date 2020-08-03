
import grpc
from . import pb2
from . import proto_utils

class MarmotRuntime:
    import logging
    __logger = logging.getLogger("marmot")
    __logger.setLevel(logging.WARN)
    __logger.addHandler(logging.StreamHandler())

    def __init__(self, host, port):
        self.target = '{host}:{port}'.format(host=host, port=port)
        self.channel = grpc.insecure_channel(self.target)
        self.data_server = DataSetServer(self.channel)

    def close(self):
        self.channel.close()

    @classmethod
    def set_log_level(cls, level):
        cls.__logger.setLevel(level)


class DataSetServer:
    import logging
    __logger = logging.getLogger("marmot.dataset")
    __logger.setLevel(logging.WARN)
    __logger.addHandler(logging.StreamHandler())

    def __init__(self, channel):
        self.stub = pb2.dataset_grpc.DataSetServiceStub(channel)

    def get_dataset(self, ds_id):
        req = pb2.type.StringProto(value=ds_id)
        resp = self.stub.getDataSetInfo(req)
        return self.__handle_dataset_info(resp)
        
    def get_dataset_all(self):
        req = pb2.type.VoidProto()
        for resp in self.stub.getDataSetInfoAll(req):
            yield self.__handle_dataset_info(resp)
            
    def get_dataset_all_in_dir(self, start, recur):
        req = pb2.dataset.DirectoryTraverseRequest(directory=start, recursive=recur)
        for resp in self.stub.getDataSetInfoAllInDir(req):
            yield self.__handle_dataset_info(resp)

    def get_dir_all(self):
        req = pb2.type.VoidProto()
        for resp in self.stub.getDirAll(req):
            yield proto_utils.handle_string_response(resp)

    def get_sub_dir_all(self, start, recur):
        req = pb2.dataset.DirectoryTraverseRequest(directory=start, recursive=recur)
        for resp in self.stub.getSubDirAll(req):
            yield  proto_utils.handle_string_response(resp)
    
    @classmethod
    def set_log_level(cls, level):
        cls.__logger.setLevel(level)

    def __handle_dataset_info(self, resp):
        case = resp.WhichOneof('either')
        if case == 'error':
            proto_utils.handle_pb_error(resp.error)
        else:
            from .dataset import DataSet, MqttDataSet
            if resp.dataset_info.type == pb2.dataset.AVRO:
                return DataSet(self.stub, resp.dataset_info)
            elif resp.dataset_info.type == pb2.dataset.MQTT:
                return MqttDataSet(self.stub, resp.dataset_info)
            else:
                raise ValueError('invalid dataset type: type=%s' % resp.dataset_info.type)
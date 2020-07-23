'''
Created on 2020. 5. 20.

@author: kwlee
'''

from grpc_tools import protoc

protoc.main((
    '',
    '-Iproto',
    '--python_out=.',
    '--grpc_python_out=.',
    'proto/base.proto',
    'proto/type.proto',
    'proto/stream.proto',
    'proto/dataset.proto',
    'proto/dric.proto',
))

if __name__ == '__main__':
    pass
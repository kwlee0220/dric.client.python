'''
Created on 2020. 5. 20.

@author: kwlee
'''

from grpc_tools import protoc

protoc.main((
    '',
    '-Iproto',
    '--python_out=dric',
    '--grpc_python_out=dric',
    'proto/dric.proto',
))

if __name__ == '__main__':
    pass
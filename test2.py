from fastavro import reader
from collections import namedtuple
import dric
from dric.dataset import *

# with open('C:/Temp/dric_store/seoul_stations.avro', 'rb') as fo:
#     avro_reader = reader(fo)
# #    print(avro_reader.schema)
#     for record in avro_reader:
#         print(list(map(record.get, ['KOR_SUB_NM', 'ENG_SUB_NM'])))




dataset = AvroFileDataSet('C:/Temp/dric_store/seoul_stations.avro')
dataset.read()
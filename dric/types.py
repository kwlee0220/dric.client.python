from enum import Enum, unique
from .proto_utils import from_value_proto
from collections import namedtuple, OrderedDict

@unique
class TypeClass(Enum):
    NULL = 0
    BYTE = 1; SHORT = 2; INT = 3; LONG = 4
    FLOAT = 5; DOUBLE = 6
    BOOLEAN = 7; STRING = 8; BINARY = 9
    DATE = 10; TIME = 11; DATETIME = 12
    COORDINATE = 13; ENVELOPE = 14
    POINT = 15; MULTI_POINT = 16; LINESTRING = 17; MULTI_LINESTRING = 18
    POLYGON = 19; MULTI_POLYGON = 20; GEOM_COLLECTION = 21; GEOMETRY = 22
    LIST = 23
    RECORD = 24

class DataType:
    def __init__(self, id, tc):
        self.id = id
        self.tc = tc

    def display_name(self):
        raise NotImplementedError
    def isPrimitiveType(self):
        return False
    def isGeometryType(self):
        return False

    @staticmethod
    def from_type_index(idx):
        try:
            return IDX_TO_TYPES[int(idx)]
        except ValueError:
            import re
            pat = re.compile('(\d+)\((\d+)\)')
            matches = pat.search(idx)
            geom_type = IDX_TO_TYPES[int(matches.group(1))]
            srid = 'EPSG:' + matches.group(2)
            return geom_type.duplicate(srid)

class PrimitiveType(DataType):
    def __init__(self, tc):
        super().__init__('{0}'.format(tc.value), tc)

    def display_name(self):
        return self.tc.name
    def isPrimitiveType(self):
        return True

    def __str__(self):
        return self.display_name()
    def __repr__(self):
        return self.display_name()

class GeometryDataType(DataType):
    def __init__(self, tc, srid):
        super().__init__('{0}'.format(tc.value), tc)
        self.srid = srid
        self.display_name = self.__encode_type_name(tc, srid)

    def get_display_name(self):
        return '{0}({1})'.format(self.tc.name, self.srid)
    def isGeometryType(self):
        return True
    
    def __call__(self, srid):
        return GeometryDataType(self.tc, srid)
    def duplicate(self, srid):
        return GeometryDataType(self.tc, srid)

    def __str__(self):
        return self.get_display_name()

    def __repr__(self):
        return self.get_display_name()

    @staticmethod
    def __encode_type_id(tc, srid):
        if ( srid.startswith('EPSG:') ):
            srid = srid[5:]
        return '{0}({1})'.format(tc.value, srid)

    @staticmethod
    def __encode_type_name(tc, srid):
        if srid is None:
            srid = '?'
        elif ( srid.startswith('EPSG:') ):
            srid = srid[5:]
        return '{0}({1})'.format(tc.name, srid)

class ListType(DataType):
    def __init__(self, elm_type):
        super().__init__('[{0}]'.format(elm_type.id), TypeClass.LIST)
        self.elm_type = elm_type
        self.display_name = 'list[{0}]'.format(elm_type.display_name)

    def display_name(self):
        return self.display_name

class RecordType(DataType):
    def __init__(self, schema):
        super().__init__('[{0}]'.format(elm_type.id), TypeClass.LIST)
        self.schema = schema
        self.display_name = 'list[{0}]'.format(elm_type.display_name)

    def display_name(self):
        return self.display_name

    @staticmethod
    def __encode_type_id(tc, srid):
        pass

from datetime import datetime, time, date
NULL = PrimitiveType(TypeClass.NULL)
BYTE = PrimitiveType(TypeClass.BYTE)
SHORT = PrimitiveType(TypeClass.SHORT)
INT = PrimitiveType(TypeClass.INT)
LONG = PrimitiveType(TypeClass.LONG)
FLOAT = PrimitiveType(TypeClass.FLOAT)
DOUBLE = PrimitiveType(TypeClass.DOUBLE)
STRING = PrimitiveType(TypeClass.STRING)
BOOLEAN = PrimitiveType(TypeClass.BOOLEAN)
BINARY = PrimitiveType(TypeClass.BINARY)
DATETIME = PrimitiveType(TypeClass.BINARY)
DATE = PrimitiveType(TypeClass.BINARY)
TIME = PrimitiveType(TypeClass.BINARY)
COORDINATE = PrimitiveType(TypeClass.COORDINATE)
ENVELOPE = PrimitiveType(TypeClass.ENVELOPE)

POINT = GeometryDataType(TypeClass.POINT, None)
MULTI_POINT = GeometryDataType(TypeClass.MULTI_POINT, None)
LINESTRING = GeometryDataType(TypeClass.LINESTRING, None)
MULTI_LINESTRING = GeometryDataType(TypeClass.MULTI_LINESTRING, None)
POLYGON = GeometryDataType(TypeClass.POLYGON, None)
MULTI_POLYGON = GeometryDataType(TypeClass.MULTI_POLYGON, None)
GEOM_COLLECTION = GeometryDataType(TypeClass.GEOM_COLLECTION, None)
GEOMETRY = GeometryDataType(TypeClass.GEOMETRY, None)

IDX_TO_TYPES = [
    NULL, BYTE, SHORT, INT, LONG, FLOAT, DOUBLE, BOOLEAN, STRING,   # 0 ~ 8
    BINARY, DATE, TIME, DATETIME, COORDINATE, ENVELOPE,             # 9 ~ 14
    POINT, MULTI_POINT, LINESTRING, MULTI_LINESTRING, POLYGON,      # 15
    MULTI_POLYGON, GEOM_COLLECTION, GEOMETRY
]

from collections import namedtuple
Coordinate = namedtuple("Coordinate", 'x y')
Envelope = namedtuple("Envelope", 'tl br')

class ColumnNotFound(Exception):
    def __init__(self, name):
        self.name = name

class ColumnExists(Exception):
    def __init__(self, name):
        self.name = name

AVRO_COLUMNS = {
    TypeClass.BYTE: [{'type': 'int', 'specific': 'BYTE'}, 'null'],
    TypeClass.SHORT: [{'type': 'int', 'specific': 'SHORT'}, 'null'],
    TypeClass.INT: [{'type': 'int', 'specific': 'INT'}, 'null'],
    TypeClass.LONG: [{'type': 'long', 'specific': 'LONG'}, 'null'],
    TypeClass.FLOAT: ['float', 'null'],
    TypeClass.DOUBLE: ['double', 'null'],
    TypeClass.BOOLEAN: ['boolean', 'null'],
    TypeClass.STRING: ['string', 'null'],
    TypeClass.BINARY: ['bytes', 'null'],
    TypeClass.DATETIME: [{'type': 'long', 'specific': 'DATETIME'}, 'null'],
    TypeClass.COORDINATE: [{'type': 'array', 'items': 'double', 'specific': 'COORDINATE'}, 'null'],
    TypeClass.ENVELOPE: [{'type': 'array', 'items': 'double', 'specific': 'ENVELOPE'}, 'null'],
    TypeClass.POINT: [{'type': 'bytes', 'srid': 'EPSG:4326', 'specific': 'POINT'}, 'null'],
}

Column = namedtuple("Column", 'name type ordinal')
class Columns:
    def __init__(self, columns):
        self.column_map = columns
        self.columns = list(columns.values())

    def __len__(self):
        return len(self.columns)

    def __iter__(self):
        # return (col for col in self.columns)
        return iter(self.columns)

    def __getitem__(self, idx):
        if type(idx) == str:
            return self.column_map[idx]
        else:
            return self.columns[idx]

    def __getattr__(self, name):
        return self.column_map[name]

class RecordSchema:
    def __init__(self, columns):
        self.columns = columns
        self.display_name = self.__to_type_name()

        from fastavro import parse_schema
        self.avro_schema = __to_avro_schema(columns.values())
        self.parsed_schema = parse_schema(self.avro_schema)

    @property
    def avro_schema(self):
        return self.__to_avro_schema()
    @property
    def parsed_avro_schema(self):
        return self.__to_avro_schema()
        
    def __str__(self):
        return self.display_name
        
    def __to_type_name(self):
        return '{' + ','.join(['%s:%s'% c[0:2] for c in self.columns.values()]) + '}'

    @staticmethod
    def from_type_id(type_id):
        col_expr_list = type_id[1:-1].split(",")

        builder = RecordSchemaBuilder()
        for col_expr in col_expr_list:
            parts = col_expr.split(":")
            type = DataType.from_type_index(parts[1])
            builder.add(parts[0], type)
        return builder.build()

    @staticmethod
    def __to_avro_schema(columns):
        cols_spec = [__to_avro_column(col) for col in columns]
        avro_schema = { 
            'name': 'simple_feature',
            'namespace': 'etri.marmot',
            'type': 'record',
            'fields': cols_spec
        }
        return avro_schema
    @staticmethod
    def __to_avro_column(col):
        col_spec = AVRO_COLUMNS[col.type.tc]
        return { 'name': col.name, 'type': col_spec }

class RecordSchemaBuilder:
    def __init__(self):
        self.columns = OrderedDict()
        self.__next_idx = 0

    def add(self, name, data_type):
        if name in self.columns:
            raise ColumnExists(name)
        self.columns[name] = Column(name, data_type, self.__next_idx)
        self.__next_idx += 1
        return self

    def build(self):
        return RecordSchema(self.columns)

class Record:
    def __init__(self, schema, values=None):
        self.schema = schema
        if values:
            self.values = values
        else:
            self.values = tuple(None for col in schema.columns.values())

    def to_bytes(self):
        with BytesIO() as fo:
            schemaless_writer(fo, self.schema, to_dict())
            fo.flush()
            return fo.getvalue()
            
    @classmethod
    def from_bytes(cls, bytes):
        with BytesIO(bytes) as fo:
            grec = schemaless_reader(fo, cls.PARSED_AVRO_SCHEMA)
            return Record.from_dict(grec, cls.SCHEMA)

    def to_dict(self):
        return { col.name: self.values[col.ordinal] for col in self.schema.columns.values() }

    @classmethod
    def from_dict(cls, dict, schema):
        values = tuple(Record.__parse_avro_value(dict, col) for col in schema.columns.values())
        return cls(schema, values)

    @staticmethod
    def __parse_avro_value(dict, col):
        avro_value = dict.get(col.name)
        if avro_value is not None:
            return parse_avro_value(avro_value, col.type)
        else:
            return None

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return iter(self.values)

    def __getitem__(self, idx):
        col = self.schema.columns[idx]
        if isinstance(col, Column):
            return self.values[col.ordinal]
        elif type(col) == list:
            return tuple(self.values[c.ordinal] for c in col)

    def __getattr__(self, name):
        ret = getattr(self.schema.columns, name)
        if isinstance(ret, Column):
            return self.values[ret.ordinal]
        else:
            return ret
        
    def __repr__(self):
        return '(' + ', '.join(['%s:%s' % (col[0], self[col[2]]) for col in self.schema.columns]) + ')'
        
    def __str__(self):
        return '(' + ', '.join(['%s' % (self.values[col[2]]) for col in self.schema.columns]) + ')'

def write_avro_value(value, type):
    if type.isPrimitiveType:
        if type.tc == TypeClass.STRING or type.tc == TypeClass.INT or type.tc == TypeClass.DOUBLE or    \
            type.tc == TypeClass.LONG or type.tc == TypeClass.FLOAT or type.tc == TypeClass.SHORT or \
            type.tc == TypeClass.BOOLEAN or type.tc == TypeClass.BOOLEAN or type.tc == TypeClass.BYTE or \
            type.tc == TypeClass.BINARY or type.tc == TypeClass.DATETIME:
            return value
        elif type.tc == TypeClass.COORDINATE:
            return list(value)
        elif type.tc == TypeClass.ENVELOPE:
            return list(value.tl) + list(value.br)
    elif type.isGeometryType:
        from shapely.wkb import dumps
        return dumps(value)
    else:
        pass

def parse_avro_value(value, type):
    if type.isPrimitiveType:
        if type.tc == TypeClass.STRING or type.tc == TypeClass.INT or type.tc == TypeClass.DOUBLE or    \
            type.tc == TypeClass.LONG or type.tc == TypeClass.FLOAT or type.tc == TypeClass.SHORT or \
            type.tc == TypeClass.BOOLEAN or type.tc == TypeClass.BOOLEAN or type.tc == TypeClass.BYTE or \
            type.tc == TypeClass.BINARY or type.tc == TypeClass.DATETIME:
            return value
        elif type.tc == TypeClass.COORDINATE:
            return Coordinate(value[0], value[1])
        elif type.tc == TypeClass.ENVELOPE:
            tl = Coordinate(value[0], value[1])
            br = Coordinate(value[2], value[3])
            return Envelope(tl, br)
    elif type.isGeometryType:
        from shapely.wkb import loads
        return loads(value)
    else:
        pass
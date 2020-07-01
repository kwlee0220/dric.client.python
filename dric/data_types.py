from enum import Enum, unique

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
    def __init__(self, id, tc, inst_class):
        self.id = id
        self.tc = tc
        self.inst_class = inst_class

    def display_name(self):
        raise NotImplementedError

    @classmethod
    def LIST(cls, elm_type):
        return ListType()

class PrimitiveType(DataType):
    def __init__(self, tc, inst_class):
        super().__init__('{0}'.format(tc.value), tc, inst_class)

    def display_name(self):
        return self.tc.name

    def __str__(self):
        return self.display_name()
    def __repr__(self):
        return self.display_name()

class GeometryDataType(DataType):
    def __init__(self, tc, inst_class, srid):
        super('{0}'.format(tc.value), tc, inst_class)
        self.display_name = self.__encode_type_name(tc, srid)

    @staticmethod
    def __encode_type_id(tc, srid):
        if ( srid.startswith('EPSG:') ):
            srid = srid[5:]
        return '{0}({1})'.format(tc.value, srid)

    @staticmethod
    def __encode_type_name(tc, srid):
        if ( srid.startswith('EPSG:') ):
            srid = srid[5:]
        return '{0}({1})'.format(tc.name, srid)

class ListType(DataType):
    def __init__(self, elm_type):
        super().__init__('[{0}]'.format(elm_type.id), TypeClass.LIST, None)
        self.elm_type = elm_type
        self.display_name = 'list[{0}]'.format(elm_type.display_name)

    def display_name(self):
        return self.display_name

class RecordType(DataType):
    def __init__(self, schema):
        super().__init__('[{0}]'.format(elm_type.id), TypeClass.LIST, None)
        self.schema = schema
        self.display_name = 'list[{0}]'.format(elm_type.display_name)

    def display_name(self):
        return self.display_name

    @staticmethod
    def __encode_type_id(tc, srid):
        pass

NULL = PrimitiveType(TypeClass.NULL, type(None))
BYTE = PrimitiveType(TypeClass.BYTE, int)
SHORT = PrimitiveType(TypeClass.SHORT, int)
INT = PrimitiveType(TypeClass.INT, int)
LONG = PrimitiveType(TypeClass.LONG, int)
FLOAT = PrimitiveType(TypeClass.FLOAT, float)
DOUBLE = PrimitiveType(TypeClass.DOUBLE, float)
STRING = PrimitiveType(TypeClass.STRING, str)
from data_types import *
from collections import namedtuple

Column = namedtuple("Column", 'name type ordinal')
class RecordSchema:
    def __init__(self, columns):
        self.columns = columns
        self.display_name = self.__to_type_name()

    def get_column_count(self):
        return len(self.columns)

    def __iter__(self):
        return (col for col in self.columns)

    def __getitem__(self, key):
        if ( isinstance(key, str) ):
            for col in self.columns:
                if col[0] == key:
                    return col
            return None
        else:
            return self.columns[key]

    def __contains__(self, col_name):
            for col in self.columns:
                if col[0] == col_name:
                    return True
            return False

    def __getattr__(self, name):
        for col in self.columns:
            if col[0] == name:
                return col
        return None
        
    def __str__(self):
        return self.display_name
        
    def __to_type_name(self):
        return 'RECORD{' + ','.join(['%s:%s'% col[0:2] for col in self.columns]) + '}'

class RecordSchemaBuilder:
    def __init__(self):
        self.columns = []
        self.__next_idx = 0

    def add(self, name, data_type):
        self.columns.append(Column(name, data_type, self.__next_idx))
        self.__next_idx += 1
        return self

    def build(self):
        return RecordSchema(self.columns)

class Record:
    def __init__(self, schema):
        self.__schema = schema
        self.__values = [None for col in schema.columns]

    def get_column_count(self):
        return self.__schema.get_column_count()

    def __iter__(self):
        return iter(self.__values)

    def __getitem__(self, key):
        if ( isinstance(key, str) ):
            col = self.__schema[key]
            if col:
                return self.__values[col[2]]
            else:
                return None
        else:
            self.__values[key]

    def __getattr__(self, name):
        col = getattr(self.__schema, name)
        if col:
            return self.__values[col[2]]
        else:
            return None
        
    def __str__(self):
        return '{' + ', '.join(['%s:%s' % (col[0], self[col[2]]) for col in self.__schema]) + '}'

class DataSet:
    def read(self):
        pass

print(STRING)
print(Column("name", STRING, -1))
schema = RecordSchemaBuilder().add("name", STRING).add("age", INT).build()
print(schema)
print(schema["age"])
print(schema["kkk"])
print('name' in schema)
print('abc' in schema)
print(schema[1])
print(schema.age.type)

names = [col.name for col in schema]
print(names)

record = Record(schema)
print(record)
print(record.age)
print(record[1])
(a, b) = record
print(a)
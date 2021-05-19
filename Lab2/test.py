import base64
from dis import dis
import pytest
import Json
import roune



class A:
    def sum(self, a, b):
        return a + b
    d = 23.1
    def __init__(self):
        self.a = True
        self.b = 21
        self.c = 'Something'






global a
a=5
def sum(b):
    return a + b



test_simple_hash = {"key1":['None', [1,2],
    {"key": {"key": [1,2]}, "key1": 1},1], "key2": None}

test_simple_hash2= {"key1":[3, [1,2],
    {"key": {"key": [1,2]}, "key1": 1},1], "key2": 2}




SIMPLE_OBJECTS =A()




def test_simple_object():
    serializer=Json.Json()
    print(test_simple_hash, 'hdfgdgf')
    strdata=serializer.dumps(test_simple_hash)
    print(strdata, 'hj')
    fromstrdata=serializer.loads(strdata)
    print(fromstrdata)
    strdata1=serializer.dumps(fromstrdata)
    fromstrdata1=serializer.loads(strdata1)
    assert fromstrdata1==test_simple_hash


def test_simple_object2():
    serializer=Json.Json()
    strdata=serializer.dumps(SIMPLE_OBJECTS)
    print(strdata, '2')
    fromstrdata=serializer.loads(strdata)
    print(fromstrdata, '3')
    print(fromstrdata.sum(1,2) ,'4')
    print(dir(fromstrdata),'5')
    print(dir(SIMPLE_OBJECTS),'6')
    strdata1=serializer.dumps(fromstrdata)
    fromstrdata1=serializer.loads(strdata1)
    assert dir(fromstrdata1)==dir(SIMPLE_OBJECTS)

SIMPLE_OBJECTS2=sum
def test_simple_object3():
    serializer=Json.Json()
    strdata=serializer.dumps(sum)
    print(strdata, 'hi')
    fromstrdata=serializer.loads(strdata)
    print(fromstrdata, '3 usual')
    print(dir(fromstrdata),'5 dir')
    print(dir(fromstrdata),'5 dir')
    print(dir(sum),'6 dir')
    assert roune._function_equals(sum, fromstrdata)



# import Pickle
#
# def test_simple_objectp():
#     serializer=Pickle.Pickle()
#     print(test_simple_hash, 'hdfgdgf')
#     strdata=serializer.dumps(test_simple_hash)
#     print(strdata, 'hj')
#     fromstrdata=serializer.loads(strdata)
#     print(fromstrdata)
#     assert fromstrdata==test_simple_hash
# #
# SIMPLE_OBJECTS =A()
# def test_simple_object2p():
#     serializer=Pickle.Pickle()
#     strdata=serializer.dumps(SIMPLE_OBJECTS)
#     # print(strdata, '2')
#     fromstrdata=serializer.loads(strdata)
#     print(fromstrdata, '3')
#     print(dir(fromstrdata),'5')
#     print(dir(SIMPLE_OBJECTS),'6')
#     assert dir(fromstrdata)==dir(SIMPLE_OBJECTS)
#
# SIMPLE_OBJECTS1=k
# def test_simple_object3p():
#     serializer=Pickle.Pickle()
#     # strdata=serializer.dumps(SIMPLE_OBJECTS1)
#     # print(strdata, '2')
#     strdata=b'\x80\x04\x95\x10\x00\x00\x00\x00\x00\x00\x00\x8c\x04test\x94\x8c\x03sum\x94\x93\x94.'
#     fromstrdata=serializer.loads(strdata)
#     print(fromstrdata, '3')
#     print(SIMPLE_OBJECTS1)
#     # print(dir(fromstrdata),'5')
#     # print(dir(SIMPLE_OBJECTS1),'6')
#     assert dir(fromstrdata)==dir(SIMPLE_OBJECTS1)
#

# import Yaml
# import Toml
# import toml
# serializer=Toml.Toml()
# serializer=Yaml.Yaml()
#
#
# def test_simple_objecty():
#     k=test_simple_hash
#     strdata=toml.dumps(k)
#     print(strdata, 'hgfew')
#     fromstrdata=serializer.loads(strdata)
#     print(fromstrdata, 'bjfghf')
#     print(test_simple_hash, 'hgfew')
#     assert strdata!=test_simple_hash2

# SIMPLE_OBJECTS =A()
# def test_simple_object2y():
#     strdata=serializer.dumps(SIMPLE_OBJECTS)
#     # print(strdata, '2')
#     fromstrdata=serializer.loads(strdata)
#     print(fromstrdata, '3')
#     print(fromstrdata['__base64__'])
#     k=fromstrdata['__base64__']
#     base64_bytes=base64.b64encode(k)
#     print(base64_bytes, 'sdgdssdgds')
#     print(dir(fromstrdata),'5')
#     print(dir(SIMPLE_OBJECTS),'6')
#     #assert dir(fromstrdata) == dir(SIMPLE_OBJECTS)
#     assert fromstrdata.__dict__==SIMPLE_OBJECTS.__dict__ #Yaml
#
# SIMPLE_OBJECTS1=sum
# def test_simple_object3y():
#     strdata=serializer.dumps(SIMPLE_OBJECTS1)
#     print(strdata, '2')
#     fromstrdata=serializer.loads(strdata)
#     print(fromstrdata, '3')
#     # print(fromstrdata.a ,'4')
#     print(dir(fromstrdata),'5')
#     print(dir(SIMPLE_OBJECTS1),'6')
#     assert dir(fromstrdata)==dir(SIMPLE_OBJECTS1)

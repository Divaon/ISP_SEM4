import base64
from dis import dis
import pytest
import Yaml
import roune
import Serializer



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


def test_simple_objectwrite():
    serializer=Yaml.Yaml()
    print(test_simple_hash, 'hdfgdgf')
    strdata=serializer.dump(test_simple_hash, 'test.yaml')
    print(strdata, 'hj')
    fromstrdata=serializer.load('test.yaml')
    print(fromstrdata)
    assert fromstrdata==test_simple_hash



def test_simple_object():
    serializer=Yaml.Yaml()
    print(test_simple_hash, 'hdfgdgf')
    strdata=serializer.dumps(test_simple_hash)
    print(strdata, 'hj')
    fromstrdata=serializer.loads(strdata)
    print(fromstrdata)
    strdata1=serializer.dumps(fromstrdata)
    fromstrdata1=serializer.loads(strdata1)
    assert fromstrdata1==test_simple_hash


def test_simple_object2():
    serializer=Yaml.Yaml()
    strdata=serializer.dumps(SIMPLE_OBJECTS)
    fromstrdata=serializer.loads(strdata)
    print(dir(fromstrdata),'5')
    print(dir(SIMPLE_OBJECTS),'6')
    assert dir(fromstrdata)==dir(SIMPLE_OBJECTS)

SIMPLE_OBJECTS2=sum
def test_simple_object3():
    serializer=Yaml.Yaml()
    strdata=serializer.dumps(sum)
    print(strdata, 'hi')
    fromstrdata=serializer.loads(strdata)
    print(fromstrdata, '3 usual')
    print(fromstrdata(5))
    print(dir(fromstrdata),'5 dir')
    print(dir(fromstrdata),'5 dir')
    print(dir(sum),'6 dir')
    assert roune._function_equals(sum, fromstrdata)

import pytest

import main
import Pickle
import Toml
import Yaml
import Json

def sum(a,b):
    return a+b

test_simple_hash = {"key1":[3, [1,2], {"key": {"key": [1,2]}, "key1": 1},1], "key2": 2}

class A:

    d=23.1

    def __init__(self):
        self.a=True
        self.b=21
        self.c='Something'

    def sum(self, a, b):
        return a+b

SIMPLE_OBJECTS =A()





def test_simple_objectp():
    serializer=Pickle.Pickle()
    print(test_simple_hash, 'hdfgdgf')
    strdata=serializer.dumps(test_simple_hash)
    print(strdata, 'hj')
    fromstrdata=serializer.loads(strdata)
    print(fromstrdata)
    assert fromstrdata==test_simple_hash


def test_simple_object2p():
    serializer=Pickle.Pickle()
    strdata=serializer.dumps(SIMPLE_OBJECTS)
    # print(strdata, '2')
    fromstrdata=serializer.loads(strdata)
    # print(fromstrdata, '3')
    # print(fromstrdata.a ,'4')
    print(dir(fromstrdata),'5')
    print(dir(SIMPLE_OBJECTS),'6')
    assert fromstrdata==SIMPLE_OBJECTS

SIMPLE_OBJECTS =sum

def test_simple_object3p():
    serializer=Pickle.Pickle()
    strdata=serializer.dumps(SIMPLE_OBJECTS)
    # print(strdata, '2')
    fromstrdata=serializer.loads(strdata)
    # print(fromstrdata, '3')
    # print(fromstrdata.a ,'4')
    print(dir(fromstrdata),'5')
    print(dir(SIMPLE_OBJECTS),'6')
    assert fromstrdata==SIMPLE_OBJECTS




SIMPLE_OBJECTS =A()





def test_simple_objectt():
    serializer=Toml.Toml()
    print(test_simple_hash, 'hdfgdgf')
    strdata=serializer.dumps(test_simple_hash)
    print(strdata, 'hj')
    fromstrdata=serializer.loads(strdata)
    print(fromstrdata)
    assert fromstrdata==test_simple_hash


def test_simple_object2t():
    serializer=Toml.Toml()
    strdata=serializer.dumps(SIMPLE_OBJECTS)
    # print(strdata, '2')
    fromstrdata=serializer.loads(strdata)
    # print(fromstrdata, '3')
    # print(fromstrdata.a ,'4')
    print(dir(fromstrdata),'5')
    print(dir(SIMPLE_OBJECTS),'6')
    assert fromstrdata==SIMPLE_OBJECTS

SIMPLE_OBJECTS =sum

def test_simple_object3t():
    serializer=Toml.Toml()
    strdata=serializer.dumps(SIMPLE_OBJECTS)
    # print(strdata, '2')
    fromstrdata=serializer.loads(strdata)
    # print(fromstrdata, '3')
    # print(fromstrdata.a ,'4')
    print(dir(fromstrdata),'5')
    print(dir(SIMPLE_OBJECTS),'6')
    assert fromstrdata==SIMPLE_OBJECTS


SIMPLE_OBJECTS = A()


def test_simple_objecty():
    serializer = Yaml.Yaml()
    print(test_simple_hash, 'hdfgdgf')
    strdata = serializer.dumps(test_simple_hash)
    print(strdata, 'hj')
    fromstrdata = serializer.loads(strdata)
    print(fromstrdata)
    assert fromstrdata == test_simple_hash


def test_simple_object2y():
    serializer = Yaml.Yaml()
    strdata = serializer.dumps(SIMPLE_OBJECTS)
    # print(strdata, '2')
    fromstrdata = serializer.loads(strdata)
    # print(fromstrdata, '3')
    # print(fromstrdata.a ,'4')
    print(dir(fromstrdata),'5')
    print(dir(SIMPLE_OBJECTS),'6')
    assert fromstrdata== SIMPLE_OBJECTS


SIMPLE_OBJECTS = sum


def test_simple_object3y():
    serializer = Yaml.Yaml()
    strdata = serializer.dumps(SIMPLE_OBJECTS)
    # print(strdata, '2')
    fromstrdata = serializer.loads(strdata)
    # print(fromstrdata, '3')
    # print(fromstrdata.a ,'4')
    print(dir(fromstrdata),'5')
    print(dir(SIMPLE_OBJECTS),'6')
    assert fromstrdata== SIMPLE_OBJECTS





import base64
from dis import dis

import pytest


import main
import Json

a=3


class A:
    def sum(self, a, b):
        return a + b
    d = 23.1
    def __init__(self):
        self.a = True
        self.b = 21
        self.c = 'Something'






a=5
def sum(c,  b):
    return c + b

def k(self, a, b):
    return a + b


test_simple_hash = {"key1":[3, [1,2],
    {"key": {"key": [1,2]}, "key1": 1},1], "key2": 2}

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
    assert fromstrdata1.__dict__==SIMPLE_OBJECTS.__dict__

def test_simple_object3():
    serializer=Json.Json()
    strdata=serializer.dumps(sum)
    print(strdata, 'hi')
    fromstrdata=serializer.loads(strdata)
    print(fromstrdata, '3 usual')
    print(dir(fromstrdata),'5 dir')
    print(dir(fromstrdata),'5 dir')
    print(dir(sum),'6 dir')
    assert dir(fromstrdata)==dir(sum)





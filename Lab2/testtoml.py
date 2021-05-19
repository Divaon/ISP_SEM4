import pytest
import base64
from dis import dis
import pytest
import Json
import Toml
import roune

b=4

test_simple_hash={"key5": 1, "key6":{"keyd1":6, "keyd2":[1,2],"key":{"keydd1":5},"keyk" : 7}}
test_simple_hash2={"key1": 1.1 , "key2":True, "key3"  :False, "key4": "i am string", "key5": 1, "key6":[2,8,'hi', [2,45],  ['hi']] }
test_simple_hash3={ "key5": 1, "key6":{"keyd1":6, "keyd2":[1,2],"key":{"keydd1":5},"keyk" : 7}, "kkkkkey": 5}
test_simple_hash4={"key5": 'None', "key6":{"keyd1":6, "keyd2":[1,2]}, "key":None, "b":b}




class A:
    def sum(self, c, b):
        return c + b
    d = 23.1
    def __init__(self):
        self.a = True
        self.b = 21
        self.c = 'Something'






a=5
b=2
def sum( b):
    print(globals)
    return a + b

def k(self, a, b):
    return a + b
SIMPLE_OBJECTS =A()

def test_simple_object():
    serializer = Toml.TomlSerializer()
    strdata=serializer.ddumps(test_simple_hash4)
    # print(strdata, 'from dumps')
    # print("Hii")
    fromdata=serializer.loads(strdata)
    print()
    print(fromdata, 'from loads')
    print(test_simple_hash4, 'original')
    assert fromdata==test_simple_hash4

def test_simple_object2():
    serializer=Toml.TomlSerializer()
    strdata=serializer.ddumps(SIMPLE_OBJECTS)
    print(strdata, '2')
    fromstrdata=serializer.loads(strdata)
    print(fromstrdata, '3')
    print(fromstrdata.sum(3,2) ,'4')
    print(dir(fromstrdata),'5')
    print(dir(SIMPLE_OBJECTS),'6')
    strdata1=serializer.ddumps(fromstrdata)
    fromstrdata1=serializer.loads(strdata1)
    assert dir(fromstrdata1)==dir(SIMPLE_OBJECTS)

SIMPLE_OBJECTS2=sum
def test_simple_object3():
    serializer=Toml.TomlSerializer()
    strdata=serializer.ddumps(sum)
    #print(strdata, 'hi')
    fromstrdata=serializer.loads(strdata)
    print(fromstrdata, '3 usual')
    #print(dir(fromstrdata),'5 dir')
    #print(dir(fromstrdata),'5 dir')
    #print(dir(sum),'6 dir')
    print(sum)
    assert roune._function_equals(sum, fromstrdata)



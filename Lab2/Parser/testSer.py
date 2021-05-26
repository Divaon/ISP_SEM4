import Serializer
import pytest
import roune
import Json
import Toml


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

test_simple_hash = {"key1": [3,[1,2]], "key": {"key3": [1,2]}, "key4": 1, "key2": 2}




def test_simple_object_json():
    converfromfile = Serializer.CreateDesirializator()
    converfromfile1 = Serializer.CreateDesirializator()
    converfromfile2 = Serializer.CreateDesirializator()
    converttofile = Serializer.CreateSirializator()
    converttofile1 = Serializer.CreateSirializator()
    converttofile2 = Serializer.CreateSirializator()
    converttofile2.serialize(test_simple_hash, 'JSON', 'teest.json')
    strdata1=converfromfile.deserialize('JSON', 'teest.json')
    converttofile.serialize(strdata1, 'TOML', 'teest.toml')
    strdata2=converfromfile1.deserialize('TOML', 'teest.toml')
    converttofile1.serialize(strdata1, 'PICLE', 'teest.picle')
    strdata3 = converfromfile2.deserialize('PICLE', 'teest.picle')
    assert strdata1==test_simple_hash and strdata1==strdata2 and strdata1==strdata3


SIMPLE_OBJECTS =A()
def test_class_json():
    converfromfile = Serializer.CreateDesirializator()
    converfromfile1 = Serializer.CreateDesirializator()
    converfromfile2 = Serializer.CreateDesirializator()
    converttofile = Serializer.CreateSirializator()
    converttofile1 = Serializer.CreateSirializator()
    converttofile2 = Serializer.CreateSirializator()
    converttofile2.serialize(SIMPLE_OBJECTS, 'JSON', 'teest.json')
    strdata1=converfromfile.deserialize('JSON', 'teest.json')
    converttofile.serialize(strdata1, 'TOML', 'teest.toml')
    strdata2=converfromfile1.deserialize('TOML', 'teest.toml')
    converttofile1.serialize(strdata1, 'PICLE', 'teest.picle')
    strdata3 = converfromfile2.deserialize('PICLE', 'teest.picle')
    assert strdata3.sum(1,2)==strdata2.sum(1,2) and strdata1.sum(1,2)==strdata2.sum(1,2)

SIMPLE_OBJECTS2=sum
def test_function_json():
    converfromfile = Serializer.CreateDesirializator()
    converfromfile1 = Serializer.CreateDesirializator()
    converfromfile2 = Serializer.CreateDesirializator()
    converttofile = Serializer.CreateSirializator()
    converttofile1 = Serializer.CreateSirializator()
    converttofile2 = Serializer.CreateSirializator()
    converttofile2.serialize(SIMPLE_OBJECTS2, 'JSON', 'teest.json')
    strdata1=converfromfile.deserialize('JSON', 'teest.json')
    converttofile.serialize(strdata1, 'TOML', 'teest.toml')
    strdata2=converfromfile1.deserialize('TOML', 'teest.toml')
    converttofile1.serialize(SIMPLE_OBJECTS2, 'PICLE', 'teest.picle')
    strdata3 = converfromfile2.deserialize('PICLE', 'teest.picle')
    assert roune._function_equals(strdata1, strdata2) and roune._function_equals(strdata1, strdata3)
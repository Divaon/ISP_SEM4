import re
import Parser.json_converter as json_converter
import inspect

from types import FunctionType
import sys
import types

class JsonSerializer:
    _complexconvert=False


    def dumps(self, obj) -> str:
        ret=''
        if  type(obj) is list:
            ret=ret+'['
            for i in range(0, len(obj)):
                if i!=0:
                    ret=ret+','
                ret=ret+self.dumps(obj[i])
            ret=ret+']'
        elif type(obj) is dict:
            ret=ret+'{'
            for key in obj.keys():
                if list(obj.keys())[0]!=key:
                    ret=ret+', '
                dumpedkey=self.dumps(key)
                if dumpedkey[0]!='"' and dumpedkey[-1]!='"':
                    dumpedkey='"'+dumpedkey+'"'
                ret=ret+dumpedkey
                ret=ret+': '
                ret=ret+self.dumps(obj[key])
            ret=ret+'}'
        elif type(obj) is str:
            ret=ret+f"\"{obj}\""
        elif type(obj) is bool:
            if obj:
                ret=ret+'true'
            else:
                ret = ret + 'false'
        elif (type(obj) is float) or (type(obj) is int):
            ret=ret+str(obj)
        else:
            ret=ret+str(obj)
        with open('test.txt', 'w') as f:
            f.write(ret)
        return ret

    def loads(self, string):
        obj=json_converter.convert(string)
        with open('test.txt', 'w') as f:
            f.write(str(obj))
        return obj





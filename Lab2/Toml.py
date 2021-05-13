import types
import TOML_converter


class TomlSerializer:
    def dumps(self,  obj)->str:
        ret = ''
        if  type(obj) is list:
            ret=ret+'[ '
            for i in range(0, len(obj)):
                if i!=0:
                    ret=ret+', '
                ret=ret+self.dumps(obj[i])
            ret=ret+' ]'
        elif type(obj) is dict:
            for key in obj.keys():
                if list(obj.keys())[0] != key:
                    ret = ret + '\n'
                ret = ret + key
                ret = ret + ' = '
                ret = ret + self.dumps(obj[key])
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
        return ret

    def loads(self, string):
        obj=TOML_converter.convert(string)
        return obj





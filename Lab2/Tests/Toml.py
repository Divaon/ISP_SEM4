import types
import TOML_converter
import Pickle
import inspect
import base64
import types
import logging
import traceback

class A:
  d = 23.1

  def __init__(self):
    self.a = True
    self.b = 21
    self.c = 'Something'

  def sum(self, a, b):
    a=1
    b=3
    return a + b


f_found = {}
sort_keys = False

SIMPLE_OBJECTS = A()



class TomlSerializer:

    def __init__(self):
        self.dict_words=[]

    def dumps(self,  obj):
        return self.ddump(self._prepare(obj))

    def dump(self, obj, filepath):
      print(obj)
      string=self.dumps(obj)
      with open(filepath, 'w') as f: 
        f.write(string)

    def ddump(self,  obj)->str:
        ret = ''
        if  type(obj) is list:
            ret = self.save_list(ret, obj)
        elif type(obj) is dict:
            ret = self.save_dict(ret, obj)
        else:
            ret = self.save_simple_value(ret, obj)
        with open('test.txt', 'w') as f:
            f.write(ret)
        return ret

    def save_simple_value(self, ret, obj):
        if (type(obj) is float) or (type(obj) is int):
            ret=ret+str(obj)
        elif type(obj) is bool:
            if obj:
                ret=ret+'true'
            else:
                ret = ret + 'false'
        elif type(obj) is str:
            ret=ret+f"\"{obj}\""
        else:
            ret=ret+str(obj)
        ret += '\n'
        return ret

    def save_list(self, ret, obj):
        ret=ret+'[ '
        for i in range(0, len(obj)):
            if i!=0:
                ret=ret+', '
            ret=ret+self.ddump(obj[i])
            ret = ret[:-1]
        ret=ret+' ]\n'
        return ret

    def build_section_name(self):
        string='['
        for i in range(0,len(self.dict_words)):
            if i!=len(self.dict_words)-1:
                string=string+self.dict_words[i]+'.'
            else:
                string=string+self.dict_words[i]
        string=string+']'
        return string

    def save_dict(self, ret, obj):
        string=''
        tt=''        
        if not self.dict_words:
            self.dict_words.append('Start')
            ret=ret+'['+self.dict_words[0]+']'+'\n'
        for key, value in obj.items():
            if type(value)==dict:
                self.dict_words.append(key)
                string = self.build_section_name()
                ret=ret+string+'\n'
                ret = ret + self.ddump(obj[key])
            else:
                ret = ret + key
                ret = ret + ' = '
                ret = ret + self.ddump(obj[key])
            if type(value)==dict:
                self.dict_words.remove(key)
                string=self.build_section_name()
                ret=ret+string+'\n'
        return ret



    def loads(self, string, complex_convert=True):
        result=TOML_converter.convert('[Start]',string)
        if complex_convert:
          if "function_type" in result and len(result.keys()) == 1:
              des = Pickle.Pickle()
              return des.loads(result["function_type"])
          if 'class' in result.get('__type__', ''):
                print(result, 2)
                obj=globals()[result['__name__']]()
                for k, b in result.items():
                    if not k.startswith('__'):
                        obj.__dict__[k]=b
                return obj
          else:
                return result
        else:
            return result

    def load(self, filepath, complex_convert=True):
      with open(filepath, 'r') as f:
        string=f.read()
      return self.loads(string, complex_convert)




    def _prepare(self, obj):
      if isinstance(obj, (int, float, int, bool, str)) or \
        obj is None:
        return obj
      elif isinstance(obj, list):
        for index in range(len(obj)):
          obj[index] = self._prepare(obj[index])
        return obj
      elif isinstance(obj, types.FunctionType):
        ser=Pickle.Pickle()
        return {"function_type": ser.dumps(obj)}

      elif isinstance(obj, dict):
        for key, value in obj.items():
          obj[key] = self._prepare(value)

        return obj

      else:
        value = dict()
        try:
          for k, b in obj.__dict__.items():
            if not k.startswith('__'):
              value[k]=b

          if obj.__class__.__name__ == 'type':
            name = obj.__name__
          else:
            name = obj.__class__.__name__
          value["__type__"]=str(type(obj))
          value["__name__"] = name
          return value

        except Exception as e:
          traceback.print_exc()
          logging.error(repr(obj) + ' is not serializable' + repr(e))
          exit()





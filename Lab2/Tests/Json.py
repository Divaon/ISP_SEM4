import Pickle
import main
import pickle
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


class Json:
  def dump(self, obj, filepath):
    string=self.dumps(obj)
    with open(filepath, 'w') as f: 
      f.write(string)

  def dumps(self, obj):
    serial=main.JsonSerializer()
    return serial.dumps(self._prepare(obj))

  def load(self, file_stream):
    return main.JsonSerializer.load(file_stream)

  def loads(self, string, complex_convert=True):
    serial=main.JsonSerializer()
    print(string)
    result=serial.loads(string)
    if complex_convert:
      if "function_type" in result and len(result.keys()) == 1:
        des = Pickle.Pickle()
        return des.loads(result["function_type"])
      if 'class' in result.get('__type__', ''):
        print(result, 1)
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



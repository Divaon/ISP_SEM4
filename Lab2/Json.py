
import main
import pickle
import inspect
import base64
import types
import logging
import traceback
import json



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
  def dump(self, obj, file_stream):
    json.dumps(self._prepare(obj), file_stream, default=self._dificult_objects, indent=2)

  def dumps(self, obj):
    serial=main.JsonSerializer()
    return serial.dumps(self._prepare(obj))

  def load(self, file_stream):
    return main.JsonSerializer.load(file_stream)

  def loads(self, string):
    serial=main.JsonSerializer()
    result=serial.loads(string)
    if "function_type" in result and len(result.keys()) == 1:
      return dict_to_func(result["function_type"])

    if 'class' in result.get('__type__', ''):
      obj=globals()[result['__name__']]()
      for k, b in result.items():
        if not k.startswith('__'):
          obj.__dict__[k]=b
      return obj
    else:
      return result


  def _prepare(self, obj):
    if isinstance(obj, (int, float, int, bool, str)) or \
      obj is None:
      return obj
    elif isinstance(obj, list):
      for index in range(len(obj)):
        obj[index] = self._prepare(obj[index])
      return obj
    elif isinstance(obj, types.FunctionType):
      return function_to_dict(obj)

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

  def _dificult_objects(self, obj):
    if isinstance(obj, (set, tuple)):

      return {
        "__type__" : str(type(obj)),
      }

    elif isinstance(obj, types.FunctionType):
      source = []
      out = ""

      for char in inspect.getsource(obj):
        if char == '\n':
          source.append(out)
          out = ""
          continue

        out += char

      return {
        "__type__" : str(type(obj)),
        "__name__" : obj.__name__,
        "__sorce__" : source
      }

    else:
      try:
        fields = [field for field in dir(obj) if not field.startswith("__")]
        s_obj = str(base64.b64encode(pickle.dumps(obj)))

        if obj.__class__.__name__ == 'type':
          name = obj.__name__
        else:
          name = obj.__class__.__name__

        return {
          "__type__" : str(type(obj)),
          "__name__" : name
        }

      except:
        logging.error(repr(obj) + ' is not json serializable')
        exit()

def gather_gls (obj, obj_code):
  global f_found
  f_found[obj] = True
  gls = {}
  for i in obj_code.co_names:
    try:
      if inspect.isfunction(obj.__globals__[i]):
        if obj.__globals__[i] not in f_found:
          gls[i] = function_to_dict(obj.__globals__[i])
    except KeyError:
      pass
    for i in obj_code.co_consts:
      if isinstance(i, types.CodeType):
        gls.update(gather_gls(obj, i))
    return gls

def function_to_dict(obj):
  gls = gather_gls(obj, obj.__code__)
  return {
    "function_type": {
      "__globals__": gls,
      "__name__": obj.__name__,
      "__code__": code_to_dict(obj.__code__),
      "__defaults__": obj.__defaults__,
      "__closure__": obj.__closure__,
      }
    }

def collect_funcs(obj, is_visited):
    for i in obj.__globals__:
      attr = obj.__globals__[i]
      if inspect.isfunction(attr) and attr.__name__ not in is_visited:
        is_visited[attr.__name__] = attr
        is_visited = collect_funcs(attr, is_visited)
    return is_visited

def set_funcs(obj, is_visited, gls):
  for i in obj.__globals__:
    attr = obj.__globals__[i]
    if inspect.isfunction(attr) and attr.__name__ not in is_visited:
      is_visited[attr.__name__] = True
      attr.__globals__.update(gls)
      is_visited = set_funcs(attr, is_visited, gls)
  return is_visited

def dict_to_code(obj):
    return types.CodeType(
      obj["co_argcount"],
      obj["co_posonlyargcount"],
      obj["co_kwonlyargcount"],
      obj["co_nlocals"],
      obj["co_stacksize"],
      obj["co_flags"],
      bytes(bytearray(obj["co_code"])[0]),
      tuple([x for x in obj["co_consts"] if x is not None]),
      tuple([x for x in obj["co_names"] if x is not None]),
      tuple([x for x in obj["co_varnames"] if x is not None]),
      obj["co_filename"],
      obj["co_name"],
      obj["co_firstlineno"],
      bytes(bytearray(obj["co_lnotab"])[0]),
      tuple([x for x in obj["co_freevars"] if x is not None]),
      tuple([x for x in obj["co_cellvars"] if x is not None]),
    )

def code_to_dict(obj):
  return {
    "code_type": {
        "co_argcount": obj.co_argcount,
        "co_posonlyargcount": obj.co_posonlyargcount,
        "co_kwonlyargcount": obj.co_kwonlyargcount,
        "co_nlocals": obj.co_nlocals,
        "co_stacksize": obj.co_stacksize,
        "co_flags": obj.co_flags,
        "co_code": obj.co_code,
        "co_consts": list(obj.co_consts),
        "co_names": list(obj.co_names),
        "co_varnames": list(obj.co_varnames),
        "co_filename": obj.co_filename,
        "co_name": obj.co_name,
        "co_firstlineno": obj.co_firstlineno,
        "co_lnotab": obj.co_lnotab,
        "co_freevars": list(obj.co_freevars),
        "co_cellvars": list(obj.co_cellvars),
      }
    }

def dict_to_func(obj):
  closure = None
  if obj["__closure__"] is not None:
    closure = obj["__closure__"]
  if obj["__globals__"] is  None:
    obj["__globals__"] = {}
  res = types.FunctionType(
    globals=obj["__globals__"],
    code=dict_to_code(obj["__code__"]['code_type']),
    name=obj["__name__"],
    closure=closure,
  )
  try:
    setattr(res, "__defaults__", obj["__defaults__"])
  except TypeError:
    pass
  funcs = collect_funcs(res, {})
  funcs.update({res.__name__: res})
  set_funcs(res, {res.__name__: True}, funcs)
  res.__globals__.update(funcs)
  res.__globals__["__builtins__"] = __import__("builtins")
  return res

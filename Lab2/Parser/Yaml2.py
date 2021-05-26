import yaml
import inspect

class YamlParser:
    def dumps(self, obj):
        if type(obj) is int or type(obj) is float or type(obj) is bool or type(obj) is str or \
                isinstance(obj, type(None)):
            return obj
        if type(obj) is list:
            result = []
            if len(obj) == 0:
                return result
            for i in range(len(obj)):
                result += self.dumps(obj[i])
            return result
        elif isinstance(obj, dict):
            result = {}
            if len(obj) == 0:
                return result
            for key in obj.keys():
                val_str = self.dumps(obj[key])
                result[key] = val_str
            return result
        elif isinstance(obj, tuple):
            result = {"_tuple_": []}
            for i in obj:
                result["_tuple_"].append(self.dumps(i))
            return result
        elif isinstance(obj, set):
            result = {"_set_": []}
            for i in obj:
                result["_set_"].append(self.dumps(i))
            return result
        elif inspect.isfunction(obj):
            count = 0
            result = {"type": "_function_"}
            code = inspect.getsource(obj)
            name = obj.__name__
            args = {}
            result["name"] = name
            tup = obj.__code__.co_names
            for i in tup:
                if i in obj.__globals__ and not inspect.isbuiltin(obj.__globals__[i]):
                    args[i] = self.dumps(obj.__globals__[i])
                    count += 1
            result["args"] = args
            result["function_code"] = code.replace('"', "'")
            return result
        elif inspect.isclass(obj):
            result = {"type": "_class_"}
            code = inspect.getsource(obj)
            name = obj.__name__
            result["name"] = name
            method_list = {}
            attr_list = {}
            for attribute in dir(obj):
                attribute_value = getattr(obj, attribute)
                if callable(attribute_value) and (attribute.endswith('__') is False or attribute == '__init__'):
                    method_list[attribute] = attribute_value
                elif not callable(attribute_value) and attribute.endswith('__') is False:
                    attr_list[attribute] = attribute_value
            args = {}
            globals_dict = globals()
            for i in method_list:
                for j in method_list[i].__code__.co_names:
                    if j in method_list[i].__globals__ and not inspect.isbuiltin(method_list[i].__globals__[j]):
                        args[j] = self.dumps(method_list[i].__globals__[j])
            for k in attr_list:
                if k in globals_dict:
                    args[j] = self.dumps(globals_dict[j])
            result["args"] = args
            result["class_code"] = code.replace('"', "'")
            return result

        elif not inspect.isclass(obj) and inspect.isclass(type(obj)):
            result = {"type": "_class_object_"}
            code = inspect.getsource(type(obj))
            name = type(obj).__name__
            method_list = {}
            attr_list = {}
            for attribute in dir(obj):
                attribute_value = getattr(obj, attribute)
                if callable(attribute_value) and (attribute.endswith('__') is False or attribute == '__init__'):
                    method_list[attribute] = attribute_value
                elif not callable(attribute_value) and attribute.endswith('__') is False:
                    attr_list[attribute] = attribute_value
            args = {}
            set_args = {}
            init_args = {}
            # print("sdfdgd",attr_list)
            init_vars = obj.__class__.__init__.__code__.co_varnames
            # print(obj.__class__.__init__.__code__.co_varnames)
            for i in attr_list.keys():
                if i in init_vars:
                    init_args[i] = attr_list[i]
                else:
                    set_args[i] = attr_list[i]
            globals_dict = globals()
            for i in method_list:
                for j in method_list[i].__code__.co_names:
                    if j in method_list[i].__globals__ and not inspect.isbuiltin(method_list[i].__globals__[j]):
                        args[j] = self.dumps(method_list[i].__globals__[j])
            print(self.dumps(args))
            result["name"] = name
            result["args"] = args
            result["init"] = self.dumps(init_args)
            result["set_args"] = self.dumps(set_args)
            result["class_code"] = code.replace('"', "'")
            print(result)
            return result
        else:
            return obj
        # return pickle.dumps(obj)

    def dump(self, obj, fp):
        print("Yaml Dump")
        with open(fp,'w') as f:
            yaml.dump(self.dumps(obj), f)

    def loads(self, output, need_dict=False):
        if not need_dict:
            if output is list:
                parsed_output = []
                for i in output:
                    if i is list or i is dict:
                        parsed_output.append(self.loads(i, need_dict))
                    else:
                        parsed_output.append(i)
                return parsed_output
            elif isinstance(output, dict):
                if "_tuple_" in output:
                    vals = output["_tuple_"]
                    return tuple(self.loads(vals))
                elif "_set_" in output:
                    vals = output["_set_"]
                    return set(self.loads(vals))
                elif "type" in output:
                    if output["type"] == "_function_":
                        # print(output)
                        val = self._yes_its_func(output)
                        return val
                    elif output["type"] == "_class_" or output["type"] == "_class_object_":
                        # print(output)
                        val = self._yes_its_class(output)
                        return val
                else:
                    parsed_output = {}
                    for i in output:
                        parsed_output[i] = self.loads(output[i], need_dict)
                    return parsed_output
            else:
                return output
        else:
            return output

    def load(self, fp, need_dict=False):
        print("Yaml Load")
        with open(fp) as f:
            output = yaml.safe_load(f)
        return self.loads(output, need_dict)

    def _yes_its_func(self, _dict_func):
        y = {}
        q = {}
        for i in _dict_func['args']:
            if isinstance(_dict_func['args'][i], list):
                if _dict_func['args'][i][0] == "_tuple_":
                    val = tuple(self.loads(_dict_func['args'][i], False))
                    q[i] = val
                elif _dict_func['args'][i][0] == "_set_":
                    val = set(self.loads(_dict_func['args'][i], False))
                    q[i] = val
            elif isinstance(_dict_func['args'][i], dict):
                if _dict_func['args'][i]['type'] == "_function_":
                    func = self._yes_its_func(_dict_func['args'][i])
                    q[i] = func
                elif _dict_func['args'][i]['type'] == "_class_" or _dict_func['args'][i]['type'] == "_class_object_":
                    obj = self._yes_its_class(_dict_func['args'][i])
                    q[i] = obj
            else:
                val = _dict_func['args'][i]
                q[i] = val
        exec(_dict_func["function_code"], q, y)
        print(y)
        return y[_dict_func["name"]]

    def _yes_its_class(self, class_dict):
        y = {}
        q = {}
        for i in class_dict['args']:
            if isinstance(class_dict['args'][i], list):
                if class_dict['args'][i][0] == "_tuple_":
                    val = tuple(self.loads(class_dict['args'][i], False))
                    q[i] = val
                elif class_dict['args'][i][0] == "_set_":
                    val = set(self.loads(class_dict['args'][i], False))
                    q[i] = val
            elif isinstance(class_dict['args'][i], dict):
                if class_dict['args'][i]['type'] == "_function_":
                    func = self._yes_its_func(class_dict['args'][i])
                    q[i] = func
                elif class_dict['args'][i]['type'] == "_class_":
                    obj = self._yes_its_class(class_dict['args'][i])
                    q[i] = obj
                elif class_dict['args'][i]['type'] == "_class_object_":
                    class_type = self._yes_its_class(class_dict['args'][i])
                    obj = class_type(**self.loads(class_dict["init"], False))
                    for j in class_dict["set_args"]:
                        obj.__setattr__(j, self.loads(class_dict["set_args"][j], False))
                    q[i] = obj
            else:
                val = class_dict['args'][i]
                q[i] = val
        exec(class_dict["class_code"], q, y)
        if not class_dict['type'] == "_class_object_":
            return y[class_dict["name"]]
        else:
            example = y[class_dict["name"]]
            obj = example(**self.loads(class_dict["init"], False))
            for j in class_dict["set_args"]:
                obj.__setattr__(j, self.loads(class_dict["set_args"][j], False))
            return obj
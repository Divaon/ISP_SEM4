import Parser.Json as Json

class Yaml:

    # According to yaml spec json is valid yaml, so we just can use json
    # https://yaml.org/spec/1.2/spec.html 

    json_parsers = Json.Json()

    def dump(self,string,filepath):
        return self.json_parsers.dump(string,filepath)

    def dumps(self,string):
        return self.json_parsers.dumps(string)

    def loads(self,string, complex_convert=True):
        return self.json_parsers.loads(string, complex_convert)
    
    def load(self,filepath, complex_convert=True):
        return self.json_parsers.load(filepath, complex_convert)

import Json
import Pickle
import Toml
import Yaml
import logging

class CreateSirializator:
    def serialize(self, obj, format, filepath):
        self.serialize=None
        print(format)
        if format=='JSON':
            self.serialize=Json.Json()
        elif format=='TOML':
            self.serialize=Toml.TomlSerializer()
        elif format=='YAML':
            self.serialize=Yaml.Yaml()
        elif format=='PICLE':
            self.serialize=Pickle.Pickle()
            with open(filepath, 'wb') as f:
                return self.serialize.dump(obj, f)
        else:
            logging.error("Unsuported type from load ")
            exit()
        return self.serialize.dump(obj, filepath)

class CreateDesirializator:
    def deserialize(self, format, filepath):
        self.deserialize=None
        if format=='JSON':
            self.deserialize=Json.Json()
        elif format=='TOML':
            self.deserialize=Toml.TomlSerializer()
        elif format=='YAML':
            self.deserialize=Yaml.Yaml()
        elif format=='PICLE':
            self.deserialize=Pickle.Pickle()
            with open(filepath, 'rb') as f:
                return self.deserialize.load(f)
        else:
            logging.error("Unsuported type from dump ")
            exit()
        return self.deserialize.load(filepath)

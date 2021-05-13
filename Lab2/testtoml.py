import pytest

import TOML

test_simple_hash={"key1 ": 1.1 , "key2 ":True, "key3 "  :False, "key4 ": "i am string", "key5 ": 1}
                  #"key6":[1, 2, 'hi'] }

test_simple_hash2={"key1 ": 1.1 , "key2 ":True, "key3 "  :False, "key4 ": "i am string", "key5 ": 1, "key6":[1, 2, 'hi'] }




def test_simple_object():
    serializer = TOML.TomlSerializer()
    strdata=serializer.dumps(test_simple_hash)
    # print(strdata, 'from dumps')
    fromdata=serializer.loads(strdata)
    print()
    print(fromdata, 'from loads')
    print(test_simple_hash, 'original')
    assert fromdata==test_simple_hash


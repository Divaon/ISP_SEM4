
def save_value(key, dictkeys, result, value):
    current_result = result
    for dictkey in dictkeys:
        dictkey = dictkey.replace('[', '')
        dictkey = dictkey.replace(']', '')
        current_result[dictkey] = current_result.get(dictkey, {})
        current_result = current_result[dictkey]
    current_result[key] = value


def convert(checkline,toml_string: str) ->dict:
    result = {}
    dictkeys = ['Start']

    for line in toml_string.splitlines():
        if line.startswith('['):
            dictkeys = line.split('.')
            continue
        first_equals_symbol_index = line.index('=')
        key = line[:first_equals_symbol_index].strip()
        value = line[first_equals_symbol_index+1:].strip()
        value = calculate_list(value)
        save_value(key, dictkeys, result, value)
    return result['Start']

def skip_unnecessary_chars(string):
    i = 0
    all_char_skipped = False
    while not all_char_skipped and i < len(string):
        c = string[i]
        if c in (']', '}', ',', ' ', ':',):
            i += 1
        else:
            all_char_skipped = True
    return string[i:]


def calculate_list(string):
    string = string.strip()
    value_list = []
    value_builder = []
    sq_brackets = []
    string=skip_unnecessary_chars(string)
    i = 0
    if string[:2]=='= ':
        string=string[2:]
    elif string[0]=='=':
        string=string[1:]
    if  string[0]!='[':
        return calculate_value(string)
    if string=='[  ]':
        value_list.append(None)
        return value_list
    while i < len(string):
        i += 1
        char = string[i]
        if char == ',' and len(sq_brackets) == 0:
            value_list.append(''.join(value_builder))
            value_builder = []
        else:
            value_builder.append(char)
            if char == '[':
                sq_brackets.append('[')
            elif char == ']':
                if len(sq_brackets):
                    sq_brackets.pop()
                else:
                    value_builder = value_builder[:-1]
                    value_list.append(''.join(value_builder))
                    return [convert_value(x) for x in value_list]




def calculate_object(string):
    value_builder = []
    curly_brackets = []
    for i in range(len(string)):
        char = string[i]
        if char == '{':
            curly_brackets.append('{')
        value_builder.append(char)
        if char == '}':

            if len(curly_brackets) > 1:
                curly_brackets.pop()
            else:
                value_str = ''.join(value_builder)
                return value_str


def calculate_value(string):
    string = string.strip()
    value_builder = []
    if string.startswith('{'):
        return calculate_object(string)

    for i in range(len(string)):
        char = string[i]
        if char in ('}', ',') or i==len(string):
            value_str = ''.join(value_builder)
            return convert_value(value_str)
        else:
            value_builder.append(char)
    value_str = ''.join(value_builder)
    return convert_value(value_str)


def convert_value(value_str):
    value_str = value_str.strip()
    if value_str == 'true':
        return True
    elif value_str == 'false':
        return False
    elif value_str.startswith('b'):
        return eval(value_str)
    elif value_str == 'None':
        return None
    elif value_str == '':
        return None
    elif value_str.startswith('"'):
        value_str = value_str.replace('"', '')
        return value_str
    elif value_str.startswith('{'):
        return convert(value_str)  
    elif value_str.startswith('['):
        return calculate_list(value_str)
    elif '.' in value_str:
        return float(value_str)
    else:
        return int(value_str)


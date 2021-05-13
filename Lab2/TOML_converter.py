def convert(json_string: str) ->dict:

    json_string=json_string.replace('\n',' , ')
    value_started = False
    field_name = None
    result = {}

    i = 0
    json_string=json_string+','
    while i < len(json_string):
        char = json_string[i]
        # if json_string=='= 1':
        #     print(json_string[0],'i')
        #     print(i)
        #     print(json_string, 'control')
        if not field_name:
            field_name, json_string = calculate_key(json_string)
            print(field_name,'k')
            field_name=field_name[:len(field_name)-1]
            print(field_name,'k')
            print(json_string,'kk')
            json_string = skip_unnecessary_chars(json_string)
            i = 0
        elif not value_started and (char == '=' or json_string[0]=='='):
            print(json_string, 'value_started')
            value_started = True
        elif value_started:
            print(json_string, 'krehg')
            value, json_string = calculate_list(json_string)
            value=value[2:]
            print(value, 'kkktest')
            print(json_string, 'kkktest')
            i = 0
            json_string = skip_unnecessary_chars(json_string)
            value = value if isinstance(value, list) else convert_value(value ) #? isinstance
            result[field_name] = value
            field_name = None
            value_started = False
            continue
        i += 1

    return result

def skip_unnecessary_chars(string):
    i = 0
    all_char_skipped = False
    while not all_char_skipped and i < len(string):
        c = string[i]
        if c in (']', '}', ',', ' ', ':'):
            i += 1
        else:
            all_char_skipped = True
    return string[i:]


def calculate_key(string):
    field_started = False
    field_name_builder = []
    i = 0
    while i < len(string):
        char = string[i]
        if not field_started and string[i+1] == '=':
            field_started = True
        elif field_started:
            return string[:i], string[i-1:]
        i += 1


def calculate_list(string):
    string = string.strip()
    value_list = []
    value_builder = []
    sq_brackets = []
    curly_brackets = []
    if not string.startswith('['):
        return calculate_value(string)
    i = 0
    while i < len(string):
        i += 1
        char = string[i]
        if char == ',' and len(sq_brackets) == len(curly_brackets) == 0:
            value_list.append(''.join(value_builder))
            value_builder = []
        else:
            value_builder.append(char)
            if char == '[':
                sq_brackets.append('[')
            elif char == '{':
                curly_brackets.append('{')
            elif char == '}':
                curly_brackets.pop()
            elif char == ']':
                if len(sq_brackets):
                    sq_brackets.pop()
                else:
                    value_builder = value_builder[:-1]
                    value_list.append(''.join(value_builder))
                    return [convert_value(x) for x in value_list], string[i:]


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
                return value_str, string[i:]


def calculate_value(string):
    string = string.strip()
    value_builder = []
    # print("Start value")
    # print(len(string))
    if string.startswith('{'):
        return calculate_object(string)

    for i in range(len(string)):
        char = string[i]
        if char in ('}', ',') or i==len(string):
            value_str = ''.join(value_builder)
            # print(string, 'check value')
            # print(''.join(value_str), 'ccheck value')
            return value_str, string[i:]
        else:
            # print(''.join(value_builder), 'char')
            value_builder.append(char)


def convert_value(value_str):
    value_str = value_str.strip()
    if value_str == 'true':
        return True
    elif value_str == 'false':
        return False
    elif value_str=='None':
        return None
    elif value_str.startswith("b'"):
        value_str=value_str.replace("b'",'')
        value_str=value_str.replace("'",'')
        return ' '.join(format(ord(x), 'b') for x in value_str)
    elif value_str.startswith('"'):
        value_str = value_str.replace('"', '')
        return value_str
    elif value_str.startswith('{'):
        return convert(value_str)
    elif value_str.startswith('['):
        return calculate_list(value_str)[0]
    elif '.' in value_str:
        return float(value_str)
    else:
        return int(value_str)

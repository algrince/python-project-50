#!/usr/bin/env pyhton3

from gendiff.formats.default import sort_data


statuses = {
    'equal': '',
    'added': "Property '{key}' was added with value: {value1}\n",
    'removed': "Property '{key}' was removed\n",
    'updated': "Property '{key}' was updated. From {value1} to {value2}\n"
}

def formate_plain(data, nest_lvl=0):
    sorted_data = sort_data(data)
    string_data = make_plain(sorted_data)
    return string_data



def make_plain(sorted_data, key=''):
    string_data = ''
    for line in sorted_data:
        old_key, value, status, nest, update = line
        if key != '':
            new_key = key + '.' + old_key
            act_key = key
        else:
            new_key = old_key
            act_key = old_key
        if update == 'updated':
            print('a saltar', line)
            continue
        elif nest == 'nested':
            if status == 'equal':
                string_line = make_plain(value, key=new_key)
            else:
                value = transform_complex(value)
                if isinstance(update, dict):
                    value2 = update.get('updated')
                    status = 'updated'
                else:
                    value2 = None
                value2 = transform_complex(value2)
                string_line = make_plain_string(act_key, value, value2, status)
            string_data += string_line
    return string_data
        
    

def transform_complex(var):
    if isinstance(var, list):
        var = '[complex value]'
    return var


def make_plain_string(old_key, val1, val2, status):
    added_status = statuses[status]
    if status == 'added':
        string_line = added_status.format(
            key=old_key,
            value1=trans_var(val1)
        )
    elif status == 'removed':
        string_line = added_status.format(
            key=old_key
        )
    elif status == 'updated':
        string_line = added_status.format(
            key=old_key,
            value1=trans_var(val1),
            value2=trans_var(val2)
        )
    return string_line


def trans_var(var):
    if var != '[complex value]':
        var = f"'{var}'"
    return var



'''
def formate_plain(data, nest_lvl=0):
    sorted_data = sort_data(data)
    string_data = ''
    for line in sorted_data:
        plain_data = make_plain(line)
        if plain_data is None:
            continue
        else:
            plain_string = make_plain_string(plain_data)
            string_data += plain_string
    return string_data


def make_plain(line, key=''):
    update = line[-1]
    old_key = line[0]
    if update == 'updated':
        plain_diff is None
    else:
        if line[-2] == 'nested':
            if key != '':
                new_key = key + '.' + old_key
            else:
                new_key = old_key
            plain_diff = make_plain(line[1])
        else:
            if isinstance(update, dict):
                value = line[1]
                value2 = update.get('updated')
                state = 'updated'
            else:
                value = line[1]
                value2 = None
                state = line[-3]
            value, value2 = transform_complex(value, value2)
            plain_diff = [old_key, value, value2, state]
    return plain_diff
        

def make_plain_string(line):
    print(line)
    state = line[2]
    added_status = statuses[state]
    if state == 'added':
        string_diff = added_status.format(
            key=line[0], 
            value1=line[1]
        )
    elif state == 'removed':
        string_diff = added_status.format(
            key=line[0]
        )
    elif state == 'updated':
        string_diff = added_status.format(
            key=line[0],
            value1=line[1],
            value2=line[2]
        )
    return string_diff


def transform_complex(var1, var2):
    if isinstance(var1, dict):
        var1 = '[complex value]'
    elif isinstance(var2, dict):
        var2 = '[complex value]'
    return var1, var2


def make_plain_line(line, nest_lvl=0):
    if len(line) == 1:
        return line[0]
    key, value, state, nest, update = line
    if isinstance(update, dict):
        value2 = update.get('updated')
        state = 'updated'
    else:
        value2 = None
    value, value2 = transform_complex(value, value2)
    return [key, value, value2, state] '''

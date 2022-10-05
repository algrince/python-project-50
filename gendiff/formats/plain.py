#!/usr/bin/env pyhton3

from gendiff.formats.default import sort_data


statuses = {
    'equal': '',
    'added': 'Property {key} was added with value {value1}\n',
    'removed': 'Property {key} was removed\n',
    'updated': 'Property {key} was updated. From {value1} to {value2}\n'
}


def formate_plain(data, nest_lvl=0):
    sorted_data = sort_data(data)
    plain_data = make_plain(sorted_data)
    string_data = make_plain_string(plain_data)
    return string_data


def make_plain(sorted_data, key=''):
    plain_diff = []
    for line in sorted_data:
        s_key, s_value, s_state, s_nest, s_update = line
        s_key = key + '.' + s_key
        if line[4] == 'updated':
            print('UPDATED', line, '\n')
            continue
        else:
            if line[3] == 'nested':
                print('nested line', line, '\n')
                line = make_plain(s_value, key=s_key)
            print('line', line, '\n')
            plain_line = make_plain_line(line)
            plain_diff.append(plain_line)
            print('DIFF', plain_diff)
    return plain_diff
        

def make_plain_string(plain_data):
    string_diff = ''
    for line in plain_data:
        state = line[2]
        added_status = statuses[state]
        if state == 'added':
            string_diff += added_status.format(
                key=line[0], 
                value1=line[1]
            )
        elif state == 'removed':
            string_diff += added_status.format(
                key=line[0]
            )
        elif state == 'updated':
            string_diff += added_status.format(
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
    return [key, value, value2, state]

#!/usr/bin/env pyhton3

from gendiff.formats.default import sort_data


statuses = {
    'added': 'Property {key} was added with value {value1}\n',
    'removed': 'Property {key} was removed\n',
    'updated': 'Property {key} was updated. From {value1} to {value2}\n'
}


def formate_plain(data, nest_lvl=0):
    sorted_data = sort_data(data)
    for line in sorted_data:
        if line[3] == 'nested':
            level = nest_lvl + 1
            line[1] = formate_plain(line[1], nest_lvl=level)
    string_data = make_plain(sorted_data, nest_lvl)
    return string_data


def make_plain(sorted_data, nest_lvl=0):
    string_diff = ''
    for line in sorted_data:
        print('sorted line', line)
        if line[2] == 'equal' or line[4] == 'updated':
            continue
        else:
            plain_line = make_plain_line(line, nest_lvl=0)
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
    print(line)
    key, value, state, nest, update = line
    if isinstance(update, dict):
        value2 = update.get('updated')
        state = 'updated'
    else:
        value2 = None
    value, value2 = transform_complex(value, value2)
    return [key, value, value2, state]

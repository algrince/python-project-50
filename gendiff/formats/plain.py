#!/usr/bin/env pyhton3

from gendiff.formats.default import sort_data


statuses = {
    'added': 'Property {key} was added with value {value1}\n',
    'removed': 'Property {key} was removed\n',
    'updated': 'Property {key} was updated. From {value1} to {value2}\n'
}


def formate_plain(data, nest_lvl=0):
    sorted_data = sort_data(data)
    plain_data = decode_plain(sorted_data, nest_lvl=0)
    data_string = ''
    for line in plain_data:
        key, value1, value2, status = line
        added_status = statuses[status]
        data_string += added_status.format(
            key=key, value1=value1, value2=value2)
    return data_string




def decode_plain(sorted_data, nest_lvl=0):
    plain_data = []
    for line in sorted_data:
        print(line)
        key, value, state, nest, update = line
        value2 = None
        if state == 'equal' or update == 'updated':
            continue
        elif nest == 'nested':
            if isinstance(update, dict):
                value2 = update.get('updated')
                value, value2 = transform_complex(value, value2)
            else:
                lvl = nest_lvl + 1
                nested_line = decode_plain(line, nest_lvl=lvl)
                nested_key = nested_line[0]
                key += nested_key
        plain_data.append([key, value, value2, state])
    return plain_data


def transform_compex(var1, var2):
    if isinstance(var1, dict):
        var1 = '[complex value]'
    elif isinstance(var2, dict):
        var2 = '[complex value]'
    return var1, var2

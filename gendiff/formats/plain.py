#!/usr/bin/env pyhton3

from gendiff.formats.default import sort_data
from gendiff.decoder import decode

statuses = {
    'added': "Property '{key}' was added with value: {value1}\n",
    'removed': "Property '{key}' was removed\n",
    'changed': "Property '{key}' was updated. From {value1} to {value2}\n"
}


def format_plain(data, nest_lvl=0):
    '''Formates raw diff in plain format'''
    sorted_data = sort_data(data)
    string_data = make_plain(sorted_data)
    return string_data[0:-1]


def make_plain(sorted_data, key=''):
    '''Formates data in plain format'''
    string_data = ''
    for node in sorted_data:
        new_key = transform_key(node, key)
        node_type, values = sorted_data[node]
        if node_type == 'unchanged':
            continue
        elif node_type == 'nested':
            new_value = sort_data(values)
            string_line = make_plain(new_value, key=new_key)
        else:
            string_line = make_plain_string(new_key, values, node_type)
        string_data = "".join([string_data, string_line])
    return string_data


def make_plain_string(old_key, values, node_type):
    '''Formates a string'''
    added_status = statuses[node_type]
    if isinstance(values, tuple):
        val1, val2 = values
        string_line = added_status.format(
            key=old_key,
            value1=trans_var(val1),
            value2=trans_var(val2)
        )
    if node_type == 'added':
        string_line = added_status.format(
            key=old_key,
            value1=trans_var(values)
        )
    elif node_type == 'removed':
        string_line = added_status.format(
            key=old_key
        )
    return string_line


def transform_complex(var):
    '''Replaces value with set string'''
    if isinstance(var, dict):
        var = '[complex value]'
    return var


def trans_var(var):
    '''Formates values'''
    var = transform_complex(var)
    if type(var) is int:
        return var
    else:
        var = decode(var)
    simple_vars = ['false', 'true', 'null',
                   '[complex value]']
    if var not in simple_vars:
        var = f"'{var}'"
    return var


def transform_key(old_key, key):
    '''Adds parent key to children'''
    if key != '':
        new_key = f'{key}.{old_key}'
    else:
        new_key = old_key
    return new_key

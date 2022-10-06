#!/usr/bin/env pyhton3

from gendiff.formats.default import sort_data
from gendiff.scripts.decoder import decode

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
        new_key = transform_key(old_key, key)
        if update == 'updated':
            continue
        elif nest == 'nested' and status == 'equal':
            new_value = sorted(value, key=lambda x: x[0])
            string_line = make_plain(new_value, key=new_key)
        elif status == 'equal':
            continue
        else:
            value, value2, status = transform_update(update, status, value)
            string_line = make_plain_string(new_key, value, value2, status)
        string_data += string_line
    return string_data
        

def transform_update(update, status, value):
    if isinstance(update, dict):
        value2 = update.get('updated')
        status = 'updated'
    else:
        value2 = None
    value = transform_complex(value)
    value2 = transform_complex(value2)
    return value, value2, status


def transform_complex(var):
    if isinstance(var, list):
        var = '[complex value]'
    return var


def make_plain_string(old_key, val1, val2, status):
    added_status = statuses[status]
    val1 = trans_var(val1)
    val2 = trans_var(val2)
    if status == 'added':
        string_line = added_status.format(
            key=old_key,
            value1=val1
        )
    elif status == 'removed':
        string_line = added_status.format(
            key=old_key
        )
    elif status == 'updated':
        string_line = added_status.format(
            key=old_key,
            value1=val1,
            value2=val2
        )
    return string_line


def trans_var(var):
    var = decode(var)
    simple_vars = ['false', 'true', 
        'null', '[complex value]'] 
    if var not in simple_vars:
        var = f"'{var}'"
    return var


def transform_key(old_key, key):
    if key != '':
        new_key = f'{key}.{old_key}'
    else:
        new_key = old_key
    return new_key

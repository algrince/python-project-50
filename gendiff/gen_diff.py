#!/usr/bin/env python3


from gendiff.parser import get_data
from gendiff.formats.formatter import formate


STATUS = {0: 'removed', 1: 'added', 2: 'unchanged', 3: 'changed', 4: 'nested'}


def separate_keys(data1, data2):
    '''Separates dictionary keys in types for their values
    (added, removed, unchanged, changed, nested)'''
    keys1 = set(data1)
    keys2 = set(data2)
    # Проверить, был ли ключ added или removed
    removed_keys = keys1 - keys2
    added_keys = keys2 - keys1
    print(added_keys, data2)
    # Найти unchanged, changed, вложенные вершины (nested)
    same_keys = keys1 & keys2
    unchanged_keys = {key for key in same_keys if data1[key] == data2[key]}
    changed_keys = set()
    nested_keys = set()
    for key in same_keys - unchanged_keys:
        if isinstance(data1[key], dict) or isinstance(data2[key], dict):
            nested_keys.add(key)
        else:
            changed_keys.add(key)
    keys = [removed_keys, added_keys, unchanged_keys, changed_keys, nested_keys]
    return keys


def format_nested(dic):
    '''Formates nested dictionaries if diff is not needed'''
    diffed_dict = dict()
    for key, value in dic.items():
        if isinstance(value, dict):
            value = format_nested(value)
        diffed_dict.update({key: [value, None, 'unchanged']})
    return diffed_dict


def diff_nested_values(key, value1, value2):
    '''Treates the special case of nested values'''
    if isinstance(value1, dict) and isinstance(value2, dict):
        diff = {key: [diff_dict(value1, value2), None, 'unchanged']}
    elif isinstance(value1, dict):
        diff = {key: [format_nested(value1), value2, 'changed']}
    else:
        diff = {key: [value1, format_nested(value2), 'changed']}
    return diff


def diff_dict(data1, data2):
    '''Generated diff between two dictionaries'''
    keys = separate_keys(data1, data2)
    diff = dict()
    for idx, key_type in enumerate(keys):
        for key in key_type:
            value1 = data1.get(key)
            value2 = data2.get(key)
            if idx != 4:
                diff.update({key: [value1, value2, STATUS[idx]]})
            else:
                nested_diff = diff_nested_values(key, value1, value2)
                diff.update(nested_diff)
    return diff


def generate_diff(file_path1, file_path2, output_format='stylish'):
    '''Generates the formatted diff of two data'''
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    diff = diff_dict(data1, data2)
    print(diff)
    formatted_diff = formate(diff, output_format)
    return formatted_diff

#!/usr/bin/env python3


from gendiff.parser import parse
from gendiff.formats.formatter import formate


CHANGES = (EQUAL, REMOVED, ADDED) = (
    'equal', 'removed', 'added')
STYLES = (NESTED, PLAIN) = ('nested', 'plain')


def diff_one(dict1):
    diff = []
    keys = dict1.keys()
    for key in keys:
            value1 = dict1[key]
            diff = evaluate(key, diff, **{'key3': value1})
    return diff


def evaluate(key, diff, **kwargs):
    print(diff)
    v1 = kwargs.get('key1', ' ')
    v2 = kwargs.get('key2', ' ')
    v3 = kwargs.get('key3', ' ')
    if v1 != ' ' and v2 != ' ':
        if isinstance(v1, dict) and isinstance(v2, dict):
            value = diff_dict(v1, v2)
            diff.append([key, value, EQUAL, NESTED])
        elif isinstance(v1, dict):
            value = diff_one(v1)
            diff.append([key, value, REMOVED, NESTED])
            diff.append([key, v2, ADDED, PLAIN])
        elif isinstance(v2, dict):
            value = diff_one(v2)
            diff.append([key, v1, REMOVED, PLAIN])
            diff.append([key, value, ADDED, NESTED])
        else:
            if v1 == v2:
                diff.append([key, v1, EQUAL, PLAIN])
            elif v1 != v2:
                diff.append([key, v1, REMOVED, PLAIN])
                diff.append([key, v2, ADDED, PLAIN])
    elif v1 != ' ':
        if isinstance(v1, dict):
            value = diff_one(v1)
            diff.append([key, value, REMOVED, NESTED])
        else:
            diff.append([key, v1, REMOVED, PLAIN])
    elif v2 != ' ':
        if isinstance(v2, dict):
            value = diff_one(v2)
            diff.append([key, value, ADDED, NESTED])
        else:
            diff.append([key, v2, ADDED, PLAIN])
    elif v3 != ' ':
        if isinstance(v3, dict):
            value = diff_one(v3)
            diff.append([key, value, EQUAL, NESTED])
        else: 
            diff.append([key, v3, EQUAL, PLAIN])
    return diff

def diff_dict(dict1, dict2):
    keys_d1 = dict1.keys()
    keys_d2 = dict2.keys()
    common = keys_d1 & keys_d2
    diff_in_1 = keys_d1 - keys_d2
    diff_in_2 = keys_d2 - keys_d1
    diff = []
    for key in common:
        value1 = dict1[key]
        value2 = dict2[key]
        diff = evaluate(key, diff, **{'key1' : value1, 'key2' : value2})
    for key in diff_in_1:
        value1 = dict1[key]
        diff = evaluate(key, diff, **{'key1' : value1})
    for key in diff_in_2:
        value2 = dict2[key]
        diff = evaluate(key, diff, **{'key2': value2})
    return diff


def generate_diff(file_path1, file_path2):
    data1 = parse(file_path1)
    data2 = parse(file_path2)
    diff = diff_dict(data1, data2)
    formatted_diff = formate(diff)
    return formatted_diff

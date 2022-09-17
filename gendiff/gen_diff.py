#!/usr/bin/env python3


from gendiff.parser import parse
from gendiff.scripts.decoder import decode


def items_to_keys(items):
    keys = set()
    for item in items:
        keys.add(item[0])
    return keys


def diff_keys(dict1, dict2):
    items_d1 = dict1.items()
    items_d2 = dict2.items()
    common = items_to_keys(items_d1 & items_d2)
    diff_in_1 = items_to_keys(items_d1 - items_d2)
    diff_in_2 = items_to_keys(items_d2 - items_d1)
    return common, diff_in_1, diff_in_2


def generate_diff(file_path1, file_path2):
    f1 = parse(file_path1)
    f2 = parse(file_path2)
    common, diff1, diff2 = diff_keys(f1, f2)
    keys_list = list(f1.keys() | f2.keys())
    keys_list.sort()
    diff = '{\n'
    for key in keys_list:
        if key in common:
            diff = diff + f'    {key}: {decode(f1[key])}\n'
        if key in diff1:
            diff = diff + f'  - {key}: {decode(f1[key])}\n'
        if key in diff2:
            diff = diff + f'  + {key}: {decode(f2[key])}\n'
    diff = diff + '}\n'
    return diff

#!/usr/bin/env python3


from gendiff.parser import parse
from gendiff.formats.formatter import formate


CHANGES = (EQUAL, CHANGED, REMOVED, ADDED, NESTED) = (
    'equal', 'changed', 'removed', 'added', 'nested'
)
FILE_NUMBERS = (NM, FILE1, FILE2) = (0, 1, 2)


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
        if isinstance(value1, dict) and isinstance(value2, dict):
            value = diff_dict(value1, value2)
            diff.append([key, value, NESTED, NM])
        elif value1 == value2:
            diff.append([key, value1, EQUAL, NM])
        else:
            diff.append([key, value1, REMOVED, FILE1])
            diff.append([key, value2, ADDED, FILE2])
    for key in diff_in_1:
        diff.append([key, dict1[key], REMOVED, NM])
    for key in diff_in_2:
        diff.append([key, dict2[key], ADDED, NM])
    return diff


def generate_diff(file_path1, file_path2):
    data1 = parse(file_path1)
    data2 = parse(file_path2)
    diff = diff_dict(data1, data2)
    formatted_diff = formate(diff)
    return formatted_diff

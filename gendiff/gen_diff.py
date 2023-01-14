#!/usr/bin/env python3


from gendiff.parser import get_data
from gendiff.formats.formatter import formate


def diff_dict(  # noqa: C901
        data1, data2):
    keys1 = set(data1)
    keys2 = set(data2)
    keys = keys1 | keys2
    diff = dict()
    for key in keys:
        if key in keys1 and key in keys2:
            value1 = data1[key]
            value2 = data2[key]
            if value1 == value2:
                diff.update({key: ['unchanged', value1]})
            elif isinstance(value1, dict) and isinstance(value2, dict):
                diff.update({key: ['nested', diff_dict(value1, value2)]})
            else:
                diff.update({key: ['changed', (value1, value2)]})
        elif key in keys1:
            value1 = data1[key]
            diff.update({key: ['removed', value1]})
        elif key in keys2:
            value2 = data2[key]
            diff.update({key: ['added', value2]})
    return diff


def generate_diff(file_path1, file_path2, output_format='stylish'):
    '''Generates the formatted diff of two data'''
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    diff = diff_dict(data1, data2)
    formatted_diff = formate(diff, output_format)
    return formatted_diff

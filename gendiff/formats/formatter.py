#!/usr/bin/env python3


from gendiff.formats.default import formate_default
from gendiff.formats.stylish import formate_stylish


def formate(diff):
    for line in diff:
        if line[2] == 'nested':
            return formate_type(diff, style='stylish')
    return formate_type(diff)



def formate_type(diff, style='default'):
    if style == 'default':
        formatted_diff = formate_default(diff)
    if style == 'stylish':
        formatted_diff = formate_stylish(diff)
    return formatted_diff

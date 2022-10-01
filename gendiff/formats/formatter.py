#!/usr/bin/env python3


from gendiff.formats.default import formate_default
from gendiff.formats.stylish import formate_stylish
from gendiff.formats.plain import formate_plain

#def formate(diff):
#    for line in diff:
#        if line[3] == 'nested':
#            return formate_type(diff, style='stylish')
#    return formate_type(diff)


def formate(diff, style):
    if style == 'json':
        formatted_diff = formate_default(diff)
    if style == 'stylish':
        formatted_diff = formate_stylish(diff)
    if style == 'plain':
        formatted_diff = formate_plain(diff)
    return formatted_diff

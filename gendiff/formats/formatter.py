#!/usr/bin/env python3


from gendiff.formats.json import formate_json
from gendiff.formats.stylish import formate_stylish
from gendiff.formats.plain import formate_plain


def formate(diff, style):
    if style == 'json':
        formatted_diff = formate_json(diff)
    if style == 'stylish':
        formatted_diff = formate_stylish(diff)
    if style == 'plain':
        formatted_diff = formate_plain(diff)
    return formatted_diff

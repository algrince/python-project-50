#!/usr/bin/env python3


from gendiff.formats.json import format_json
from gendiff.formats.stylish import format_stylish
from gendiff.formats.plain import format_plain


def format(diff, style):
    '''Chooses the format'''
    if style == 'json':
        formatted_diff = format_json(diff)
    if style == 'stylish':
        formatted_diff = format_stylish(diff)
    if style == 'plain':
        formatted_diff = format_plain(diff)
    return formatted_diff

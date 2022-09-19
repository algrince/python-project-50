#!/usr/bin/env python3


from gendiff.formats.default import formate_default


def formate(diff, style='default'):
    if style == 'default':
        formatted_diff = formate_default(diff)
    if style == 'stylish':
        pass
    return formatted_diff

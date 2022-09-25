#!/usr/bin/env python3


from json import dumps


def decode(value):
    if type(value) is str:
        return value
    else:
        return dumps(value)


'''def decode_dict(dictionary):
    data = []
    keys = dictionary.keys()
    for key in keys:
        value = dictionary[key]
        if isinstance(value, dict):
            pass
        diff.append([key, value, 'equal', 0])
    return diff
'''

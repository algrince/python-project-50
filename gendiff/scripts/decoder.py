#!/usr/bin/env python3


from json import dumps


def decode(value):
    if type(value) is str:
        return value
    else:
        return dumps(value)

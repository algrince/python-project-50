#!/usr/bin/env python3

from json import dumps
from gendiff.formats.default import sort_data


def formate_json(data, nest_lvl=0):
    '''Formates data with json format'''
    json_data = dumps(data, indent=4)
    print(json_data)
    return json_data

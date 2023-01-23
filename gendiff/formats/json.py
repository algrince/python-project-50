#!/usr/bin/env python3

from json import dumps


def format_json(data, nest_lvl=0):
    '''Formates data with json format'''
    json_data = dumps(data, indent=4, sort_keys=True)
    return json_data

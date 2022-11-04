#!/usr/bin/env python3

from json import dumps
from gendiff.formats.default import sort_data


def formate_json(data, nest_lvl=0):
    '''Formates data with json format'''
    dict_data = make_dict(data)
    json_data = dumps(dict_data, indent=4)
    return json_data


def make_dict(data):
    '''Makes a dict out of raw diff'''
    dict_data = {}
    sorted_data = sort_data(data)
    for line in sorted_data:
        key, value, status, nest, update = line
        if update == 'updated':
            continue
        elif nest == 'nested':
            value = make_dict(value)
        if isinstance(update, dict):
            value2 = update.get('updated')
            dict_line = {key: {'removed': value,
                               'added': value2}}
        elif status == 'equal':
            dict_line = {key: value}
        else:
            dict_line = {key: {status: value}}
        dict_data.update(dict_line)
    return dict_data

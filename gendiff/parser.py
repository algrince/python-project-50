#!/usr/bin/env python3


from json import load as json_load
from yaml import safe_load as yaml_load
from os.path import splitext


def get_format(file_path):
    '''Gets formats of the file'''
    file_ext = splitext(file_path)[1]
    return file_ext.lstrip('.')


def parse(file_path):
    '''Opens the file'''
    if get_format(file_path) == 'json':
        with open(file_path) as files:
            return json_load(files)
    elif get_format(file_path) in ('yaml', 'yml'):
        with open(file_path) as files:
            return yaml_load(files)

#!usr/bin/env python3


'''Default format for result representation '''

from gendiff.decoder import decode


signs = {'equal': '  ', 'removed': '- ', 'added': '+ '}


def sort_data(data):
    '''Sorts data'''
    keys = list(data.keys())
    keys.sort()
    sort_dict = {key: data[key] for key in keys}
    return sort_dict


def make_formate(sort_dict, nest_lvl=0):
    '''Formates data as default'''
    string_diff = '{\n'
    for line in sort_dict:
        string_diff += make_line(line, space_count=nest_lvl + 2)
    ending_space = ' ' * nest_lvl + '}'
    string_diff += ending_space
    return string_diff


def make_line(line, formatter=' ', space_count=2):
    '''Formates line for default presentation'''
    key, value, state, nest, update = line
    new_string = '{}{}{}: {}\n'
    string_line = new_string.format(
        formatter * space_count,
        signs[state],
        decode(key),
        decode(value))
    return string_line


def formate_default(data):
    '''Formates data as default'''
    sort_dict = sort_data(data)
    string_diff = make_formate(sort_dict)
    return string_diff

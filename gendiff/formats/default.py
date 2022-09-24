#!usr/bin/env python3


'''Default format for result representation '''

from gendiff.scripts.decoder import decode


signs = {'equal': '  ', 'removed': '- ', 'added': '+ '}


def sort_data(data):
    sort_dict = sorted(data, key=lambda x: (x[0], x[3]))
    return sort_dict


def make_formate(sort_dict, nest_lvl):
    string_diff = '{\n'
    for line in sort_dict:
        string_diff += make_line(line, space_count=nest_lvl+2)
    string_diff += '}\n'
    return string_diff


def make_line(line, formatter=' ', space_count=2):
    key, value, state, n_file = line
    new_string = '{}{}{}: {}\n'
    string_line = new_string.format(
        formatter * space_count,
        signs[state],
        decode(key),
        decode(value)
        )
    return string_line


def formate_default(data):
    sort_dict = sort_data(data)
    string_diff = make_formate(sort_dict)
    return string_diff

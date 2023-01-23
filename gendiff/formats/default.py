#!usr/bin/env python3


'''Default format for result representation '''

from gendiff.decoder import decode


signs = {'unchanged': '  ', 'nested': '  ', 'removed': '- ', 'added': '+ '}


def sort_data(data):
    '''Sorts data'''
    keys = list(data.keys())
    keys.sort()
    sort_dict = {key: data[key] for key in keys}
    return sort_dict


def transform_dict(var, space_count):
    count = space_count
    string_diff = '{\n'
    if isinstance(var, dict):
        for node in var:
            if isinstance(var[node], dict):
                var[node] = transform_dict(var[node], count + 4)
            line = {node: ['unchanged', var[node]]}
            string_line = make_line(line, space_count=count + 4)
            string_diff = "".join([string_diff, string_line])
        ending_space = ' ' * (count + 2) + '}'
        string_diff = "".join([string_diff, ending_space])
        return string_diff
    return var


def make_formate(sort_dict, nest_lvl=0):
    '''Formates data as default'''
    string_diff = '{\n'
    for node in sort_dict:
        line = {node: sort_dict[node]}
        string_line = make_line(line, space_count=nest_lvl + 2)
        string_diff = "".join([string_diff, string_line])
    ending_space = ' ' * nest_lvl + '}'
    string_diff = "".join([string_diff, ending_space])
    return string_diff


def make_line(node, formatter=' ', space_count=2):
    '''Formates line for default presentation'''
    key = list(node.keys())[0]
    node_type, values = node[key]
    count = space_count
    if node_type == 'changed':
        value1 = transform_dict(values[0], count)
        value2 = transform_dict(values[1], count)
        string_line = make_line(
            {key: ['removed', value1]}, space_count=count
        ) + make_line(
            {key: ['added', value2]}, space_count=count
        )
    else:
        value = transform_dict(values, count)
        new_string = '{}{}{}: {}\n'
        string_line = new_string.format(
            formatter * space_count,
            signs[node_type],
            decode(key),
            decode(value))
    return string_line


def format_default(data):
    '''Formates data as default'''
    sort_dict = sort_data(data)
    string_diff = make_formate(sort_dict)
    return string_diff

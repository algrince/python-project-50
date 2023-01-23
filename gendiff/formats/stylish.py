#!usr/bin/env python3

from gendiff.decoder import decode

signs = {'unchanged': '  ', 'nested': '  ', 'removed': '- ', 'added': '+ '}


def format_stylish(data, nest_lvl=0):
    '''Fomates raw diff in stylish format'''
    for node in data:
        info = data[node]
        node_type, values = info
        if node_type == 'nested':
            level = nest_lvl + 4
            values = format_stylish(values, nest_lvl=level)
            data[node] = [node_type, values]
    string_data = make_stylish_representation(data, nest_lvl)
    return string_data


def make_stylish_dict(var, space_count):
    '''Formates dictionary in stylish representation'''
    count = space_count
    string_diff = '{\n'
    if isinstance(var, dict):
        for node in var:
            if isinstance(var[node], dict):
                var[node] = make_stylish_dict(var[node], count + 4)
            line = {node: ['unchanged', var[node]]}
            string_line = make_line(line, space_count=count + 4)
            string_diff = "".join([string_diff, string_line])
        ending_space = ' ' * (count + 2) + '}'
        string_diff = "".join([string_diff, ending_space])
        return string_diff
    return var


def make_stylish_representation(data, nest_lvl=0):
    '''Formates data as stylish and fills it with lined diff'''
    string_diff = '{\n'
    for node in data:
        line = {node: data[node]}
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
        value1 = make_stylish_dict(values[0], count)
        value2 = make_stylish_dict(values[1], count)
        string_line = make_line(
            {key: ['removed', value1]}, space_count=count
        ) + make_line(
            {key: ['added', value2]}, space_count=count
        )
    else:
        value = make_stylish_dict(values, count)
        new_string = '{}{}{}: {}\n'
        string_line = new_string.format(
            formatter * space_count,
            signs[node_type],
            decode(key),
            decode(value))
    return string_line

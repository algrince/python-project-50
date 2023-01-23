#!usr/bin/env python3

from gendiff.decoder import decode

signs = {'unchanged': '  ', 'nested': '  ', 'removed': '- ', 'added': '+ '}


def format_diff_to_stylish(data, nest_lvl=0):
    '''Fomates raw diff in stylish format'''
    for node in data:
        info = data[node]
        node_type, values = info
        if node_type == 'nested':
            level = nest_lvl + 1
            values = format_diff_to_stylish(values, nest_lvl=level)
            data[node] = [node_type, values]
    string_data = make_stylish_represent(data, nest_lvl)
    return string_data


def make_stylish_dict(var, nest_lvl):
    '''Formates dictionary in stylish representation'''
    space_count = trans_lvl_to_spaces(nest_lvl)
    count = nest_lvl
    string_diff = '{\n'
    if isinstance(var, dict):
        for node in var:
            if isinstance(var[node], dict):
                var[node] = make_stylish_dict(var[node], nest_lvl + 1)
            line = {node: ['unchanged', var[node]]}
            string_line = make_line_from_node(line, nest_lvl=count + 1)
            string_diff = "".join([string_diff, string_line])
        ending_space = ' ' * (space_count + 2) + '}'
        string_diff = "".join([string_diff, ending_space])
        return string_diff
    return var


def make_stylish_represent(data, nest_lvl=0):
    '''Formates data as stylish and fills it with lined diff'''
    space_count = trans_lvl_to_spaces(nest_lvl)
    string_diff = '{\n'
    for node in data:
        line = {node: data[node]}
        string_line = make_line_from_node(line, nest_lvl=nest_lvl)
        string_diff = "".join([string_diff, string_line])
    ending_space = ' ' * (space_count - 2) + '}'
    string_diff = "".join([string_diff, ending_space])
    return string_diff


def make_line_from_node(node, formatter=' ', nest_lvl=0):
    '''Formates line for default presentation'''
    space_count = trans_lvl_to_spaces(nest_lvl)
    key = list(node.keys())[0]
    node_type, values = node[key]
    count = nest_lvl
    if node_type == 'changed':
        value1 = make_stylish_dict(values[0], count)
        value2 = make_stylish_dict(values[1], count)
        string_line = make_line_from_node(
            {key: ['removed', value1]}, nest_lvl=count
        ) + make_line_from_node(
            {key: ['added', value2]}, nest_lvl=count
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


def trans_lvl_to_spaces(nest_lvl):
    if nest_lvl == 0:
        space_count = 2
    else:
        space_count = 2 + nest_lvl * 4
    return space_count

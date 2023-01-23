#!usr/bin/env python3


from gendiff.formats.default import make_formate

signs = {'equal': '  ', 'removed': '- ', 'added': '+ ', 'nested': '  '}


def format_stylish(data, nest_lvl=0):
    '''Fomates raw diff in stylish format'''
    for node in data:
        info = data[node]
        node_type, values = info
        if node_type == 'nested':
            level = nest_lvl + 4
            values = format_stylish(values, nest_lvl=level)
            data[node] = [node_type, values]
    string_data = make_formate(data, nest_lvl)
    return string_data

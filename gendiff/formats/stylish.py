#!usr/bin/env python3


from gendiff.formats.default import sort_data, make_formate

signs = {'equal': '  ', 'removed': '- ', 'added': '+ ', 'nested': '  '}


def format_stylish(data, nest_lvl=0):
    '''Fomates raw diff in stylish format'''
    sort_dict = sort_data(data)
    for node in sort_dict:
        info = sort_dict[node]
        node_type, values = info
        if node_type == 'nested':
            level = nest_lvl + 4
            values = format_stylish(values, nest_lvl=level)
            sort_dict[node] = [node_type, values]
    string_data = make_formate(sort_dict, nest_lvl)
    return string_data

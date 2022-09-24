#!usr/bin/env python3


from gendiff.scripts.decoder import decode
from gendiff.formats.default import sort_data, make_formate, make_line

signs = {'equal': '  ', 'removed': '- ', 'added': '+ ', 'nested': '  '}


def formate_stylish(data, nest_lvl=0):
    if isinstance(data[0], list):
        sort_dict = sort_data(data)
        for line in sort_dict:
            if line[2] == 'nested':
                nest_lvl += 4 
                line[1] = formate_stylish(line[1], nest_lvl)
                line[2] = 'equal'
        string_data = make_formate(sort_dict, nest_lvl)
    else:
        string_data = '{\n' + make_line(data, space_count=nest_lvl+2) + '}\n'
    return string_data

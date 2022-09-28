#!usr/bin/env python3


from gendiff.scripts.decoder import decode
from gendiff.formats.default import sort_data, make_formate, make_line

signs = {'equal': '  ', 'removed': '- ', 'added': '+ ', 'nested': '  '}


def formate_stylish(data, nest_lvl=0):
    sort_dict = sort_data(data)
    for line in sort_dict:
        if line[3] == 'nested':
            level = nest_lvl + 4
            line[1] = formate_stylish(line[1], nest_lvl=level)
    string_data = make_formate(sort_dict, nest_lvl) 
    return string_data

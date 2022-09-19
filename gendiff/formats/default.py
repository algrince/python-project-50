#!usr/bin/env python3


'''Default format for result representation '''

from gendiff.scripts.decoder import decode


signs = {'equal': '  ', 'removed': '- ', 'added': '+ '}


def formate_default(data, formatter=' ', space_count=2):
    sort_dict = sorted(data, key=lambda x: (x[0], x[3]))
    string_diff = '{\n'
    for line in sort_dict:
        key, value, state, n_file = line
        new_string = '{}{}{}: {}\n'
        string_diff += new_string.format(
            formatter * space_count,
            signs[state],
            decode(key),
            decode(value)
        )
    string_diff += '}\n'
    return string_diff

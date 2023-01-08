#!/usr/bin/env python3


from gendiff.parser import get_data
from gendiff.formats.formatter import formate


CHANGES = (EQUAL, REMOVED, ADDED, UPDATED, NO_UPD) = (
    'equal', 'removed', 'added', 'updated', 'not updated')
STYLES = (NESTED, PLAIN) = ('nested', 'plain')


def detect_nest(nest):
    '''Returns style in function of nest vlaue'''
    return NESTED if nest is True else PLAIN


def evaluate(  # noqa: C901
        key, diff, **kwargs):
    '''Evaluates if values are nested'''
    v1 = kwargs.get('key1', ' ')
    v2 = kwargs.get('key2', ' ')
    v3 = kwargs.get('key3', ' ')
    if v1 != ' ' and v2 != ' ':
        if isinstance(v1, dict) and isinstance(v2, dict):
            value = diff_dict(v1, v2)
            diff.append([key, value, EQUAL, detect_nest(nest=True), NO_UPD])
        elif isinstance(v1, dict) or isinstance(v2, dict):
            diff = evaluate_vars(v1, v2, key, diff)
        else:
            if v1 == v2:
                diff.append([key, v1, EQUAL, PLAIN, NO_UPD])
            elif v1 != v2:
                diff = evaluate_update(v1, v2, key, diff)
    elif v1 != ' ':
        diff = evaluate_var(v1, key, REMOVED, diff)
    elif v2 != ' ':
        diff = evaluate_var(v2, key, ADDED, diff)
    elif v3 != ' ':
        diff = evaluate_var(v3, key, EQUAL, diff)
    return diff


def evaluate_update(
    var1, var2,
    key, diff,
    nest1=False, nest2=False
):
    '''Formes diff for updated data'''
    diff.append([key, var1, REMOVED,
                detect_nest(nest1),
                {UPDATED: var2}])
    diff.append([key, var2, ADDED,
                detect_nest(nest2),
                UPDATED])
    return diff


def evaluate_var(var, key, state, diff):
    '''Generates evaluate var-type response for one var'''
    if isinstance(var, dict):
        value = diff_one(var)
        diff.append([key, value, state, NESTED, NO_UPD])
    else:
        diff.append([key, var, state, PLAIN, NO_UPD])
    return diff


def evaluate_vars(var1, var2, key, diff):
    '''Generates diff-type response for two vars when one is nested'''
    if isinstance(var1, dict):
        value = diff_one(var1)
        diff = evaluate_update(value, var2, key, diff, nest1=True)
    elif isinstance(var2, dict):
        value = diff_one(var2)
        diff = evaluate_update(var1, value, key, diff, nest2=True)
    return diff


def diff_dict(dict1, dict2):
    '''Extracts keys from the dictionaries in 3 groups and generates diff'''
    keys_d1 = dict1.keys()
    keys_d2 = dict2.keys()
    common = keys_d1 & keys_d2
    diff_in_1 = keys_d1 - keys_d2
    diff_in_2 = keys_d2 - keys_d1
    diff = []
    for key in common:
        value1 = dict1[key]
        value2 = dict2[key]
        diff = evaluate(key, diff, **{'key1': value1, 'key2': value2})
    for key in diff_in_1:
        value1 = dict1[key]
        diff = evaluate(key, diff, **{'key1': value1})
    for key in diff_in_2:
        value2 = dict2[key]
        diff = evaluate(key, diff, **{'key2': value2})
    return diff


def diff_one(dict1):
    '''Generates diff-type response for one dictionary'''
    diff = []
    keys = dict1.keys()
    for key in keys:
        value1 = dict1[key]
        diff = evaluate(key, diff, **{'key3': value1})
    return diff


def generate_diff(file_path1, file_path2, output_format='stylish'):
    '''Generates the formatted diff of two data'''
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    diff = diff_dict(data1, data2)
    formatted_diff = formate(diff, output_format)
    return formatted_diff

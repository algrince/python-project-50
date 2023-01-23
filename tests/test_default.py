#!usr/bin/env python3


from gendiff.formats.default import (
    transform_dict, make_line, make_formate
)
from gendiff.formats.plain import sort_data
from gendiff.decoder import decode


CHANGED = {'change_key': ['changed', ['value1', 'value2']]}
ADDED = {'add_key': ['added', 'add_val']}
REMOVED = {'remove_key': ['removed', 'rmv_val']}
UNCHANGED = {'key': ['unchanged', 'value']}


def test_decode():
    assert 'patata' == decode('patata')
    assert 'null' == decode(None)
    assert 'false' == decode(False)
    assert 'true' == decode(True)
    assert '12' == decode(12)


def test_transform_dict():
    nested_var = {'key5': 'var5'}
    simple_var = 'var6'

    exp_nested_var = '{\n      key5: var5\n  }'
    exp_simple_var = simple_var

    assert exp_simple_var == transform_dict(simple_var, 2)
    assert exp_nested_var == transform_dict(nested_var, 0)


def test_make_formate():
    data = {**CHANGED, **ADDED, **REMOVED, **UNCHANGED}
    sorted_data = sort_data(data)
    expected_data = '{\n  + add_key: add_val\n  - change_key: value1\n  + change_key: value2\n    key: value\n  - remove_key: rmv_val\n}'  # noqa: E501

    assert expected_data == make_formate(sorted_data)


def test_make_line():
    nested = {'nested_key': ['nested', {'key2': 'value'}]}
    formated = {'key': ['unchanged', 'value']}

    exp_changed = '  - change_key: value1\n  + change_key: value2\n'
    exp_added = '  + add_key: add_val\n'
    exp_removed = '  - remove_key: rmv_val\n'
    exp_unchanged = '    key: value\n'
    exp_nested = '    nested_key: {\n        key2: value\n    }\n'
    exp_formated = '1111  key: value\n'

    assert exp_changed == make_line(CHANGED)
    assert exp_added == make_line(ADDED)
    assert exp_removed == make_line(REMOVED)
    assert exp_unchanged == make_line(UNCHANGED)
    assert exp_nested == make_line(nested)
    assert exp_formated == make_line(formated, formatter='1', space_count=4)

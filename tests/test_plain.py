#!usr/bin/env python3

from gendiff.formats.plain import (
    transform_complex, trans_var, transform_key,
    make_plain_represent, sort_data
)


def test_trans_complex():
    complex_var = {'key': 'value'}
    simple_var = 'value'
    assert '[complex value]' == transform_complex(complex_var)
    assert simple_var == transform_complex(simple_var)


def test_trans_var():
    assert 'false' == trans_var(False)
    assert 'null' == trans_var(None)
    assert 12 == trans_var(12)
    assert "'patata'" == trans_var('patata')


def test_trans_key():
    assert 'two.one' == transform_key('one', 'two')
    assert 'key' == transform_key('key', '')


def test_make_plain():
    nested = {'nested_key': [
        'nested', {
            'key2': ['removed', 'value'],
            'key3': ['added', 'var']
        }
    ]}
    unchanged = {'key': ['unchanged', 'value']}
    exp_nested = "Property 'nested_key.key2' was removed\nProperty 'nested_key.key3' was added with value: 'var'\n"  # noqa: E501

    assert '' == make_plain_represent(unchanged)
    assert exp_nested == make_plain_represent(nested)


def test_sort():
    expected = {'a': 1, 'b': 45, 'cad': 'patata', 'e': False, 'zet': True}
    to_sort = {'zet': True, 'cad': 'patata', 'b': 45, 'e': False, 'a': 1}

    assert expected == sort_data(to_sort)

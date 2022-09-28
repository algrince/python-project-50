#!usr/bin/env python3


from gendiff.gen_diff import generate_diff
from gendiff.gen_diff import diff_dict, diff_one, evaluate, state

alfa = {
    'key': 'value',
    'llave': 'valor',
    'kluc': 'znac',
}

beta = {
    'key': 'value',
    'llave': 'valor222',
    'zamok': '123'
}


def test_diff_dict():
    expected = [
        ['llave', 'valor', 'removed', 'plain'],
        ['llave', 'valor222', 'added', 'plain'],
        ['key', 'value', 'equal', 'plain'],
        ['kluc', 'znac', 'removed', 'plain'],
        ['zamok', '123', 'added', 'plain']
    ]
    assert expected == diff_dict(alfa, beta)


def test_diff_one():
    expected = [
        ['key', 'value', 'equal', 'plain'],
        ['llave', 'valor', 'equal', 'plain'],
        ['kluc', 'znac', 'equal', 'plain']
    ]
    assert expected == diff_one(alfa)


def test_evaluate_common():
    equal_line = [['common', 'value', 'equal', 'plain']]
    assert equal_line == evaluate('common', [], 
            **{'key1': 'value', 'key2': 'value'})
    diff_line = [['common', '12345', 'removed', 'plain'],
            ['common', '67890', 'added', 'plain']]
    assert diff_line == evaluate('common', [],
            **{'key1': '12345', 'key2': '67890'})


def test_evaluate_diff1():
    removed_line = [['diff_in_1', 'value1', 'removed', 'plain']]
    added_line = [['diff_in_2', 'value2', 'added', 'plain']]
    equal_line = [['key3', 'value3', 'equal', 'plain']]
    assert removed_line == evaluate('diff_in_1', [], **{'key1': 'value1'})
    assert added_line == evaluate('diff_in_2', [], **{'key2': 'value2'})
    assert equal_line == evaluate('key3', [], **{'key3': 'value3'})


def test_state():
    assert 'removed' == state(1)
    assert 'added' == state(2)
    assert 'equal' == state(3)
    
def test_format_json():
    with open('./tests/fixtures/expected.txt','r') as fixture:
        expected = fixture.read()
    assert expected == generate_diff(
            './tests/fixtures/file1.json', 
            './tests/fixtures/file2.json'
    )



def test_format_yaml():    
    with open('./tests/fixtures/expected.txt','r') as fixture:
        expected = fixture.read()
    assert expected == generate_diff(
            './tests/fixtures/file1.yaml', 
            './tests/fixtures/file2.yaml'
    )


def test_format_combined():
    with open('./tests/fixtures/expected.txt','r') as fixture:
        expected = fixture.read()
    assert expected == generate_diff(
            './tests/fixtures/file1.json', 
            './tests/fixtures/file2.yaml'
    )


def test_format_str_json():
    with open('./tests/fixtures/structured_expected.txt','r') as fixture:
        expected = fixture.read()
    assert expected == generate_diff(
            './tests/fixtures/structured_file1.json', 
            './tests/fixtures/structured_file2.json'
    )



def test_format_str_yaml():    
    with open('./tests/fixtures/structured_expected.txt','r') as fixture:
        expected = fixture.read()
    assert expected == generate_diff(
            './tests/fixtures/structured_file1.yaml', 
            './tests/fixtures/structured_file2.yaml'
    )


def test_format_str_combined():
    with open('./tests/fixtures/structured_expected.txt','r') as fixture:
        expected = fixture.read()
    assert expected == generate_diff(
            './tests/fixtures/structured_file1.json', 
            './tests/fixtures/structured_file2.yaml'
    )

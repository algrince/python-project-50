#!usr/bin/env python3


from gendiff.gen_diff import generate_diff
from gendiff.gen_diff import diff_dict

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
        ['key', 'value', 'equal', 0],
        ['llave', 'valor', 'removed', 1],
        ['llave', 'valor222', 'added', 2],
        ['kluc', 'znac', 'removed', 0],
        ['zamok', '123', 'added', 0]
    ]
    assert expected == diff_dict(alfa, beta)


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

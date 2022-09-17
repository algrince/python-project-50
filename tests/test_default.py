#!usr/bin/env python3


from gendiff.gen_diff import generate_diff


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

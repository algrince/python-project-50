#!usr/bin/env python3


from gendiff.gen_diff import generate_diff


def test_format():
    with open('tests/fixtures/expected.txt','r') as fixture:
        expected = fixture.read()
    assert expected == generate_diff(
            'tests/fixtures/file1.json', 
            'tests/fixtures/file2.json'
    )

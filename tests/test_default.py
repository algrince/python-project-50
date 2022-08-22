#!usr/bin/env python3


from gendiff.gen_diff import generate_diff


def test_format():
    with open('fixtures/expected.txt','r') as fixture:
        expected = fixture.read()
    assert expected == generate_diff(
            'fixtures/file1.json', 
            'fixtures/file2.json'
    )

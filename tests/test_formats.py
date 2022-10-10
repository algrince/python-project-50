#ª/usr/bin/env pyhton3


from gendiff.gen_diff import generate_diff


def test_stylish():
    with open('./tests/fixtures/structured_expected.txt', 'r') as fixture:
        expected = fixture.read()
    assert expected[0:-1] == generate_diff(
            './tests/fixtures/structured_file1.json',
            './tests/fixtures/structured_file2.json',
            output_format='stylish'
    )


def test_plain():
    with open('./tests/fixtures/plain_expected.txt', 'r') as fixture:
        expected = fixture.read()
    assert expected[0:-1] == generate_diff(
            './tests/fixtures/structured_file1.json',
            './tests/fixtures/structured_file2.json',
            output_format='plain'
    )


def test_json():
    with open('./tests/fixtures/json_expected.txt', 'r') as fixture:
        expected = fixture.read()
    assert expected[0:-1] == generate_diff(
            './tests/fixtures/structured_file1.json',
            './tests/fixtures/structured_file2.json',
            output_format='json'
    )

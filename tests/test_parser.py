from gendiff.parser import get_format, parse

file_path_json = '/home/User/file.json'
file_path_empty = '/home/User/'


def test_format():
    assert get_format(file_path_json) == 'json'
    assert get_format(file_path_empty) == ''


def test_parser_json():
    py_obj = parse('./tests/fixtures/file1.json')
    assert isinstance(py_obj, dict)


def test_parser_yaml():
    py_obj = parse('./tests/fixtures/file1.yaml')
    assert isinstance(py_obj, dict)

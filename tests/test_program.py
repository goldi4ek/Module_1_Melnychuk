import pytest
from main import FileChecker


@pytest.fixture()
def file_checker():
    return FileChecker()


def test_input(file_checker):
    result = file_checker.open_file("testinput.txt")
    assert result == ['hello', 'everyone']

import pytest
from main import FileChecker


@pytest.fixture()
def file_checker():
    return FileChecker()


def test_input(file_checker):
    result = file_checker.open_file("testinput.txt")
    assert result == ['hello', 'everyone']


def test_check_similar(file_checker):
    file1 = file_checker.open_file("testSimilarDifferenceFile1.txt")
    file2 = file_checker.open_file("testSimilarDifferenceFile2.txt")
    result = file_checker.check_similar(file1, file2)
    assert result == {"hello", "everyone", "guys"}


def test_check_different(file_checker):
    file1 = file_checker.open_file("testSimilarDifferenceFile1.txt")
    file2 = file_checker.open_file("testSimilarDifferenceFile2.txt")
    result = file_checker.check_different(file1, file2)
    assert result == {"me", "nobody", "love"}


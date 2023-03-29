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


@pytest.mark.parametrize('input_line, result_line', [("hello", {"hello"}),
                                                     ("buy", {"buy"}),
                                                     ("hay", {"hay"}),
                                                     ("dota2", {"dota2"})])
def test_check_similar_parametrize(file_checker, input_line, result_line):
    file_checker.wrote_file([input_line], "testCheckSimilarParametrize1")
    file_checker.wrote_file([input_line], "testCheckSimilarParametrize2")
    text1 = file_checker.open_file("testCheckSimilarParametrize1.txt")
    text2 = file_checker.open_file("testCheckSimilarParametrize2.txt")
    result = file_checker.check_similar(text1, text2)
    assert result == result_line

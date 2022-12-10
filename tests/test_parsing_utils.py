from pytest import raises as pytest_raises
from fifteen_puzzle.parsing_utils import load_from_file
from fifteen_puzzle.exceptions import NumbersOutOfRangeException, WrongRowInputException, \
    MissingGridSizeException
from os.path import join as os_path_join


def test_load_from_file_out_or_range_3x3():
    with pytest_raises(NumbersOutOfRangeException):
        load_from_file(os_path_join('.', 'tests', 'prepared_boards', 'input3.15sav'))


def test_load_from_file_wrong_row_input_4x4():
    with pytest_raises(WrongRowInputException):
        load_from_file(os_path_join('.', 'tests', 'prepared_boards', 'input5.15sav'))


def test_load_from_file_out_or_range_4x4():
    with pytest_raises(NumbersOutOfRangeException):
        load_from_file(os_path_join('.', 'tests', 'prepared_boards', 'input6.15sav'))


def test_load_from_file_missing_grid_size_4x4():
    with pytest_raises(MissingGridSizeException):
        load_from_file(os_path_join('.', 'tests', 'prepared_boards', 'input13.15sav'))

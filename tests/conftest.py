import pytest
from fifteen_puzzle.algo_utils import PuzzleNode


@pytest.fixture(scope='session')
def basic_invalid_3x3_state():
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    yield PuzzleNode(board=board, dimension=3, steps='')


@pytest.fixture(scope='session')
def target_4x4_state():
    board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]
    yield PuzzleNode(board=board, dimension=4, steps='')


@pytest.fixture(scope='session')
def two_moves_to_solve_4x4_state():
    board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 0, 12],
        [13, 14, 11, 15]
    ]
    yield PuzzleNode(board=board, dimension=4, steps='')

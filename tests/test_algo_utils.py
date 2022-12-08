from fifteen_puzzle.algo_utils import PuzzleNode
from fifteen_puzzle.algo_utils import find_coords_of_tile, \
    check_if_solvable, find_0_row, prepare_solved_board, \
    check_if_valid_numbers, check_if_numbers_dont_repeat, \
    calculate_manhattan_distance, calculate_hamming_distance, \
    evaluate_node_bf_strategy, evaluate_node_astar
from pytest import raises as pytest_raises
from fifteen_puzzle.exceptions import NoEmptySpaceFoundException


def test_finding_coords_of_tile(target_4x4_state):
    board = target_4x4_state.board
    assert (0, 2) == find_coords_of_tile(board, 3)


def test_if_solvable_board(two_moves_to_solve_4x4_state):
    assert check_if_solvable(two_moves_to_solve_4x4_state, 4)


def test_if_unsolvable_board():
    board = [
        [2, 1, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]
    node = PuzzleNode(board=board, dimension=4, steps='')
    assert not check_if_solvable(node, 4)


def test_find_0_row(two_moves_to_solve_4x4_state):
    board = two_moves_to_solve_4x4_state.board
    assert 2 == find_0_row(board)


def test_find_0_row_raises():
    board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 1]
    ]
    with pytest_raises(NoEmptySpaceFoundException):
        find_0_row(board)


def test_prepare_4x4_solved_board(target_4x4_state):
    assert target_4x4_state == prepare_solved_board(4)


def test_numbers_out_of_range():
    board = [
        [17, 1, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]
    assert not check_if_valid_numbers(board, 4)


def test_numbers_in_of_range():
    board = [
        [2, 1, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]
    assert check_if_valid_numbers(board, 4)


def test_if_numbers_do_not_repeat(target_4x4_state):
    board = target_4x4_state.board
    assert check_if_numbers_dont_repeat(board)


def test_if_numbers_do_repeat():
    board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 1]
    ]
    assert not check_if_numbers_dont_repeat(board)


def test_calculating_manhattan_distance(two_moves_to_solve_4x4_state, target_4x4_state):
    board = two_moves_to_solve_4x4_state.board
    solved_board = target_4x4_state.board
    assert 4 == calculate_manhattan_distance(board=board, solved_board=solved_board)


def test_calculating_hamming_distance(two_moves_to_solve_4x4_state):
    board = two_moves_to_solve_4x4_state.board
    assert 3 == calculate_hamming_distance(board=board)


def test_bf_strategy_evaluation_given_manhattan_heuristics(two_moves_to_solve_4x4_state, target_4x4_state):
    assert 4 == evaluate_node_bf_strategy(node=two_moves_to_solve_4x4_state,
                                          heuristics='manh', solved_state=target_4x4_state)


def test_bf_strategy_evaluation_given_hamming_heuristics(two_moves_to_solve_4x4_state, target_4x4_state):
    assert 3 == evaluate_node_bf_strategy(node=two_moves_to_solve_4x4_state,
                                          heuristics='hamm', solved_state=target_4x4_state)


def test_astar_evaluation_given_manhattan_heuristics(two_moves_to_solve_4x4_state, target_4x4_state):
    two_moves_to_solve_4x4_state.depth = 2
    assert 6 == evaluate_node_astar(node=two_moves_to_solve_4x4_state,
                                    heuristics='manh', solved_state=target_4x4_state)


def test_astar_evaluation_given_hamming_heuristics(two_moves_to_solve_4x4_state, target_4x4_state):
    two_moves_to_solve_4x4_state.depth = 2
    assert 5 == evaluate_node_astar(node=two_moves_to_solve_4x4_state,
                                    heuristics='hamm', solved_state=target_4x4_state)

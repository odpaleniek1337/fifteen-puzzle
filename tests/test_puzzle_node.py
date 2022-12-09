from fifteen_puzzle.algo_utils import PuzzleNode, ExtendedPuzzleNode


def test_if_two_3x3_puzzlenodes_with_same_board_are_equal():
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    node1 = PuzzleNode(board=board, dimension=3, steps='')
    node2 = PuzzleNode(board=board, dimension=3, steps='')
    assert node1 == node2


def test_if_two_3x3_puzzlenodes_have_the_same_hashes():
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    hash1 = ExtendedPuzzleNode(board=board, dimension=3, steps='')
    hash2 = ExtendedPuzzleNode(board=board, dimension=3, steps='')
    assert hash1 == hash2


def test_move_left(two_moves_to_solve_4x4_state):
    target_board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 12, 0],
        [13, 14, 11, 15]
    ]
    target_node = PuzzleNode(board=target_board, dimension=4, steps='')
    expected_node = two_moves_to_solve_4x4_state.move('L')
    assert target_node == expected_node


def test_move_right(two_moves_to_solve_4x4_state):
    target_board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 0, 10, 12],
        [13, 14, 11, 15]
    ]
    target_node = PuzzleNode(board=target_board, dimension=4, steps='')
    expected_node = two_moves_to_solve_4x4_state.move('R')
    assert target_node == expected_node


def test_move_up(two_moves_to_solve_4x4_state):
    target_board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 0, 15]
    ]
    target_node = PuzzleNode(board=target_board, dimension=4, steps='')
    expected_node = two_moves_to_solve_4x4_state.move('U')
    assert target_node == expected_node


def test_move_down(two_moves_to_solve_4x4_state):
    target_board = [
        [1, 2, 3, 4],
        [5, 6, 0, 8],
        [9, 10, 7, 12],
        [13, 14, 11, 15]
    ]
    target_node = PuzzleNode(board=target_board, dimension=4, steps='')
    expected_node = two_moves_to_solve_4x4_state.move('D')
    assert target_node == expected_node


def test_if_move_possible_true(target_4x4_state):
    assert target_4x4_state.move('R') is not None
    assert target_4x4_state.move('D') is not None


def test_if_move_possible_false(target_4x4_state):
    assert target_4x4_state.move('L') is None
    assert target_4x4_state.move('U') is None

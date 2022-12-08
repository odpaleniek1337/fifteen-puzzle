from fifteen_puzzle.algo_utils import PuzzleNode


def test_if_two_puzzlenodes_with_same_board_are_equal():
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    node1 = PuzzleNode(board=board, dimension=3, steps='')
    node2 = PuzzleNode(board=board, dimension=3, steps='')
    assert node1 == node2

from fifteen_puzzle.algo_utils import check_if_solvable, prepare_solved_node
from fifteen_puzzle.parsing_utils import load_from_file
from fifteen_puzzle.algorithms import BreadthFirstSearchAlgorithm
from os.path import join as os_path_join


def test_load_from_file_game_not_solvable_4x4():
    state, dimension = load_from_file(os_path_join('.', 'tests', 'prepared_boards', 'input1.15sav'))
    assert not check_if_solvable(state, dimension)


def test_solve_bfs_load_from_file_4x4():
    state, dimension = load_from_file(os_path_join('.', 'tests', 'prepared_boards', 'input9.15sav'))
    n, steps = BreadthFirstSearchAlgorithm().solve(state, prepare_solved_node(4), 'LRUD')
    assert 2 == n
    assert 'UL' == steps

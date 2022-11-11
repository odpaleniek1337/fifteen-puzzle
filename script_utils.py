from constants import *

from typing import Union
from argparse import ArgumentParser
from algorithms import PuzzleNode, check_if_valid_numbers, check_if_numbers_dont_repeat
from exceptions import CustomException, WrongGridSizeException, \
    MissingGridSizeException, WrongRowInputException, CannotMapToIntegerException, \
    NumbersOutOfRangeException, NumberRepetitionException

def parse_arguments() -> object:
    """
    """
    parser = ArgumentParser(
        description='Script tires to solve fifteen-puzzle game using algorithm given by the user.'
    )

    algorithms_choice = parser.add_mutually_exclusive_group()
    algorithms_choice.add_argument('-b', '--bfs', choices=ORDER_SEARCH_POSSIBILITIES, help='Breadth-first search')
    algorithms_choice.add_argument('-d', '--dfs', choices=ORDER_SEARCH_POSSIBILITIES, help='Depth-first search')
    algorithms_choice.add_argument('-i', '--idfs', choices=ORDER_SEARCH_POSSIBILITIES, help='Iterative deepenening DFS')
    algorithms_choice.add_argument('-f', '--bf', choices=HEURISTICS_IDS, help='Best-first strategy')
    algorithms_choice.add_argument('-a', '--astar', choices=HEURISTICS_IDS, help='A* strategy')
    algorithms_choice.add_argument('-s', '--sma', choices=HEURISTICS_IDS, help='SMA* strategy')
    algorithms_choice.add_argument('-e', '--display', help='Used to display previous games', action='store_true')

    parser.add_argument('-n', '--input_file', default='input.15sav')
    parser.add_argument('-o', '--output_file', default='output.15sav')

    return parser.parse_args()

def load_from_file(filename: str) -> Union[PuzzleNode, CustomException]:
    """
    Loads dimensions and board from file
    Adjusted for boards with square shape (3x3, 4x4 etc.)
    """
    grid = []
    with open(filename, 'r') as input_file:
        try:
            grid_size = list(map(int, input_file.readline().strip(' ').split()))
        except ValueError:
            raise CannotMapToIntegerException('Line: 0')
        try:
            if grid_size[0] != grid_size[1]:
                raise WrongGridSizeException
            if len(grid_size) != 2:
                raise MissingGridSizeException
        except IndexError:
            raise MissingGridSizeException

        for x in range(grid_size[0]):
            try:
                line = list(map(int, input_file.readline().strip(' ').split()))
            except ValueError:
                msg = f'Line: {x + 1}'
                raise CannotMapToIntegerException(msg)
            if len(line) != grid_size[1]:
                msg = f'Wrong row size - expected: {grid_size[1]} given: {len(line)}. Row: {x + 1}'
                raise WrongRowInputException(msg)
            grid.append(line)

    if not check_if_valid_numbers(board=grid, dimension=grid_size[0]):
        msg = f'Range: <0, {grid_size[0] ** 2 - 1}>'
        raise NumbersOutOfRangeException(msg)
    if not check_if_numbers_dont_repeat(board=grid):
        raise NumberRepetitionException
    
    root_puzzle = PuzzleNode(board=grid, dimension=grid_size[0])

    return root_puzzle, grid_size[0]
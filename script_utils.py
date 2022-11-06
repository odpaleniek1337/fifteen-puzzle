from constants import *

from argparse import ArgumentParser
from algorithms import PuzzleNode
from exceptions import WrongGridSizeException, MissingGridSizeException, \
    WrongRowInputException, CannotMapToIntegerException

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

def load_from_file(filename: str) -> PuzzleNode:
    """
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

    #check if valid numbers
    
    parent_puzzle = PuzzleNode(board=grid, parent='Root', grid_dimension=grid_size[0])

    return parent_puzzle
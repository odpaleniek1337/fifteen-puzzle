from constants import *

from argparse import ArgumentParser
from algorithms import PuzzleNode
from exceptions import WrongGridSize, MissingGridSize, WrongRowInput

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

def load_from_file(filename) -> PuzzleNode:
    """
    """
    grid = []
    with open(filename, 'r') as input_file:
        grid_size = input_file.readline().strip(' ').split()
        try:
            if grid_size[0] != grid_size[1]:
                raise WrongGridSize
            if grid_size.__len__() != 2:
                raise MissingGridSize
        except IndexError:
            raise MissingGridSize

        for x in range(int(grid_size[0])):
            line = input_file.readline().strip(' ').split()
            if line.__len__() != int(grid_size[1]):
                msg = f'Wrong row size - expected: {grid_size[1]} given: {line.__len__()}. Row: {x + 1}'
                raise WrongRowInput(msg)
            grid.append(line)

    parent_puzzle = PuzzleNode(grid, 'Root', grid_size[0])
    
    return parent_puzzle
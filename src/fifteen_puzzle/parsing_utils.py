import pickle
from fifteen_puzzle.constants import *  # noqa: F403
from io import TextIOWrapper
from argparse import ArgumentParser
from typing import Tuple, List
from fifteen_puzzle.algo_utils import PuzzleNode, check_if_valid_numbers, check_if_numbers_dont_repeat
from fifteen_puzzle.exceptions import WrongGridSizeException, \
    MissingGridSizeException, WrongRowInputException, CannotMapToIntegerException, \
    NumbersOutOfRangeException, NumberRepetitionException


def parse_arguments() -> object:
    """Parses given arguments by the user

    Returns:
        object: parsed arguments object
    """
    parser = ArgumentParser(
        description='Script tries to solve fifteen-puzzle game using algorithm given by the user.'
    )

    algorithms_choice = parser.add_mutually_exclusive_group()
    algorithms_choice.add_argument('-b', '--bfs', choices=ORDER_SEARCH_POSSIBILITIES,
                                   help='Breadth-first search')
    algorithms_choice.add_argument('-d', '--dfs', choices=ORDER_SEARCH_POSSIBILITIES,
                                   help='Depth-first search')
    algorithms_choice.add_argument('-i', '--idfs', choices=ORDER_SEARCH_POSSIBILITIES,
                                   help='Iterative deepenening DFS')
    algorithms_choice.add_argument('-f', '--bf', choices=HEURISTICS_IDS,
                                   help='Best-first strategy with 1-Manhattan Distance; 2-Hamming Distance')
    algorithms_choice.add_argument('-a', '--astar', choices=HEURISTICS_IDS,
                                   help='A* strategy with 1-Manhattan Distance; 2-Hamming Distance')

    parser.add_argument('-e', '--display', help='Used to display previous games', action='store_true')
    parser.add_argument('-n', '--input_file', help='Alternative to << any.15sav')
    parser.add_argument('-o', '--output_file', help='Alternative to >> any.15sav')

    return parser.parse_args()


def load_from_file(filename: str) -> Tuple[PuzzleNode, int]:
    """Loads grid from provided file

    Args:
        filename (str): filename

    Returns:
        Tuple[PuzzleNode, int]: (Starting state, dimension)
    """
    with open(filename, 'r') as input_file:
        grid, grid_dimension = read_input(input_file)

    return transform_board_to_state(grid, grid_dimension), grid_dimension


def load_from_input() -> Tuple[PuzzleNode, int]:
    """Loads grid from stdin

    Returns:
        Tuple[PuzzleNode, int]: (Starting state, dimension)
    """
    grid, grid_dimension = read_input()

    return transform_board_to_state(grid, grid_dimension), grid_dimension


def transform_board_to_state(board: List[List], dimension: int) -> PuzzleNode:
    """Transforms board to state

    Args:
        board (List[List]): starting board
        dimension (int): given dimension

    Returns:
        PuzzleNode: Starting state of the game
    """
    check_numbers_validity(grid=board, grid_dimension=dimension)
    root_puzzle = PuzzleNode(board=board, dimension=dimension, steps='')

    return root_puzzle


def check_numbers_validity(grid: List[List], grid_dimension: int) -> None:
    """Checks for basic validity of data

    Args:
        grid (List[List]): board of the game
        grid_dimension (int): dimension of the game

    Raises:
        NumbersOutOfRangeException: Numbers are out of range
        NumberRepetitionException: One of the number is repeated
    """
    if not check_if_valid_numbers(board=grid, dimension=grid_dimension):
        msg = f'Range: <0, {grid_dimension ** 2 - 1}>'
        raise NumbersOutOfRangeException(msg)
    if not check_if_numbers_dont_repeat(board=grid):
        raise NumberRepetitionException


def read_input(chosen_input: object = input) -> Tuple[PuzzleNode, int]:
    """Reads input from given source

    Args:
        chosen_input (object, optional): Provided stream. Defaults to input.

    Raises:
        CannotMapToIntegerException: Wrong types of input
        WrongGridSizeException: Wrong grid size e.g. 3x4
        MissingGridSizeException: User did not provide exactly 2 dimensions
        WrongRowInputException: Number of tiles differes from declared in certain row

    Returns:
        Tuple[Union[PuzzleNode, CustomException], int]:
        Either raises exception or creates starting state and dimension.
    """
    grid = []
    try:
        if isinstance(chosen_input, TextIOWrapper):
            grid_size = list(map(int, chosen_input.readline().strip(' ').split()))
        else:
            grid_size = list(map(int, chosen_input().split()))
    except ValueError:
        raise CannotMapToIntegerException('Line: 0')
    except EOFError:
        raise MissingGridSizeException('File is empty.')
    try:
        if grid_size[0] != grid_size[1]:
            raise WrongGridSizeException
        if len(grid_size) != 2:
            raise MissingGridSizeException
    except IndexError:
        raise MissingGridSizeException

    for x in range(grid_size[0]):
        try:
            if isinstance(chosen_input, TextIOWrapper):
                line = list(map(int, chosen_input.readline().strip(' ').split()))
            else:
                line = list(map(int, chosen_input().split()))
        except ValueError:
            msg = f'Line: {x + 1}'
            raise CannotMapToIntegerException(msg)
        if len(line) != grid_size[1]:
            msg = f'Wrong row size - expected: {grid_size[1]} given: {len(line)}. Row: {x + 1}'
            raise WrongRowInputException(msg)
        grid.append(line)

    return grid, grid_size[0]


def output_to_file(filename: str, solution_length: int, steps: str) -> None:
    """Outputs data to given file

    Args:
        filename (str): filename
        solution_length (int): length of found solution
        steps (str): steps in found solution
    """
    with open(filename, 'w', newline='') as output_file:
        output_file.write(f'{solution_length}, {steps}\n')


def serialize_objects(filename: str, objects: object) -> None:
    """Pickle serialization function

    Args:
        filename (str): filename
        objects (object): objects desired for serialization
    """
    with open(filename, 'wb') as output_file:
        pickle.dump(objects, output_file)


def deserialize_objects(filename: str) -> object:
    """Pickle deserialization function

    Args:
        filename (str): filename

    Returns:
        object: Deserialized object(s)
    """
    with open(filename, 'rb') as input_file:
        inputs = pickle.load(input_file)

    return inputs

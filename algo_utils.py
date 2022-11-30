from typing import List, Union, Tuple
from exceptions import NoEmptySpaceFoundException
from constants import MOVE_RIGHT, MOVE_DOWN, MOVE_LEFT, MOVE_UP

class PuzzleNode:
    """
    Base class for saving board state
    """
    def __init__(self, board: List[List], dimension: int, steps: str, depth: int = 0) -> None:
        self.board = board
        self.dimension = dimension
        self.depth = depth
        self.steps = '' + steps

    def __hash__(self) -> int:
        return hash(bytes(two_d_to_one_d(self.board)))

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, self.__class__):
            return NotImplemented
        return self.board == __o.board
    
    def __str__(self) -> str:
        str_board = ''
        for x in range(self.dimension):
            str_board += str(self.board[x]) + '\n'
        #return f'Depth: {self.depth}\n' + str_board
        return f'{str_board}'

    def _find_0_coords(self) -> Tuple[int, int]:
        """
        Returns coordinates of 0 in 0-indexed tuple (row, column)
        """
        for i, row in enumerate(self.board):
            if 0 in row:
                for j, num in enumerate(row):
                    if not num:
                        return (i, j)

    def _check_if_move_possible(self, position: tuple, move: tuple) -> bool:
        if position[0] + move[0] < 0 or position[0] + move[0] >= self.dimension:
            return False
        elif position[1] + move[1] < 0 or position[1] + move[1] >= self.dimension:
            return False
        return True

    def _swap_0(self, position_0: tuple, move: tuple) -> List[List]:
        board_copy = [[y for y in x] for x in self.board]
        board_copy[position_0[0]][position_0[1]], board_copy[position_0[0] + move[0]][position_0[1] + move[1]] = \
            board_copy[position_0[0] + move[0]][position_0[1] + move[1]], board_copy[position_0[0]][position_0[1]]
        return board_copy

    def _right(self, position_0: tuple, move: tuple) -> 'PuzzleNode':
        swapped_board = self._swap_0(position_0, move)
        return PuzzleNode(swapped_board, self.dimension, self.steps + 'R', self.depth + 1)
    
    def _down(self, position_0: tuple, move: tuple) -> 'PuzzleNode':
        swapped_board = self._swap_0(position_0, move)
        return PuzzleNode(swapped_board, self.dimension, self.steps + 'D', self.depth + 1)

    def _left(self, position_0: tuple, move: tuple) -> 'PuzzleNode':
        swapped_board = self._swap_0(position_0, move)
        return PuzzleNode(swapped_board, self.dimension, self.steps + 'L', self.depth + 1)

    def _up(self, position_0: tuple, move: tuple) -> 'PuzzleNode':
        swapped_board = self._swap_0(position_0, move)
        return PuzzleNode(swapped_board, self.dimension, self.steps + 'U', self.depth + 1)

    def _move(self, direction: str) -> Union['PuzzleNode', None]:
        position = self._find_0_coords()
        if direction == 'R' and self._check_if_move_possible(position, MOVE_RIGHT):
            return self._right(position, MOVE_RIGHT)
        elif direction == 'D' and self._check_if_move_possible(position, MOVE_DOWN):
            return self._down(position, MOVE_DOWN)
        elif direction == 'L' and self._check_if_move_possible(position, MOVE_LEFT):
            return self._left(position, MOVE_LEFT)
        elif direction == 'U' and self._check_if_move_possible(position, MOVE_UP):
            return self._up(position, MOVE_UP)
        return None

def check_if_solvable(start_node: PuzzleNode, dimension: int) -> int:
    """
    Checks if read board is solvable

    - dimension odd
        - inversions even -> solvable
        - inversions odd -> not solvable
    - dimension even
        - 0 position from lower boundary even 
            - inversions odd -> solvable
            - inversions even -> not solvable
        - 0 position from lower boundary odd 
            - inversions even -> solvable
            - inversions odd -> not solvable
    """
    inversions = get_inversion_count(board=start_node.board)
    if dimension % 2:
        return 0 if inversions % 2 else 1

    position = find_0_row(board=start_node.board)
    if position % 2:
        return 0 if inversions % 2 else 1

    return inversions % 2

def find_0_row(board: List[List]) -> int:
    """
    Finds first row in which 0 was found in given board
    """
    for i, row in enumerate(reversed(board), 1):
        if 0 in row:
            return i
    raise NoEmptySpaceFoundException

def get_inversion_count(board: List[List]) -> int:
    """
    Finds bubble sort inversions needed to give expected result
    """
    array_1d = [a for arr in board for a in arr]
    inversion_count = 0
    for i, num1 in enumerate(array_1d):
        for num2 in array_1d[i + 1:]:
            if (num2 and num1 and num1 > num2):
                inversion_count += 1
    return inversion_count

def prepare_solved_board(dimension: int) -> PuzzleNode:
    """
    Prepares solved board to store it globally
    """
    solved = [[dimension * j + x + 1 for x in range(dimension)] for j in range(dimension)]
    solved[dimension - 1][dimension - 1] = 0
    return PuzzleNode(solved, 4, '', 0)

def check_if_valid_numbers(board: List[List], dimension) -> bool:
    for row in board:
        for col in row:
            if col < 0 or col > (dimension ** 2) - 1:
                return False
    return True

def check_if_numbers_dont_repeat(board: List[List]) -> bool:
    transformed_board = [x for row in board for x in row]
    if not len(transformed_board) == len(set(transformed_board)):
        return False
    return True

def two_d_to_one_d(board: List[List]) -> List:
    return [x for row in board for x in row]

def evaluate_node(node: PuzzleNode) -> int:
    g, h = 0, 0

    return g + h
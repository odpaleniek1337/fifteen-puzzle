from dataclasses import dataclass, field
from typing import List, Union, Tuple
from fifteen_puzzle.constants import MOVE_RIGHT, MOVE_DOWN, MOVE_LEFT, MOVE_UP
from fifteen_puzzle.exceptions import NoEmptySpaceFoundException


class PuzzleNode:
    """Base class representing state for saving and manipulating game
    """
    def __init__(self, board: List[List], dimension: int, steps: str,
                 depth: int = 0) -> None:
        self.board = board
        self.dimension = dimension
        self.depth = depth
        self.steps = '' + steps

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, self.__class__):
            return NotImplemented
        return self.board == __o.board

    def __str__(self) -> str:
        str_board = ''
        for x in range(self.dimension):
            str_board += str(self.board[x]) + '\n'
        return f'{str_board}'

    def _check_if_move_possible(self, position: tuple, move: tuple) -> bool:
        """Checks if given move is possible

        Args:
            position (tuple): 2d coordinates of zero
            move (tuple): 2d coordinates of move e.g (0, 1) or (-1, 0)

        Returns:
            bool: indicator if it is possible to perform move
        """
        if position[0] + move[0] < 0 or position[0] + move[0] >= self.dimension:
            return False
        elif position[1] + move[1] < 0 or position[1] + move[1] >= self.dimension:
            return False
        return True

    def _swap_0(self, position_0: tuple, move: tuple) -> List[List]:
        """Prepares the 2d board for the move

        Args:
            position_0 (tuple): 2d coordinates of zero
            move (tuple): 2d coordinates of move e.g (0, 1) or (-1, 0)

        Returns:
            List[List]: newly created 2d board
        """
        board_copy = [[y for y in x] for x in self.board]

        board_copy[position_0[0]][position_0[1]], \
            board_copy[position_0[0] + move[0]][position_0[1] + move[1]] = \
            board_copy[position_0[0] + move[0]][position_0[1] + move[1]], \
            board_copy[position_0[0]][position_0[1]]
        return board_copy

    def _right(self, position_0: tuple) -> 'PuzzleNode':
        """Creates new state after move to the right

        Args:
            position_0 (tuple): 2d coordinates of zero

        Returns:
            PuzzleNode: newly created 2d state after (0, -1) move
        """
        swapped_board = self._swap_0(position_0, MOVE_RIGHT)
        return self.__class__(swapped_board, self.dimension, self.steps + 'R', self.depth + 1)

    def _down(self, position_0: tuple) -> 'PuzzleNode':
        """Creates new state after move down

        Args:
            position_0 (tuple): 2d coordinates of zero

        Returns:
            PuzzleNode: newly created 2d state after (-1, 0) move
        """
        swapped_board = self._swap_0(position_0, MOVE_DOWN)
        return self.__class__(swapped_board, self.dimension, self.steps + 'D', self.depth + 1)

    def _left(self, position_0: tuple) -> 'PuzzleNode':
        """Creates new state after move to the left

        Args:
            position_0 (tuple): 2d coordinates of zero

        Returns:
            PuzzleNode: newly created 2d state after (0, 1) move
        """
        swapped_board = self._swap_0(position_0, MOVE_LEFT)
        return self.__class__(swapped_board, self.dimension, self.steps + 'L', self.depth + 1)

    def _up(self, position_0: tuple) -> 'PuzzleNode':
        """Creates new state after move up

        Args:
            position_0 (tuple): 2d coordinates of zero

        Returns:
            PuzzleNode: newly created 2d state after (1, 0) move
        """
        swapped_board = self._swap_0(position_0, MOVE_UP)
        return self.__class__(swapped_board, self.dimension, self.steps + 'U', self.depth + 1)

    def move(self, direction: str) -> Union['PuzzleNode', None]:
        """Creates new state after move given direction (R,D,L,U)

        Returns:
            Union[PuzzleNode, None]: newly created 2d state
        """
        position = find_coords_of_tile(self.board, 0)
        if direction == 'R' and self._check_if_move_possible(position, MOVE_RIGHT):
            return self._right(position)
        elif direction == 'D' and self._check_if_move_possible(position, MOVE_DOWN):
            return self._down(position)
        elif direction == 'L' and self._check_if_move_possible(position, MOVE_LEFT):
            return self._left(position)
        elif direction == 'U' and self._check_if_move_possible(position, MOVE_UP):
            return self._up(position)
        return None


class ExtendedPuzzleNode(PuzzleNode):
    def __init__(self, board: List[List], dimension: int, steps: str,
                 depth: int = 0, heuristic_value: int = 0) -> None:
        super().__init__(board, dimension, steps, depth)
        self.heuristic_value = heuristic_value

    def __hash__(self) -> int:
        return hash(bytes(two_d_to_one_d(self.board)))

    def __lt__(self, __o: 'ExtendedPuzzleNode') -> bool:
        return self.heuristic_value < __o.heuristic_value


def find_coords_of_tile(board: List[List], tile: int) -> Tuple[int, int]:
    """Returns coordinates of number in 0-indexed tuple (row, column)

    Args:
        board (List[List]): given board
        tile (int): searched number

    Returns:
        Tuple[int, int]: 2d coordinates
    """
    for i, row in enumerate(board):
        if tile in row:
            return (i, row.index(tile))


def check_if_solvable(start_node: PuzzleNode, dimension: int) -> int:
    """Checks if read state is solvable

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

    Args:
        start_node (PuzzleNode): given state
        dimension (int): dimension index (must be a square e.g 3x3)

    Returns:
        int: (0, 1) value
    """
    inversions = get_inversion_count(board=start_node.board)
    if dimension % 2:
        return 0 if inversions % 2 else 1

    position = find_0_row(board=start_node.board)
    if position % 2:
        return 0 if inversions % 2 else 1

    return inversions % 2


def find_0_row(board: List[List]) -> int:
    """Finds first row in which 0 was found in reversed given board

    Args:
        board (List[List]): given board

    Raises:
        NoEmptySpaceFoundException: No zero in the puzzle

    Returns:
        int: 1-indexed row number
    """
    for i, row in enumerate(reversed(board), 1):
        if 0 in row:
            return i
    raise NoEmptySpaceFoundException


def get_inversion_count(board: List[List]) -> int:
    """Finds bubble sort inversions needed to give expected result

    Args:
        board (List[List]): given board

    Returns:
        int: number of inversions
    """
    array_1d = [a for arr in board for a in arr]
    inversion_count = 0
    for i, num1 in enumerate(array_1d):
        for num2 in array_1d[i + 1:]:
            if (num2 and num1 and num1 > num2):
                inversion_count += 1
    return inversion_count


def prepare_solved_node(dimension: int) -> PuzzleNode:
    """Prepares solved state to store it globally

    Args:
        dimension (int): dimension index (must be a square e.g 3x3)

    Returns:
        PuzzleNode: target game state
    """
    solved = [[dimension * j + x + 1 for x in range(dimension)] for j in range(dimension)]
    solved[dimension - 1][dimension - 1] = 0
    return PuzzleNode(solved, dimension, '', 0)


def check_if_valid_numbers(board: List[List], dimension: int) -> bool:
    """Performs a safe check if all numbers are in range <0, dimension ** 2 - 1>

    Args:
        board (List[List]): read board
        dimension (int): dimension index (must be a square e.g 3x3)

    Returns:
        bool: indicator if board is valid
    """
    for row in board:
        for value in row:
            if value < 0 or value > (dimension ** 2) - 1:
                return False
    return True


def check_if_numbers_dont_repeat(board: List[List]) -> bool:
    """Performs a safe check if there is no duplicate in board

    Args:
        board (List[List]): read board

    Returns:
        bool: indicator if board is valid
    """
    transformed_board = [x for row in board for x in row]
    if not len(transformed_board) == len(set(transformed_board)):
        return False
    return True


def two_d_to_one_d(board: List[List]) -> List:
    """Util function to quickly transpose 2d to 1d

    Args:
        board (List[List]): given board

    Returns:
        List: board in 1d
    """
    return [x for row in board for x in row]


def calculate_manhattan_distance(board: List[List], solved_board: List[List]) -> int:
    """Calculates manhattan distance between boards in 2d

    Args:
        board (List[List]): given board
        solved_board (List[List]): target board

    Returns:
        int: manhattan distance
    """
    distance = 0
    numbers_in_1d = two_d_to_one_d(board)
    for number in numbers_in_1d:
        unsolved_coords, solved_coords = \
            find_coords_of_tile(board, number), find_coords_of_tile(solved_board, number)
        distance += abs(unsolved_coords[0] - solved_coords[0])
        distance += abs(unsolved_coords[1] - solved_coords[1])
    return distance


def calculate_hamming_distance(board: List[List]) -> int:
    """Calculates hamming distance between boards

    Args:
        board (List[List]): given board

    Returns:
        int: hamming distance
    """
    distance = 0
    numbers_in_1d = two_d_to_one_d(board)
    for i, number in enumerate(numbers_in_1d, 1):
        distance += 1 if number != i or i == 16 and not number else 0
    return distance


def evaluate_node_astar(node: ExtendedPuzzleNode, heuristics: str,
                        solved_state: ExtendedPuzzleNode) -> int:
    """Evaluates node based on depth and chosen heuristic

    Args:
        node (ExtendedPuzzleNode): given state
        heuristics (str): heuristic type (manh, hamm)
        solved_state (ExtendedPuzzleNode): target state

    Returns:
        int: astar evaluation
    """
    if heuristics == 'manh':
        return node.depth + calculate_manhattan_distance(node.board, solved_state.board)
    elif heuristics == 'hamm':
        return node.depth + calculate_hamming_distance(node.board)
    return NotImplemented


def evaluate_node_bf_strategy(node: ExtendedPuzzleNode, heuristics: str,
                              solved_state: ExtendedPuzzleNode) -> int:
    """Evaluates node based on chosen heuristic

    Args:
        node (ExtendedPuzzleNode): given state
        heuristics (str): heuristic type (manh, hamm)
        solved_state (ExtendedPuzzleNode): target state

    Returns:
        int: greedy-best-first-strategy evaluation
    """
    if heuristics == 'manh':
        return calculate_manhattan_distance(node.board, solved_state.board)
    elif heuristics == 'hamm':
        return calculate_hamming_distance(node.board)
    return NotImplemented


@dataclass(order=True)
class PrioritizedPuzzleNode:
    """Class wrapping representing state and priority - the lower the better
    """
    priority: int
    item: ExtendedPuzzleNode = field(compare=False)

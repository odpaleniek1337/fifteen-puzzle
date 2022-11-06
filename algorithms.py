from typing import List, Union
from exceptions import NoEmptySpaceFoundException

class PuzzleNode:
    """
    Base class for saving board state
    """
    def __init__(self, board: List[List], parent: Union[str, 'PuzzleNode'], grid_dimension: int) -> None:
        self.board = board
        self.parent = parent
        self.grid_dimension = grid_dimension

    def _if_solved(self, grid):
        if self.board == grid:
            return True
        return False

def check_if_solvable(start_node: PuzzleNode) -> int:
    """
    Checks if read board is solvable

    - dimension odd
        - inversions even -> solvable
        - inversions odd -> not solvable
    - dimension even
        - 0 position even 
            - inversions odd -> solvable
            - inversions even -> not solvable
        - 0 position odd 
            - inversions even -> solvable
            - inversions odd -> not solvable
    """
    inversions = get_inversion_count(board=start_node.board)
    if start_node.grid_dimension % 2:
        return 0 if inversions % 2 else 1

    position = find_0(board=start_node.board)
    if position % 2:
        return 0 if inversions % 2 else 1

    return inversions % 2

def find_0(board: List[List]) -> int:
    """
    Finds first 0 found in given board
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

def bfs():
    pass

def dfs():
    pass

def idfs():
    pass

def bf():
    pass

def astar():
    pass

def smastar():
    pass


def check_if_solvable():
    pass


class PuzzleNode:
    def __init__(self, board, parent, grid_dimension=None) -> None:
        self.board = board
        self.parent = parent
        self.grid_dimension = grid_dimension

    def _if_solved(self, grid):
        if self.board == grid:
            return True
        return False

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
from typing import List
from abc import ABC, abstractmethod
from algo_utils import PuzzleNode

class BaseAlgorithm(ABC):
    @abstractmethod
    def __init__(self) -> 'BaseAlgorithm':
        self.max_depth = 0
        self.seen_nodes = set()
        self.steps = []

    @abstractmethod
    def solve(self, start_node: PuzzleNode) -> List[str]:
        pass

class BreadthFirstSearchAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode) -> List[str]:
        if start_node == solved_board:
            return []
        return NotImplemented
        #return self.steps

class DepthFirstSearchAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode) -> List[str]:
        if start_node == solved_board:
            return []
        return NotImplemented
        #return self.steps

class IterativeDeepeningDepthFirstSearchAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode) -> List[str]:
        if start_node == solved_board:
            return []
        return NotImplemented
        #return self.steps

class BestFirstSearchAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode) -> List[str]:
        if start_node == solved_board:
            return []
        return NotImplemented
        #return self.steps

class AStarAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode) -> List[str]:
        if start_node == solved_board:
            return []
        return NotImplemented
        #return self.steps

class SMAStarAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode) -> List[str]:
        if start_node == solved_board:
            return []
        return NotImplemented
        #return self.steps
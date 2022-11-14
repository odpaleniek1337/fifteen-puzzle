from typing import List
from abc import ABC, abstractmethod
from algo_utils import PuzzleNode
from random import shuffle
from collections import deque

class BaseAlgorithm(ABC):
    @abstractmethod
    def __init__(self) -> 'BaseAlgorithm':
        self.max_depth = 20
        self.seen_nodes = set()
        self.neighbours = deque()

    @abstractmethod
    def solve(self, start_node: PuzzleNode, **kwargs) -> List[str]:
        pass

class BreadthFirstSearchAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, order: List[str]) -> List[str]:
        if start_node == solved_board:
            return start_node.steps

        shuffle_flag = order[0] == 'R'
        self.neighbours.append(start_node)

        while self.neighbours:
            current_node = self.neighbours.popleft()
            #print(f'Current amount of neighbours: {len(self.neighbours)}. Total seen nodes: {len(self.seen_nodes)}')
            self.seen_nodes.add(hash(start_node))
            if not shuffle_flag:
                for direction in order:
                    new_node = current_node._move(direction=direction)
                    if new_node == solved_board:
                        return new_node
                    if new_node and hash(new_node) not in self.seen_nodes:
                        self.neighbours.append(new_node)
                        self.seen_nodes.add(hash(new_node))
            else:
                shuffle(order)
                for direction in order:
                    new_node = current_node._move(direction=direction)
                    if new_node == solved_board:
                        return new_node
                    if new_node and hash(new_node) not in self.seen_nodes:
                        self.neighbours.append(new_node)
                        self.seen_nodes.add(hash(new_node))
            if current_node.depth == self.max_depth:
                return -1, len(self.seen_nodes), len(self.neighbours) #FIX LATER

class DepthFirstSearchAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, order: List[str]) -> List[str]:
        if start_node == solved_board:
            return []
        return NotImplemented
        #return self.steps

class IterativeDeepeningDepthFirstSearchAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, order: List[str]) -> List[str]:
        if start_node == solved_board:
            return []
        return NotImplemented
        #return self.steps

class BestFirstSearchAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, choice: int) -> List[str]:
        if start_node == solved_board:
            return []
        return NotImplemented
        #return self.steps

class AStarAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, choice: int) -> List[str]:
        if start_node == solved_board:
            return []
        return NotImplemented
        #return self.steps

class SMAStarAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, choice: int) -> List[str]:
        if start_node == solved_board:
            return []
        return NotImplemented
        #return self.steps
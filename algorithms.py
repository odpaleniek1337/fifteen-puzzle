from typing import List, Tuple
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
    def solve(self, start_node: PuzzleNode, **kwargs) -> Tuple:
        pass

class BreadthFirstSearchAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, order: List[str]) -> Tuple[int, int, int]:
        if start_node == solved_board:
            return 0, start_node.steps
        
        self.seen_nodes.add(hash(start_node))
        self.neighbours.append(start_node)
        shuffle_flag = order[0] == 'R'

        while self.neighbours:
            current_node = self.neighbours.popleft()
            if current_node.depth >= self.max_depth:
                return -1, len(self.seen_nodes), len(self.neighbours) + 1 #2,3 args to be deleted
            self.seen_nodes.add(hash(start_node))
            if shuffle_flag:
                shuffle(order)
            for direction in order:
                new_node = current_node._move(direction=direction)
                if new_node and new_node == solved_board:
                    return len(new_node.steps), new_node.steps, len(self.seen_nodes)
                if new_node and hash(new_node) not in self.seen_nodes:
                    self.neighbours.append(new_node)
                    self.seen_nodes.add(hash(new_node))

class DepthFirstSearchAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, order: List[str]) -> Tuple[int, int, int]:
        if start_node == solved_board:
            return 0, start_node.steps
        
        self.seen_nodes.add(hash(start_node))
        self.neighbours.append(start_node)
        shuffle_flag = order[0] == 'R'

        while self.neighbours:
            current_node = self.neighbours.pop()
            self.seen_nodes.add(hash(start_node))
            if current_node.depth < self.max_depth:
                if shuffle_flag:
                    shuffle(order)
                for direction in order:
                    new_node = current_node._move(direction=direction)
                    if new_node and new_node == solved_board:
                        return len(new_node.steps), new_node.steps, len(self.seen_nodes)
                    if new_node and hash(new_node) not in self.seen_nodes:
                        self.neighbours.append(new_node)
                        self.seen_nodes.add(hash(new_node))

        if not self.neighbours:
            return -1, len(self.seen_nodes), len(self.neighbours) + 1 #2,3 args to be deleted

class IterativeDeepeningDepthFirstSearchAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()
        self.start_depth = 5

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, order: List[str]) -> Tuple[int, int, int]:
        if start_node == solved_board:
            return 0, start_node.steps
        
        self.seen_nodes.add(hash(start_node))
        self.neighbours.append(start_node)
        shuffle_flag = order[0] == 'R'

        while self.neighbours:
            current_node = self.neighbours.pop()
            self.seen_nodes.add(hash(start_node))
            if current_node.depth < self.max_depth:
                if shuffle_flag:
                    shuffle(order)
                for direction in order:
                    new_node = current_node._move(direction=direction)
                    if new_node and new_node == solved_board:
                        return len(new_node.steps), new_node.steps, len(self.seen_nodes)
                    if new_node and hash(new_node) not in self.seen_nodes:
                        self.neighbours.append(new_node)
                        self.seen_nodes.add(hash(new_node))

        if not self.neighbours:
            return -1, len(self.seen_nodes), len(self.neighbours) + 1 #2,3 args to be deleted

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
from abc import ABC, abstractmethod
from random import shuffle
from collections import deque
from queue import PriorityQueue
from typing import List, Tuple
from fifteen_puzzle.algo_utils import PuzzleNode, ExtendedPuzzleNode, \
    PrioritizedPuzzleNode, evaluate_node_astar, evaluate_node_bf_strategy
from fifteen_puzzle.constants import BASIC_ORDER


class BaseAlgorithm(ABC):
    """Base class for algorithms
    """
    @abstractmethod
    def __init__(self) -> 'BaseAlgorithm':
        self.max_depth = 20
        self.seen_nodes = set()
        self.neighbours = deque()

    @abstractmethod
    def solve(self, start_node: PuzzleNode, **kwargs) -> Tuple[int, str]:
        """Solve state using class's algorithm

        Args:
            start_node (PuzzleNode): starting state

        Returns:
            Tuple: (number of steps to solve, steps)
        """
        pass


class BreadthFirstSearchAlgorithm(BaseAlgorithm):
    """BFS Algorithm class

    Args:
        BaseAlgorithm (_type_): Base algorithm class
    """
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_node: PuzzleNode, order: List[str]) -> Tuple[int, str]:
        if start_node == solved_node:
            return 0, start_node.steps

        self.neighbours.append(start_node)
        shuffle_flag = order[0] == 'R'
        while self.neighbours:
            current_node = self.neighbours.popleft()
            if current_node == solved_node:
                return len(current_node.steps), current_node.steps
            if current_node.depth < self.max_depth:
                if shuffle_flag:
                    shuffle(order)
                for direction in order:
                    new_node = current_node.move(direction=direction)
                    if new_node:
                        self.neighbours.append(new_node)
        if not self.neighbours:
            return -1, ''


class DepthFirstSearchAlgorithm(BaseAlgorithm):
    """DFS Algorithm class

    Args:
        BaseAlgorithm (_type_): Base algorithm class
    """
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_node: PuzzleNode, order: List[str]) -> Tuple[int, str]:
        if start_node == solved_node:
            return 0, start_node.steps

        self.neighbours.append(start_node)
        shuffle_flag = order[0] == 'R'
        while self.neighbours:
            current_node = self.neighbours.pop()
            if current_node == solved_node:
                return len(current_node.steps), current_node.steps
            if current_node.depth < self.max_depth:
                if shuffle_flag:
                    shuffle(order)
                new_nodes = []
                for direction in order:
                    new_node = current_node.move(direction=direction)
                    if new_node:
                        new_nodes.append(new_node)
                if new_nodes:
                    self.neighbours.extend(reversed(new_nodes))
                    new_nodes = []
        if not self.neighbours:
            return -1, ''


class IterativeDeepeningDepthFirstSearchAlgorithm(BaseAlgorithm):
    """IDDFS Algorithm class

    Args:
        BaseAlgorithm (_type_): Base algorithm class
    """
    def __init__(self) -> None:
        super().__init__()
        self.current_depth = 5

    def solve(self, start_node: PuzzleNode, solved_node: PuzzleNode, order: List[str]) -> Tuple[int, str]:
        if start_node == solved_node:
            return 0, start_node.steps

        self.neighbours.append(start_node)
        shuffle_flag = order[0] == 'R'
        while True:
            while self.neighbours:
                current_node = self.neighbours.pop()
                if current_node == solved_node:
                    return len(current_node.steps), current_node.steps
                if current_node.depth < self.current_depth:
                    if shuffle_flag:
                        shuffle(order)
                    new_nodes = []
                    for direction in order:
                        new_node = current_node.move(direction=direction)
                        new_nodes.append(new_node) if new_node else None
                    if new_nodes:
                        self.neighbours.extend(reversed(new_nodes))
                        new_nodes = []

            if self.current_depth < self.max_depth:
                self.current_depth += 1
                self.neighbours.append(start_node)
            else:
                return -1, ''


class BestFirstSearchAlgorithm(BaseAlgorithm):
    """Best-First-Search-Strategy Algorithm class

    Args:
        BaseAlgorithm (_type_): Base algorithm class
    """
    def __init__(self) -> None:
        super().__init__()
        self.neighbours = PriorityQueue()

    def solve(self, start_node: ExtendedPuzzleNode, solved_node: PuzzleNode, heuristics: str) -> List[str]:
        if start_node == solved_node:
            return 0, start_node.steps
        self.neighbours.put_nowait(PrioritizedPuzzleNode(0, start_node))
        self.seen_nodes.add(hash(start_node))

        while self.neighbours:
            current_node = self.neighbours.get_nowait().item
            if current_node == solved_node:
                return len(current_node.steps), current_node.steps
            for direction in BASIC_ORDER:
                new_node = current_node.move(direction=direction)
                if new_node and hash(new_node) not in self.seen_nodes:
                    self.neighbours.put_nowait(
                        PrioritizedPuzzleNode(
                            evaluate_node_bf_strategy(new_node, heuristics, solved_node),
                            new_node)
                    )
                    self.seen_nodes.add(hash(new_node))
        return -1, ''


class AStarAlgorithm(BaseAlgorithm):
    """A* Algorithm class

    Args:
        BaseAlgorithm (_type_): Base algorithm class
    """
    def __init__(self) -> None:
        super().__init__()
        self.neighbours = PriorityQueue()

    def solve(self, start_node: ExtendedPuzzleNode, solved_node: PuzzleNode, heuristics: str) -> List[str]:
        if start_node == solved_node:
            return 0, start_node.steps
        self.neighbours.put_nowait(PrioritizedPuzzleNode(0, start_node))
        self.seen_nodes.add(hash(start_node))

        while self.neighbours:
            current_node = self.neighbours.get_nowait().item
            if current_node == solved_node:
                return len(current_node.steps), current_node.steps
            for direction in BASIC_ORDER:
                new_node = current_node.move(direction=direction)
                if new_node and hash(new_node) not in self.seen_nodes:
                    self.neighbours.put_nowait(
                        PrioritizedPuzzleNode(
                            evaluate_node_astar(new_node, heuristics, solved_node),
                            new_node)
                    )
                    self.seen_nodes.add(hash(new_node))
        return -1, ''

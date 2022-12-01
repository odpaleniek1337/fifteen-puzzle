from typing import List, Tuple
from abc import ABC, abstractmethod
from algo_utils import PuzzleNode, PrioritizedPuzzleNode, evaluate_node_astar, evaluate_node_bf_strategy
from random import shuffle
from collections import deque
from constants import BASIC_ORDER
from queue import PriorityQueue

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

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, order: List[str]) -> Tuple[int, str]:
        if start_node == solved_board:
            return 0, start_node.steps
        
        self.neighbours.append(start_node)
        self.seen_nodes.add(hash(start_node))
        shuffle_flag = order[0] == 'R'
        while self.neighbours:
            current_node = self.neighbours.popleft()
            if current_node.depth >= self.max_depth:
                return -1, '\n'
            if shuffle_flag:
                shuffle(order)
            for direction in order:
                new_node = current_node._move(direction=direction)
                if new_node and new_node == solved_board:
                    return len(new_node.steps), new_node.steps
                if new_node and hash(new_node) not in self.seen_nodes:
                    self.neighbours.append(new_node)
                    self.seen_nodes.add(hash(new_node))

class DepthFirstSearchAlgorithm(BaseAlgorithm): 
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, order: List[str]) -> Tuple[int, str]:
        if start_node == solved_board:
            return 0, start_node.steps

        self.neighbours.append(start_node)
        self.seen_nodes.add(hash(start_node))
        shuffle_flag = order[0] == 'R'
        max_neighbours = 0
        while self.neighbours:
            current_node = self.neighbours.pop()
            if current_node == solved_board:
                return len(current_node.steps), current_node.steps
            if shuffle_flag:
                shuffle(order)
            for direction in order:
                new_node = current_node._move(direction=direction)
                if new_node and new_node not in self.seen_nodes and new_node.depth <= self.max_depth:
                    self.neighbours.append(new_node)
                    self.seen_nodes.add(hash(new_node))

        if not self.neighbours:
            return -1, '\n'

class IterativeDeepeningDepthFirstSearchAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()
        self.current_depth = 5

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, order: List[str]) -> Tuple[int, str]:
        if start_node == solved_board:
            return 0, start_node.steps
        
        self.neighbours.append(start_node)
        self.seen_nodes.add(hash(start_node))
        shuffle_flag = order[0] == 'R'
        while True:
            lowest_depth_neighbours = deque()
            while self.neighbours:
                current_node = self.neighbours.pop()
                if shuffle_flag:
                    shuffle(order)
                if current_node.depth < self.current_depth:
                    for direction in order:
                        new_node = current_node._move(direction=direction)
                        if new_node and new_node == solved_board:
                            return len(new_node.steps), new_node.steps
                        if new_node and hash(new_node) not in self.seen_nodes:
                            self.seen_nodes.add(hash(new_node))
                            if current_node.depth == self.current_depth - 1:
                                lowest_depth_neighbours.append(new_node)
                            else:
                                self.neighbours.append(new_node)

            if not self.neighbours and self.current_depth < self.max_depth:
                self.current_depth += 1
                self.neighbours, lowest_depth_neighbours = lowest_depth_neighbours, deque()
            else:
                return -1, '\n'

class BestFirstSearchAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()
        self.neighbours = PriorityQueue()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, heuristics: str) -> List[str]:
        if start_node == solved_board:
            return 0, start_node.steps
        self.neighbours.put_nowait(PrioritizedPuzzleNode(0, start_node))
        self.seen_nodes.add(hash(start_node))

        while self.neighbours:
            current_node = self.neighbours.get_nowait().item
            for direction in BASIC_ORDER:
                new_node = current_node._move(direction=direction)
                if new_node and new_node == solved_board:
                    return len(new_node.steps), new_node.steps
                if new_node and hash(new_node) not in self.seen_nodes:
                    self.neighbours.put_nowait(PrioritizedPuzzleNode(evaluate_node_bf_strategy(new_node, heuristics, solved_board), new_node))
                    self.seen_nodes.add(hash(new_node))
        return -1, '\n'

class AStarAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()
        self.neighbours = PriorityQueue()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, heuristics: str) -> List[str]:
        if start_node == solved_board:
            return 0, start_node.steps
        self.neighbours.put_nowait(PrioritizedPuzzleNode(0, start_node))
        self.seen_nodes.add(hash(start_node))

        while self.neighbours:
            current_node = self.neighbours.get_nowait().item
            for direction in BASIC_ORDER:
                new_node = current_node._move(direction=direction)
                if new_node and new_node == solved_board:
                    return len(new_node.steps), new_node.steps
                if new_node and hash(new_node) not in self.seen_nodes:
                    self.neighbours.put_nowait(PrioritizedPuzzleNode(evaluate_node_astar(new_node, heuristics, solved_board), new_node))
                    self.seen_nodes.add(hash(new_node))
        return -1, '\n'

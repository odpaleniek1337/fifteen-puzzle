from typing import List, Tuple
from abc import ABC, abstractmethod
from algo_utils import PuzzleNode, evaluate_node
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

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, order: List[str]) -> Tuple[int, str]:
        if start_node == solved_board:
            return 0, start_node.steps
        
        self.seen_nodes.add(hash(start_node))
        self.neighbours.append(start_node)
        shuffle_flag = order[0] == 'R'

        while self.neighbours:
            current_node = self.neighbours.popleft()
            if current_node.depth >= self.max_depth:
                return -1, '\n'
            self.seen_nodes.add(hash(start_node))
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
    ''' on max_depth 20
    python .\main.py --idfs URLD -n input11.15sav
    Game solvable
    (19, 'LLDDRRURDLULLDRUUUL', 2111007)
    python .\main.py --dfs URLD -n input11.15sav 
    Game solvable
    (-1, 199456, 1)
    python .\main.py --bfs URLD -n input11.15sav 
    Game solvable
    (19, 'LLDDRRURDLULLDRUUUL', 2174599)
    '''
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, order: List[str]) -> Tuple[int, str]:
        if start_node == solved_board:
            return 0, start_node.steps
        
        self.seen_nodes.add(hash(start_node))
        self.neighbours.append(start_node)
        shuffle_flag = order[0] == 'R'

        while self.neighbours:
            current_node = self.neighbours.pop()
            self.seen_nodes.add(hash(start_node))
            if shuffle_flag:
                shuffle(order)
            if current_node.depth < self.max_depth:
                for direction in order:
                    new_node = current_node._move(direction=direction)
                    if new_node and new_node == solved_board:
                        return len(new_node.steps), new_node.steps
                    if new_node and hash(new_node) not in self.seen_nodes:
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
        
        self.seen_nodes.add(hash(start_node))
        self.neighbours.append(start_node)
        shuffle_flag = order[0] == 'R'
        while True:
            lowest_depth_neighbours = deque()

            while self.neighbours:
                current_node = self.neighbours.pop()
                self.seen_nodes.add(hash(start_node))
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

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, heuristics: str) -> List[str]:
        if start_node == solved_board:
            return []
        return NotImplemented
        #return self.steps

class AStarAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, heuristics: str) -> List[str]:
        if start_node == solved_board:
            return 0, start_node.steps
        evaluate_node(start_node, heuristics, solved_board)
        return -1, '\n'
        #return self.steps

class SMAStarAlgorithm(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, start_node: PuzzleNode, solved_board: PuzzleNode, heuristics: str) -> List[str]:
        if start_node == solved_board:
            return []
        return NotImplemented
        #return self.steps

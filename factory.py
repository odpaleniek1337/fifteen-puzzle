from algorithms import BaseAlgorithm, BreadthFirstSearchAlgorithm, \
    DepthFirstSearchAlgorithm, IterativeDeepeningDepthFirstSearchAlgorithm, \
    BestFirstSearchAlgorithm, AStarAlgorithm, SMAStarAlgorithm

class AlgorithmFactory():
    def get_algoritm(self, algorithm: str) -> 'BaseAlgorithm':
        if algorithm == 'bfs':
            return BreadthFirstSearchAlgorithm()
        elif algorithm == 'dfs':
            return DepthFirstSearchAlgorithm()
        elif algorithm == 'idfs':
            return IterativeDeepeningDepthFirstSearchAlgorithm()
        elif algorithm == 'bf':
            return BestFirstSearchAlgorithm() 
        elif algorithm == 'astar':
            return AStarAlgorithm()
        elif algorithm == 'smastar':
            return SMAStarAlgorithm()

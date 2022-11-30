from algorithms import BaseAlgorithm, BreadthFirstSearchAlgorithm, \
    DepthFirstSearchAlgorithm, IterativeDeepeningDepthFirstSearchAlgorithm, \
    BestFirstSearchAlgorithm, AStarAlgorithm, SMAStarAlgorithm

from typing import Tuple, Union

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

def provide_algorithm_prerequisites(factory: AlgorithmFactory, args: object) -> Union[Tuple[BaseAlgorithm, str, int], None]:
    if args.bfs:
        return factory.get_algoritm('bfs'), args.bfs, 0
    elif args.dfs:
        return factory.get_algoritm('dfs'), args.dfs, 0
    elif args.idfs:
        return factory.get_algoritm('idfs'), args.idfs, 0
    elif args.bf:
        return factory.get_algoritm('bf'), args.bf, 1
    elif args.astar:
        return factory.get_algoritm('astar'), args.astar, 1
    elif args.smastar:
        return factory.get_algoritm('smastar'), args.smastar, 1
    return None, None, None

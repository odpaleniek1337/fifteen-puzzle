from algorithms import BaseAlgorithm, BreadthFirstSearchAlgorithm, \
    DepthFirstSearchAlgorithm, IterativeDeepeningDepthFirstSearchAlgorithm, \
    BestFirstSearchAlgorithm, AStarAlgorithm

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

def provide_algorithm_prerequisites(factory: AlgorithmFactory, args: object) -> Union[Tuple[BaseAlgorithm, str, int], None]:
    if args.bfs:
        return factory.get_algoritm('bfs'), args.bfs, 0
    elif args.dfs:
        return factory.get_algoritm('dfs'), args.dfs, 0
    elif args.idfs:
        return factory.get_algoritm('idfs'), args.idfs, 0
    elif args.bf:
        return factory.get_algoritm('bf'), 'manh' if int(args.bf) == 1 else ('mdlc' if int(args.bf) == 2 else 'manh'), 1
    elif args.astar:
        return factory.get_algoritm('astar'), 'manh' if int(args.astar) == 1 else ('mdlc' if int(args.astar) == 2 else 'manh'), 1
    return None, None, None

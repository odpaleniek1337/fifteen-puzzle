from typing import Tuple, Union
from fifteen_puzzle.algorithms import BaseAlgorithm, BreadthFirstSearchAlgorithm, \
    DepthFirstSearchAlgorithm, IterativeDeepeningDepthFirstSearchAlgorithm, \
    BestFirstSearchAlgorithm, AStarAlgorithm


class AlgorithmFactory():
    """Factory for algorithms
    """
    def get_algoritm(self, algorithm: str) -> 'BaseAlgorithm':
        """Provides desired algorithm

        Args:
            algorithm (str): algorithm's shortcut given by the user

        Returns:
            BaseAlgorithm: Base class for algorithms
        """
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
        return NotImplemented


def provide_algorithm_prerequisites(factory: AlgorithmFactory,
                                    args: object) -> Union[Tuple[BaseAlgorithm, str, int],
                                                           Tuple[None, None, None]]:
    """Provides algorithm object, technique and algorithm type

    Args:
        factory (AlgorithmFactory): Factory for algorithms
        args (object): parsed object from user input

    Returns:
        Union[Tuple[BaseAlgorithm, str, int], Tuple[None, None, None]]: (algorithm, order, type)
    """
    if args.bfs:
        return factory.get_algoritm('bfs'), args.bfs, 0
    elif args.dfs:
        return factory.get_algoritm('dfs'), args.dfs, 0
    elif args.idfs:
        return factory.get_algoritm('idfs'), args.idfs, 0
    elif args.bf:
        heuristics = 'manh' if int(args.bf) == 1 else ('mdlc' if int(args.bf) == 2 else 'manh')
        return factory.get_algoritm('bf'), heuristics, 1
    elif args.astar:
        heuristics = 'manh' if int(args.astar) == 1 else ('mdlc' if int(args.astar) == 2 else 'manh')
        return factory.get_algoritm('astar'), heuristics, 1
    return None, None, None

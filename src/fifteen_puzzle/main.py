from fifteen_puzzle.parsing_utils import parse_arguments, load_from_file
from fifteen_puzzle.algo_utils import check_if_solvable, prepare_solved_node, ExtendedPuzzleNode
from fifteen_puzzle.factory import AlgorithmFactory, provide_algorithm_prerequisites
from fifteen_puzzle.solution_viewer import show_result


def main():
    args = parse_arguments()

    start_node, grid_dimension = load_from_file(filename=args.input_file)
    SOLVED_NODE = prepare_solved_node(grid_dimension)

    if not check_if_solvable(start_node=start_node, dimension=grid_dimension):
        print('-1\n')
        exit('Game not solvable')

    algorithm, technique = None, None
    factory = AlgorithmFactory()
    algorithm, technique, algo_type = provide_algorithm_prerequisites(factory, args)
    if not algorithm:
        exit('You did not provide any algorithm')

    if not algo_type:
        n, result = algorithm.solve(start_node, SOLVED_NODE, list(technique))
    else:
        start_node = ExtendedPuzzleNode(start_node.board, start_node.dimension, start_node.steps)
        n, result = algorithm.solve(start_node, SOLVED_NODE, technique)
    print(f'{n}, {result}\n')

    if args.display:
        show_result(start_node, result)


if __name__ == '__main__':
    main()

from fifteen_puzzle.parsing_utils import parse_arguments, load_from_file
from fifteen_puzzle.algo_utils import check_if_solvable, prepare_solved_board
from fifteen_puzzle.factory import AlgorithmFactory, provide_algorithm_prerequisites
from fifteen_puzzle.solution_viewer import show_result
import time


def main():
    args = parse_arguments()

    start_node, grid_dimension = load_from_file(filename=args.input_file)
    SOLVED_BOARD = prepare_solved_board(grid_dimension)

    if not check_if_solvable(start_node=start_node, dimension=grid_dimension):
        print('-1\n')
        exit('Game not solvable')

    algorithm, technique = None, None
    factory = AlgorithmFactory()
    algorithm, technique, algo_type = provide_algorithm_prerequisites(factory, args)
    if not algorithm:
        exit('You did not provide any algorithm')
    start_time = time.time()

    if not algo_type:
        n, result = algorithm.solve(start_node, SOLVED_BOARD, list(technique))
    else:
        n, result = algorithm.solve(start_node, SOLVED_BOARD, technique)
    print(f'{n}, {result}, {time.time() - start_time}')

    if args.display:
        show_result(start_node, result)


if __name__ == '__main__':
    main()

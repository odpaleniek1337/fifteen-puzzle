from parsing_utils import parse_arguments, load_from_file
from algo_utils import check_if_solvable, prepare_solved_board
from factory import AlgorithmFactory, provide_algorithm_prerequisites
from solution_viewer import show_result

def main():
    #read passed arguments
    args = parse_arguments()

    #load given files
    start_node, grid_dimension = load_from_file(filename=args.input_file)
    SOLVED_BOARD = prepare_solved_board(grid_dimension)

    #check if possible to solve
    if not check_if_solvable(start_node=start_node, dimension=grid_dimension):
        print(f'-1\n')
    
    #choose proper algorithm
    algorithm, technique = None, None
    factory = AlgorithmFactory()
    algorithm, technique, algo_type = provide_algorithm_prerequisites(factory, args)
    if not algorithm:
        exit(f'You did not provide any algorithm')

    #solve game
    if not algo_type:
        n, result = algorithm.solve(start_node, SOLVED_BOARD, list(technique))
    else:
        n, result = algorithm.solve(start_node, SOLVED_BOARD, technique)
    print(f'{n}\n{result}')

    if args.display: 
        show_result(start_node, result)

if __name__ == '__main__':
    main()

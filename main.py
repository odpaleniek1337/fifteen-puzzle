from parsing_utils import parse_arguments, load_from_file
from algo_utils import check_if_solvable, prepare_solved_board
from factory import AlgorithmFactory

def main():
    #read passed arguments
    args = parse_arguments()

    #load given files
    start_node, grid_dimension = load_from_file(filename=args.input_file)
    SOLVED_BOARD = prepare_solved_board(grid_dimension)

    #check if possible to solve
    if not check_if_solvable(start_node=start_node, dimension=grid_dimension):
        exit('Game not solvable') #FIX #output -1 \n 
    print('Game solvable')
    
    #choose proper algorithm
    algorithm, technique = None, None
    factory = AlgorithmFactory()
    if args.bfs:
        algorithm = factory.get_algoritm('bfs')
        technique = args.bfs
    elif args.dfs:
        algorithm = factory.get_algoritm('dfs')
        technique = args.dfs
    elif args.idfs:
        algorithm = factory.get_algoritm('idfs')
        technique = args.idfs
    elif args.bf:
        algorithm = factory.get_algoritm('bf')
        technique = args.bf
    elif args.astar:
        algorithm = factory.get_algoritm('astar')
        technique = args.astar
    elif args.smastar:
        algorithm = factory.get_algoritm('smastar')
        technique = args.smastar
    #solve game
    print(algorithm.solve(start_node, SOLVED_BOARD, list(technique)))

    #save steps in viewable format e.g .15sav
    #output needed data
    pass

if __name__ == '__main__':
    main()

from script_utils import parse_arguments, load_from_file
from algorithms import check_if_solvable, prepare_solved_board

def main():
    #read passed arguments
    args = parse_arguments()

    #load given files
    start_node, grid_dimension = load_from_file(filename=args.input_file)
    SOLVED_BOARD = prepare_solved_board(grid_dimension)
    #check if possible to solve
    if not check_if_solvable(start_node=start_node, dimension=grid_dimension):
        exit('Game not solvable') #FIX
    print('Game solvable')
    
    #choose proper algorithm
    #solve game
    #save steps in viewable format e.g .15sav
    #output needed data
    pass

if __name__ == '__main__':
    main() 
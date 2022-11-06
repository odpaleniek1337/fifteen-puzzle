from script_utils import parse_arguments, load_from_file
from algorithms import check_if_solvable

def main():
    #read passed arguments
    args = parse_arguments()

    #load given files
    start_node = load_from_file(filename=args.input_file)
    
    #check if possible to solve
    if not check_if_solvable(start_node=start_node):
        exit('Game not solvable') #FIX
    else:
        exit('Game solvable') #FIX
    #choose proper algorithm
    #solve game
    #save steps in viewable format e.g .15sav
    #output needed data
    pass

if __name__ == '__main__':
    main() 
from constants import *

from argparse import ArgumentParser

def parse_arguments():
    parser = ArgumentParser(
        description='Script tires to solve fifteen-puzzle game using algorithm given by the user.'
    )

    algorithms_choice = parser.add_mutually_exclusive_group()
    algorithms_choice.add_argument('-b', '--bfs', choices=ORDER_SEARCH_POSSIBILITIES, help='Breadth-first search')
    algorithms_choice.add_argument('-d', '--dfs', choices=ORDER_SEARCH_POSSIBILITIES, help='Depth-first search')
    algorithms_choice.add_argument('-i', '--idfs', choices=ORDER_SEARCH_POSSIBILITIES, help='Iterative deepenening DFS')
    algorithms_choice.add_argument('-f', '--bf', choices=HEURISTICS_IDS, help='Best-first strategy')
    algorithms_choice.add_argument('-a', '--astar', choices=HEURISTICS_IDS, help='A* strategy')
    algorithms_choice.add_argument('-s', '--sma', choices=HEURISTICS_IDS, help='SMA* strategy')
    algorithms_choice.add_argument('-e', '--display', help='Used to display previous games', action='store_true')
    parser.add_argument('-n', '--input_file', default='input.15sav')
    parser.add_argument('-o', '--output_file', default='output.15sav')

    return parser.parse_args()
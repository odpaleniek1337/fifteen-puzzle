from constants import *

def show_result(board, solution) -> None:
    print(f'Start board: \n{board}')
    for _, i in enumerate(solution):
        board = board._move(i)
        print(f'Step number: {_ + 1} \n{board}')
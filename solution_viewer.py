from constants import *

def boardPrint(board):
    for i in range(0, len(board), 4):
        print("[", board[i], board[i+1], board[i+2], board[i+3], "]")
    
    print("")

def move(direction):
    if direction == "L":
        return -1
    elif direction == "R":
        return 1
    elif direction == "U":
        return -4
    elif direction == "D":
        return 4

def showResult(board, solution):
    for i in solution:
        print("Step number", solution.index(i), ":")

        initial = board.index(0)
        previous = initial + move(solution[solution.index(i)])

        board[initial] = board[previous]
        board[previous] = 0

        boardPrint(board)

def main():

    # tu mi dasz boarda
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    # a tu mi dasz kolejność ruchów
    moves = "UULLDRRD"
    # a tu metodke dla jego
    method = "Best first search"

    print("Alghorithm used to solve the game:", method)
    print("Total steps:", len(moves))
    print("Solution sequence:", moves, "\n")
    print("Initial board:")
    boardPrint(board)

    showResult(board, moves)

if __name__ == '__main__':
    main()
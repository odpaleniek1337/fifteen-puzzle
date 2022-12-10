def pass_solution_step_by_step_to_stdout(board, solution) -> None:
    """Prints starting board and steps to stdout

    Args:
        board (_type_): given board
        solution (_type_): steps found to solve board
    """
    print(f'Start board: \n{board}')
    for _, i in enumerate(solution):
        board = board.move(i)
        print(f'Step number: {_ + 1} \n{board}')

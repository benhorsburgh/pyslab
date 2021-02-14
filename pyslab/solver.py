from typing import Generator, Any
import numpy as np
from pyslab.board import unsolved_elems, row_values, col_values, nonet_values, peer_values


def brute_force(board: np.ndarray):
    try:
        next_to_solve = next(unsolved_elems(board))
    except StopIteration:
        return board

    possible_values = set(range(1, 10)) - peer_values(board, *next_to_solve)

    for v in possible_values:
        possible_board = np.copy(board)
        possible_board[next_to_solve] = v
        solution = brute_force(possible_board)
        if solution is not None:
            return solution


def brute_force_generator(board: np.ndarray) -> Generator[np.ndarray, Any, None]:
    try:
        next_to_solve = next(unsolved_elems(board))
        possible_values = set(range(1, 10)) - peer_values(board, *next_to_solve)

        for v in possible_values:
            possible_board = np.copy(board)
            possible_board[next_to_solve] = v
            yield from brute_force_generator(possible_board)
    except StopIteration:
        yield board

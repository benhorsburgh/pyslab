import numpy as np
from typing import Iterator, Tuple, Set, Generator, Any


def unsolved_elems(board: np.ndarray) -> Iterator[Tuple[int, int]]:
    return zip(*np.where(board == 0))


def row_values(board: np.ndarray, row: int) -> Set:
    return set(board[row, :]) - {0}


def col_values(board: np.ndarray, col: int) -> Set:
    return set(board[:, col]) - {0}


def nonet_values(board: np.ndarray, row: int, col: int) -> Set:
    r, c = row//3*3, col//3*3
    return set(board[r:r+3,c:c+3].flatten()) - {0}


def peer_values(board: np.ndarray, row: int, col: int) -> Set:
    return row_values(board, row).union(col_values(board, col)).union(nonet_values(board, row, col))


def is_solved(board: np.ndarray) -> bool:

    numbers = set(range(1, 10))

    # rows
    if not all(set(board[row, :]) == numbers for row in range(9)):
        return False

    # cols
    if not all(set(board[:, col]) == numbers for col in range(9)):
        return False

    # nonets
    if not all(
            set(board[i:i + 3, j:j + 3].flatten()) == numbers
            for i in range(0, 9, 3)
            for j in range(0, 9, 3)
    ):
        return False

    return True


def brute_force_solutions(board: np.ndarray) -> Generator[np.ndarray, Any, None]:
    try:
        next_to_solve = next(unsolved_elems(board))
        possible_values = set(range(1, 10)) - peer_values(board, *next_to_solve)

        for v in possible_values:
            possible_board = np.copy(board)
            possible_board[next_to_solve] = v
            yield from brute_force_solutions(possible_board)
    except StopIteration:
        yield board


def brute_force_solution(board: np.ndarray):
    try:
        return next(brute_force_solutions(board))
    except StopIteration:
        return None


def has_unique_solution(board: np.ndarray) -> bool:
    solutions = brute_force_solutions(board)
    try:
        _ = next(solutions)
    except StopIteration:
        return False

    try:
        _ = next(solutions)
        return False
    except StopIteration:
        return True

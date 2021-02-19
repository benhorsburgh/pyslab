import numpy as np
from typing import Iterator, Tuple, Set, Generator, Any, Dict, List


def unsolved_elems(puzzle: np.ndarray) -> Iterator[Tuple[int, int]]:
    return zip(*np.where(puzzle == 0))


def solved_elems(puzzle: np.ndarray) -> Iterator[Tuple[int, int]]:
    return zip(*np.where(puzzle > 0))


def row_values(puzzle: np.ndarray, row: int) -> Set:
    return set(puzzle[row, :]) - {0}

def col_values(puzzle: np.ndarray, col: int) -> Set:
    return set(puzzle[:, col]) - {0}

def nonet_values(puzzle: np.ndarray, row: int, col: int) -> Set:
    r, c = row//3*3, col//3*3
    return set(puzzle[r:r+3,c:c+3].flatten()) - {0}

def peer_values(puzzle: np.ndarray, row: int, col: int) -> Set:
    return row_values(puzzle, row).union(col_values(puzzle, col)).union(nonet_values(puzzle, row, col))

def is_solved(puzzle: np.ndarray) -> bool:

    numbers = set(range(1, 10))

    # rows
    if not all(set(puzzle[row, :]) == numbers for row in range(9)):
        return False

    # cols
    if not all(set(puzzle[:, col]) == numbers for col in range(9)):
        return False

    # nonets
    if not all(
            set(puzzle[i:i + 3, j:j + 3].flatten()) == numbers
            for i in range(0, 9, 3)
            for j in range(0, 9, 3)
    ):
        return False

    return True



def brute_force_solutions(
        puzzle: np.ndarray
) -> Generator[np.ndarray, Any, None]:
    try:
        next_to_solve = next(unsolved_elems(puzzle))
        possible_values = set(range(1, 10)) - peer_values(puzzle, *next_to_solve)

        for v in possible_values:
            possible_puzzle = np.copy(puzzle)
            possible_puzzle[next_to_solve] = v
            yield from brute_force_solutions(possible_puzzle)
    except StopIteration:
        yield puzzle



def brute_force_solution(puzzle: np.ndarray):
    try:
        return next(brute_force_solutions(puzzle))
    except StopIteration:
        return None


def has_unique_solution(puzzle: np.ndarray) -> bool:
    solutions = brute_force_solutions(puzzle)
    try:
        _ = next(solutions)
    except StopIteration:
        return False

    try:
        _ = next(solutions)
        return False
    except StopIteration:
        return True

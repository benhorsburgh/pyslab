import numpy as np
from typing import Iterator, Tuple, Set, Generator, Any, Dict, List


def unsolved_elems(candidates: np.ndarray) -> Iterator[Tuple[int, int]]:
    for r in range(9):
        for c in range(9):
            if len(candidates[r, c]) > 1:
                yield r, c


def solved_elems(candidates: np.ndarray) -> Iterator[Tuple[int, int]]:
    return [(r, c) for r in range(9) for c in range(9) if len(candidates[r, c]) == 1]


def row_values(candidates: np.ndarray, row: int) -> Set:
    return set().union(*[e for e in candidates[row] if len(e) == 1])

def col_values(candidates: np.ndarray, col: int) -> Set:
    return set().union(*[e for e in candidates[:, col] if len(e) == 1])

def nonet_values(candidates: np.ndarray, row: int, col: int) -> Set:
    r, c = row//3*3, col//3*3
    return set().union(*[e for e in candidates[r:r + 3, c:c + 3].flatten() if len(e) == 1])

def peer_values(candidates: np.ndarray, row: int, col: int) -> Set:
    return row_values(candidates, row).union(col_values(candidates, col)).union(nonet_values(candidates, row, col))

def is_solved(candidates: np.ndarray) -> bool:
    return all(len(c) == 1 for c in candidates.flatten())



def brute_force_solutions(
        candidates: np.ndarray
) -> Generator[np.ndarray, Any, None]:
    try:
        next_to_solve = next(unsolved_elems(candidates))
        possible_values = set(range(1, 10)) - peer_values(candidates, *next_to_solve)

        for v in possible_values:
            possible_candidates = np.copy(candidates)
            possible_candidates[next_to_solve] = {v}
            yield from brute_force_solutions(possible_candidates)
    except StopIteration:
        yield candidates


def brute_force_solution(candidates: np.ndarray):
    try:
        return next(brute_force_solutions(candidates))
    except StopIteration:
        return None


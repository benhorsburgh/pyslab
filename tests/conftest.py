import pytest
import numpy as np
from typing import Tuple, Callable
from pyslab.puzzle_grid import create_candidate_grid

@pytest.fixture
def simple_puzzle():
    return np.array([
        [1,2,3,4,5,6,7,8,9],
        [4,5,6,7,8,9,1,2,3],
        [7,8,9,1,2,3,4,5,6],
        [2,1,4,3,6,5,8,9,7],
        [3,6,5,8,9,7,2,1,4],
        [8,9,7,2,1,4,3,6,5],
        [5,3,1,6,4,2,9,7,8],
        [6,4,2,9,7,8,5,3,1],
        [9,7,8,5,3,1,6,4,2]
    ])


@pytest.fixture
def simple_candidates(simple_puzzle):
    return create_candidate_grid(simple_puzzle)


@pytest.fixture
def str_to_puzzle_candidates() -> Callable[[str], Tuple[np.ndarray, np.ndarray]]:

    def _f(sudoku: str) -> Tuple[np.ndarray, np.ndarray]:
        puzzle = np.array([int(e) for e in sudoku]).reshape([9, 9])
        return puzzle, create_candidate_grid(puzzle)
    return _f
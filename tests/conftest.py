import pytest
import numpy as np
from typing import Tuple, Callable
from solver import create_candidate_grid


@pytest.fixture
def simple_grid():
    return np.array(
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 1, 4, 3, 6, 5, 8, 9, 7],
            [3, 6, 5, 8, 9, 7, 2, 1, 4],
            [8, 9, 7, 2, 1, 4, 3, 6, 5],
            [5, 3, 1, 6, 4, 2, 9, 7, 8],
            [6, 4, 2, 9, 7, 8, 5, 3, 1],
            [9, 7, 8, 5, 3, 1, 6, 4, 2],
        ]
    )


@pytest.fixture
def simple_candidates(simple_grid):
    return create_candidate_grid(simple_grid)


@pytest.fixture
def str_to_grid_candidates() -> Callable[[str], Tuple[np.ndarray, np.ndarray]]:
    def _f(sudoku: str) -> Tuple[np.ndarray, np.ndarray]:
        grid = np.array([int(e) for e in sudoku]).reshape([9, 9])
        return grid, create_candidate_grid(grid)

    return _f

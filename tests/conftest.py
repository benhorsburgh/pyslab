import pytest
import numpy as np
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
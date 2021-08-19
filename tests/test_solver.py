import numpy as np
import pytest

from pyslab.core.types import Cell, Placement
from pyslab.core.validation import is_solved
from pyslab.solver import solve, make_placement, create_candidate_grid
from .conftest import str_to_grid_candidates


@pytest.mark.parametrize(
    "board",
    [
        "080107040700469001400803007135974600270618530608532100900046005000781000860095010",
        "000000805300457000000918030030700102700000004109003050090231000000584009405000000",
    ],
)
def test_boards(board):

    grid, _ = str_to_grid_candidates(board)
    grid = solve(grid)
    assert is_solved(grid)


class TestSetCell:
    @staticmethod
    def test_grid_cell_set(simple_grid):

        simple_grid[0, :] = 0
        simple_grid[:, 0] = 0
        candidates = create_candidate_grid(simple_grid)

        assert simple_grid[0, 0] == 0
        make_placement(simple_grid, candidates, Placement(Cell(0, 0), 1))
        assert simple_grid[0, 0] == 1

    @staticmethod
    def test_candidate_cell_set(simple_grid):

        simple_grid[0, :] = 0
        simple_grid[:, 0] = 0
        candidates = create_candidate_grid(simple_grid)

        assert candidates[0, 0] == [1, 2, 3, 4, 7]
        make_placement(simple_grid, candidates, Placement(Cell(0, 0), 1))
        assert candidates[0, 0] == [1]

    @staticmethod
    def test_row_peer_candidates_updated(simple_grid):
        simple_grid[0, :] = 0
        simple_grid[:, 0] = 0
        simple_grid[2, 2] = 0
        # un-solve all 1s
        simple_grid[np.where(simple_grid == 1)] = 0
        candidates = create_candidate_grid(simple_grid)

        assert any(1 in c for c in candidates[0, 1:])
        make_placement(simple_grid, candidates, Placement(Cell(0, 0), 1))
        assert not any(1 in c for c in candidates[0, 1:])


class TestCreateCandidateGrid:
    @staticmethod
    def test_solved(simple_grid):
        candidates = create_candidate_grid(simple_grid)
        assert all(
            candidates[r, c] == simple_grid[r, c] for r in range(9) for c in range(9)
        )

    @staticmethod
    def test_unsolved(simple_grid):
        simple_grid[0, :] = 0
        simple_grid[1, :] = 0
        candidates = create_candidate_grid(simple_grid)
        assert all(len(candidates[r, c]) == 2 for r in range(2) for c in range(9))
        assert all(
            candidates[r, c].pop() == simple_grid[r, c]
            for r in range(2, 9)
            for c in range(9)
        )

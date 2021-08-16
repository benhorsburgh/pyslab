import numpy as np
from pyslab.core.types import Cell
from pyslab.solver import solve, set_cell
from solver import create_candidate_grid
from core.validation import is_solved


class TestBoards:
    def test_only_singles(self, str_to_grid_candidates):

        grid, _ = str_to_grid_candidates(
            "080107040700469001400803007135974600270618530608532100900046005000781000860095010"
        )
        grid = solve(grid)
        assert is_solved(grid)


class TestSetCell:
    def test_grid_cell_set(self, simple_grid):

        simple_grid[0, :] = 0
        simple_grid[:, 0] = 0
        candidates = create_candidate_grid(simple_grid)

        assert simple_grid[0, 0] == 0
        set_cell(simple_grid, candidates, Cell(0, 0), 1)
        assert simple_grid[0, 0] == 1

    def test_candidate_cell_set(self, simple_grid):

        simple_grid[0, :] = 0
        simple_grid[:, 0] = 0
        candidates = create_candidate_grid(simple_grid)

        assert candidates[0, 0] == [1, 2, 3, 4, 7]
        set_cell(simple_grid, candidates, Cell(0, 0), 1)
        assert candidates[0, 0] == [1]

    def test_row_peer_candidates_updated(self, simple_grid):
        simple_grid[0, :] = 0
        simple_grid[:, 0] = 0
        simple_grid[2, 2] = 0
        # un-solve all 1s
        simple_grid[np.where(simple_grid == 1)] = 0
        candidates = create_candidate_grid(simple_grid)

        assert any(1 in c for c in candidates[0, 1:])
        set_cell(simple_grid, candidates, Cell(0, 0), 1)
        assert not any(1 in c for c in candidates[0, 1:])


class TestCreateCandidateGrid:
    def test_solved(self, simple_grid):
        candidates = create_candidate_grid(simple_grid)
        assert all(
            candidates[r, c] == simple_grid[r, c] for r in range(9) for c in range(9)
        )

    def test_unsolved(self, simple_grid):
        simple_grid[0, :] = 0
        simple_grid[1, :] = 0
        candidates = create_candidate_grid(simple_grid)
        assert all(len(candidates[r, c]) == 2 for r in range(2) for c in range(9))
        assert all(
            candidates[r, c].pop() == simple_grid[r, c]
            for r in range(2, 9)
            for c in range(9)
        )

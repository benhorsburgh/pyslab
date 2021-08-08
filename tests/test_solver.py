import numpy as np
from pyslab.solver import solve, set_cell
from pyslab.grid import create_candidate_grid


def test_hidden_single(str_to_grid_candidates):

    grid, _ = str_to_grid_candidates(
        "080107040700469001400803007135974600270618530608532100900046005000781000860095010"
    )
    solve(grid)
    # todo: complete


class TestSetCell:
    def test_grid_cell_set(self, simple_grid):

        simple_grid[0, :] = 0
        simple_grid[:, 0] = 0
        candidates = create_candidate_grid(simple_grid)

        assert simple_grid[0, 0] == 0
        set_cell(simple_grid, candidates, (0, 0), 1)
        assert simple_grid[0, 0] == 1

    def test_candidate_cell_set(self, simple_grid):

        simple_grid[0, :] = 0
        simple_grid[:, 0] = 0
        candidates = create_candidate_grid(simple_grid)

        assert candidates[0, 0] == {1, 2, 3, 4, 7}
        set_cell(simple_grid, candidates, (0, 0), 1)
        assert candidates[0, 0] == {1}

    def test_row_peer_candidates_updated(self, simple_grid):
        simple_grid[0, :] = 0
        simple_grid[:, 0] = 0
        simple_grid[2, 2] = 0
        # un-solve all 1s
        simple_grid[np.where(simple_grid == 1)] = 0
        candidates = create_candidate_grid(simple_grid)

        assert any(1 in c for c in candidates[0, 1:])
        set_cell(simple_grid, candidates, (0, 0), 1)
        assert not any(1 in c for c in candidates[0, 1:])

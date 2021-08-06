import numpy as np
from pyslab.solver import solve, set_element
from pyslab.puzzle_grid import create_candidate_grid


def test_naked_single(str_to_puzzle_candidates):

    puzzle, _ = str_to_puzzle_candidates(
        "080107040700469001400803007135974600270618530608532100900046005000781000860095010"
    )
    solve(puzzle)
    # todo: complete


class TestSetElement:
    def test_puzzle_element_set(self, simple_puzzle):

        simple_puzzle[0, :] = 0
        simple_puzzle[:, 0] = 0
        candidates = create_candidate_grid(simple_puzzle)

        assert simple_puzzle[0, 0] == 0
        set_element(simple_puzzle, candidates, (0, 0), 1)
        assert simple_puzzle[0, 0] == 1

    def test_candidate_element_set(self, simple_puzzle):

        simple_puzzle[0, :] = 0
        simple_puzzle[:, 0] = 0
        candidates = create_candidate_grid(simple_puzzle)

        assert candidates[0, 0] == {1, 2, 3, 4, 7}
        set_element(simple_puzzle, candidates, (0, 0), 1)
        assert candidates[0, 0] == {1}

    def test_row_peer_candidates_updated(self, simple_puzzle):
        simple_puzzle[0, :] = 0
        simple_puzzle[:, 0] = 0
        simple_puzzle[2, 2] = 0
        # un-solve all 1s
        simple_puzzle[np.where(simple_puzzle == 1)] = 0
        candidates = create_candidate_grid(simple_puzzle)

        assert any(1 in c for c in candidates[0, 1:])
        set_element(simple_puzzle, candidates, (0, 0), 1)
        assert not any(1 in c for c in candidates[0, 1:])

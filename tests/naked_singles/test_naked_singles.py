import pytest
import numpy as np
from pyslab.naked_singles import find_in_rows


class TestFindInRows:

    def test_no_unsolved(self, str_to_puzzle_candidates):

        elem, num = find_in_rows(*str_to_puzzle_candidates(
            "080107040700469001400803007135974600270618530608532100900046005000781000860095010")).pop()

        assert elem == (5, 7)
        assert num == 7

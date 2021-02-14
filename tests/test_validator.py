import pytest
import numpy as np
from pyslab.validator import is_solved


class TestIsSolved:

    def test_solved_valid(self, simple_board):
        assert is_solved(simple_board)

    def test_solved_invalid_row(self, simple_board):
        simple_board[0,:] = np.ones(9)
        assert not is_solved(simple_board)

    def test_solved_invalid_col(self, simple_board):
        simple_board[:,0] = np.ones(9)
        assert not is_solved(simple_board)

    def test_unsolved(self, simple_board):
        simple_board[0, 0] = 0
        assert not is_solved(simple_board)

import pytest
import numpy as np
from pyslab.board import unsolved


class TestUnsolved:

    def test_no_unsolved(self, simple_board):
        with pytest.raises(StopIteration):
            next(unsolved(simple_board))

    def test_one_unsolved(self, simple_board):
        simple_board[0, 0] = 0
        to_solve = unsolved(simple_board)
        _ = next(to_solve)
        with pytest.raises(StopIteration):
            _ = next(to_solve)

    def test_multi_unsolved(self, simple_board):
        simple_board[0:3, 0] = 0
        to_solve = unsolved(simple_board)
        for _ in range(3):
            _ = next(to_solve)
        with pytest.raises(StopIteration):
            _ = next(to_solve)

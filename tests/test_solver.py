import numpy as np
from pyslab.solver import brute_force
from pyslab.validator import solved

class TestBruteForce:

    def test_from_empty(self):

        board = np.zeros([9, 9])
        solution = brute_force(board)
        assert solved(solution)

    def test_simple_problem(self, simple_board):
        test_board = np.copy(simple_board)
        test_board[0, 5] = 0
        solution = brute_force(test_board)
        assert np.array_equal(solution, simple_board)
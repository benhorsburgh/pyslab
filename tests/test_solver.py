import numpy as np
from pyslab.solver import brute_force, brute_force_generator
from pyslab.validator import is_solved


class TestBruteForce:

    def test_from_empty(self):

        board = np.zeros([9, 9])
        solution = brute_force(board)
        assert is_solved(solution)

    def test_simple_problem(self, simple_board):
        test_board = np.copy(simple_board)
        test_board[0, 5] = 0
        solution = brute_force(test_board)
        assert np.array_equal(solution, simple_board)


class TestBruteForceGenerator:

    def test_from_empty(self):
        board = np.zeros([9, 9])
        solution = next(brute_force_generator(board))
        assert is_solved(solution)

    def test_simple_problem(self, simple_board):
        test_board = np.copy(simple_board)
        test_board[0, 5] = 0
        solution = next(brute_force_generator(test_board))
        assert np.array_equal(solution, simple_board)

    def test_multiple_solutions(self):
        board = np.zeros([9, 9])
        solution = brute_force_generator(board)
        solution_a, solution_b = next(solution), next(solution)
        assert not np.array_equal(solution_a, solution_b)
import pytest
import numpy as np
from pyslab.board import unsolved_elems, is_solved, brute_force_solution, brute_force_solutions, has_unique_solution


class TestUnsolvedElems:

    def test_no_unsolved(self, simple_board):
        with pytest.raises(StopIteration):
            next(unsolved_elems(simple_board))

    def test_one_unsolved(self, simple_board):
        simple_board[0, 0] = 0
        to_solve = unsolved_elems(simple_board)
        _ = next(to_solve)
        with pytest.raises(StopIteration):
            _ = next(to_solve)

    def test_multi_unsolved(self, simple_board):
        simple_board[0:3, 0] = 0
        to_solve = unsolved_elems(simple_board)
        for _ in range(3):
            _ = next(to_solve)
        with pytest.raises(StopIteration):
            _ = next(to_solve)


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


class TestBruteForceSolution:

    def test_timing(self):

        for _ in range(100):
            board = np.zeros([9, 9])
            solution = brute_force_solution(board)
        assert is_solved(solution)

    def test_from_empty(self):

        board = np.zeros([9, 9])
        solution = brute_force_solution(board)
        assert is_solved(solution)

    def test_simple_problem(self, simple_board):
        test_board = np.copy(simple_board)
        test_board[0, 5] = 0
        solution = brute_force_solution(test_board)
        assert np.array_equal(solution, simple_board)


class TestBruteForceSolutions:

    def test_from_empty(self):
        board = np.zeros([9, 9])
        solution = next(brute_force_solutions(board))
        assert is_solved(solution)

    def test_simple_problem(self, simple_board):
        test_board = np.copy(simple_board)
        test_board[0, 5] = 0
        solution = next(brute_force_solutions(test_board))
        assert np.array_equal(solution, simple_board)

    def test_multiple_solutions(self):
        board = np.zeros([9, 9])
        solution = brute_force_solutions(board)
        solution_a, solution_b = next(solution), next(solution)
        assert not np.array_equal(solution_a, solution_b)


class TestHasUniqueSolution:

    def test_solved(self, simple_board):
        assert has_unique_solution(simple_board)

    def test_unique(self, simple_board):
        simple_board[np.where(simple_board == 1)] = 0
        assert has_unique_solution(simple_board)

    def test_non_unique(self, simple_board):
        simple_board[np.where(simple_board == 1)] = 0
        simple_board[np.where(simple_board == 2)] = 0
        assert not has_unique_solution(simple_board)
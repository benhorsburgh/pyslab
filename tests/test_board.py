import pytest
import numpy as np
from pyslab.board import (
    unsolved_elems, is_solved, brute_force_solution, brute_force_solutions, has_unique_solution,
    brute_force_solution2, unsolved_elems2
)


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

class TestSomething:

    @pytest.fixture
    def simple_board2(self):
        return np.array([
            [{1,21}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}],
            [{4}, {5}, {6}, {7}, {8}, {9}, {1}, {2}, {3}],
            [{7}, {33}, {9}, {1}, {2}, {3}, {4}, {5}, {6}],
            [{2}, {1}, {4}, {3}, {6}, {5}, {8}, {9}, {7}],
            [{3}, {6}, {5}, {8}, {9}, {7}, {2}, {1}, {4}],
            [{8}, {9}, {7}, {2}, {1}, {4}, {3}, {6}, {5}],
            [{5}, {3}, {1}, {6}, {4}, {2}, {9}, {7}, {8}],
            [{6}, {4}, {2}, {9}, {7}, {8}, {5}, {3}, {1}],
            [{99}, {7}, {8}, {5}, {3}, {1}, {6}, {4}, {2}]
        ])

    def test_a(self, simple_board2):

        print()

        board = np.array([set(range(1,10)) for _ in range(81)]).reshape([9, 9])
        print(unsolved_elems2(board))
        # print(board)
        print()
        print(brute_force_solution2(board))
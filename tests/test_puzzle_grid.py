import pytest
import numpy as np
from pyslab.puzzle_grid import (
    unsolved_elems, is_solved, brute_force_solution, brute_force_solutions, has_unique_solution
)


class TestUnsolvedElems:

    def test_no_unsolved(self, simple_puzzle):
        with pytest.raises(StopIteration):
            next(unsolved_elems(simple_puzzle))

    def test_one_unsolved(self, simple_puzzle):
        simple_puzzle[0, 0] = 0
        to_solve = unsolved_elems(simple_puzzle)
        _ = next(to_solve)
        with pytest.raises(StopIteration):
            _ = next(to_solve)

    def test_multi_unsolved(self, simple_puzzle):
        simple_puzzle[0:3, 0] = 0
        to_solve = unsolved_elems(simple_puzzle)
        for _ in range(3):
            _ = next(to_solve)
        with pytest.raises(StopIteration):
            _ = next(to_solve)


class TestIsSolved:

    def test_solved_valid(self, simple_puzzle):
        assert is_solved(simple_puzzle)

    def test_solved_invalid_row(self, simple_puzzle):
        simple_puzzle[0, :] = np.ones(9)
        assert not is_solved(simple_puzzle)

    def test_solved_invalid_col(self, simple_puzzle):
        simple_puzzle[:, 0] = np.ones(9)
        assert not is_solved(simple_puzzle)

    def test_unsolved(self, simple_puzzle):
        simple_puzzle[0, 0] = 0
        assert not is_solved(simple_puzzle)


class TestBruteForceSolution:

    def test_from_empty(self):

        puzzle = np.zeros([9, 9])
        solution = brute_force_solution(puzzle)
        assert is_solved(solution)

    def test_simple_problem(self, simple_puzzle):
        test_puzzle = np.copy(simple_puzzle)
        test_puzzle[0, 5] = 0
        solution = brute_force_solution(test_puzzle)
        assert np.array_equal(solution, simple_puzzle)


class TestBruteForceSolutions:

    def test_from_empty(self):
        puzzle = np.zeros([9, 9])
        solution = next(brute_force_solutions(puzzle))
        assert is_solved(solution)

    def test_simple_problem(self, simple_puzzle):
        test_puzzle = np.copy(simple_puzzle)
        test_puzzle[0, 5] = 0
        solution = next(brute_force_solutions(test_puzzle))
        assert np.array_equal(solution, simple_puzzle)

    def test_multiple_solutions(self):
        puzzle = np.zeros([9, 9])
        solution = brute_force_solutions(puzzle)
        solution_a, solution_b = next(solution), next(solution)
        assert not np.array_equal(solution_a, solution_b)


class TestHasUniqueSolution:

    def test_solved(self, simple_puzzle):
        assert has_unique_solution(simple_puzzle)

    def test_unique(self, simple_puzzle):
        simple_puzzle[np.where(simple_puzzle == 1)] = 0
        assert has_unique_solution(simple_puzzle)

    def test_non_unique(self, simple_puzzle):
        simple_puzzle[np.where(simple_puzzle == 1)] = 0
        simple_puzzle[np.where(simple_puzzle == 2)] = 0
        assert not has_unique_solution(simple_puzzle)

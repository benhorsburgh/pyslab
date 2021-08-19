import numpy as np
import pytest

from pyslab.core.validation import (
    unsolved_cells,
    solved_cells,
    is_solved,
    brute_force_solution,
    brute_force_solutions,
    has_unique_solution,
)


class TestUnsolvedCells:
    """Test behaviour of unsolved cells method"""

    @staticmethod
    def test_no_unsolved(simple_grid):
        with pytest.raises(StopIteration):
            next(unsolved_cells(simple_grid))

    @staticmethod
    def test_one_unsolved(simple_grid):
        simple_grid[0, 0] = 0
        to_solve = unsolved_cells(simple_grid)
        _ = next(to_solve)
        with pytest.raises(StopIteration):
            _ = next(to_solve)

    @staticmethod
    def test_multi_unsolved(simple_grid):
        simple_grid[0:3, 0] = 0
        to_solve = unsolved_cells(simple_grid)
        for _ in range(3):
            _ = next(to_solve)
        with pytest.raises(StopIteration):
            _ = next(to_solve)


class TestSolvedCells:
    """Test behaviour of solved cells method"""

    @staticmethod
    def test_all_solved(simple_grid):
        assert len(list(solved_cells(simple_grid))) == 81

    @staticmethod
    def test_one_unsolved(simple_grid):
        simple_grid[0, 0] = 0
        solved = list(solved_cells(simple_grid))
        assert len(solved) == 80
        assert (0, 0) not in solved

    @staticmethod
    def test_multi_unsolved(simple_grid):
        simple_grid[0:3, :] = 0
        solved = list(solved_cells(simple_grid))
        assert all((r, c) in solved for r in range(3, 9) for c in range(9))
        assert all((r, c) not in solved for r in range(3) for c in range(9))


class TestIsSolved:
    @staticmethod
    def test_solved_valid(simple_grid):
        assert is_solved(simple_grid)

    @staticmethod
    def test_solved_invalid_row(simple_grid):
        simple_grid[0, :] = np.ones(9)
        assert not is_solved(simple_grid)

    @staticmethod
    def test_solved_invalid_col(simple_grid):
        simple_grid[:] = np.array(range(1, 10))
        assert not is_solved(simple_grid)

    @staticmethod
    def test_solved_invalid_box(simple_grid):
        for i in range(9):
            simple_grid[i, :] = np.roll(np.array(range(1, 10)), -i)
        assert not is_solved(simple_grid)

    @staticmethod
    def test_unsolved(simple_grid):
        simple_grid[0, 0] = 0
        assert not is_solved(simple_grid)


class TestBruteForceSolution:
    @staticmethod
    def test_from_empty():

        grid = np.zeros([9, 9])
        solution = brute_force_solution(grid)
        assert is_solved(solution)

    @staticmethod
    def test_simple_problem(simple_grid):
        test_grid = np.copy(simple_grid)
        test_grid[0, 5] = 0
        solution = brute_force_solution(test_grid)
        assert np.array_equal(solution, simple_grid)

    @staticmethod
    def test_unsolveable_problem():
        grid = np.ones([9, 9])
        grid[0, 0] = 0
        assert not brute_force_solution(grid)


class TestBruteForceSolutions:
    @staticmethod
    def test_from_empty():
        grid = np.zeros([9, 9])
        solution = next(brute_force_solutions(grid))
        assert is_solved(solution)

    @staticmethod
    def test_simple_problem(simple_grid):
        test_grid = np.copy(simple_grid)
        test_grid[0, 5] = 0
        solution = next(brute_force_solutions(test_grid))
        assert np.array_equal(solution, simple_grid)

    @staticmethod
    def test_multiple_solutions():
        grid = np.zeros([9, 9])
        solution = brute_force_solutions(grid)
        solution_a, solution_b = next(solution), next(solution)
        assert not np.array_equal(solution_a, solution_b)


class TestHasUniqueSolution:
    @staticmethod
    def test_solved(simple_grid):
        assert has_unique_solution(simple_grid)

    @staticmethod
    def test_unique(simple_grid):
        simple_grid[np.where(simple_grid == 1)] = 0
        assert has_unique_solution(simple_grid)

    @staticmethod
    def test_non_unique(simple_grid):
        simple_grid[np.where(simple_grid == 1)] = 0
        simple_grid[np.where(simple_grid == 2)] = 0
        assert not has_unique_solution(simple_grid)

    @staticmethod
    def test_unsolveable():
        grid = np.ones([9, 9])
        grid[0, 0] = 0
        assert not has_unique_solution(grid)

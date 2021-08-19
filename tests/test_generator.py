import numpy as np

from pyslab.core.validation import has_unique_solution
from pyslab.generator import generate_solution, generate_problem
from pyslab.generator import (
    permute_row_blocks,
    permute_col_blocks,
    permute_rows,
    permute_cols,
)


class TestGeneraSolution:
    @staticmethod
    def test_valid():
        grid = generate_solution()
        assert has_unique_solution(grid)

    @staticmethod
    def test_permutations(simple_grid):
        grid = generate_solution(simple_grid)
        assert not np.array_equal(grid, simple_grid)


class TestGenerateProblem:
    @staticmethod
    def test_valid():
        grid = generate_solution()
        problem = next(generate_problem(grid, max_clues=60))
        assert has_unique_solution(problem)

    @staticmethod
    def test_multiple_valid():
        grid = generate_solution()
        problems = generate_problem(grid, max_clues=55)
        problem1 = next(problems)
        problem2 = next(problems)
        assert not np.array_equal(problem1, problem2)


class TestPermuteRowBlocks:
    @staticmethod
    def test_grid_changed(simple_grid):
        permuted_grid = permute_row_blocks(simple_grid)
        assert not np.array_equal(permuted_grid, simple_grid)

    @staticmethod
    def test_all_rows_present(simple_grid):
        permuted_grid = permute_row_blocks(simple_grid)
        for row in simple_grid:
            assert row in permuted_grid

    @staticmethod
    def test_all_row_blocks_present(simple_grid):
        permuted_grid = permute_row_blocks(simple_grid).reshape([3, 27])
        simple_grid = simple_grid.reshape([3, 27])

        assert all(
            (simple_grid[r, :] == permuted_grid).all(axis=1).any() for r in range(3)
        )


class TestPermuteColBlocks:
    @staticmethod
    def test_grid_changed(simple_grid):
        permuted_grid = permute_col_blocks(simple_grid)
        assert not np.array_equal(permuted_grid, simple_grid)

    @staticmethod
    def test_all_cols_present(simple_grid):
        permuted_grid = permute_col_blocks(simple_grid).T
        for col in simple_grid.T:
            assert col in permuted_grid

    @staticmethod
    def test_all_col_blocks_present(simple_grid):
        permuted_grid = permute_col_blocks(simple_grid).T.reshape([3, 27])
        simple_grid = simple_grid.T.reshape([3, 27])

        assert all(
            (simple_grid[c, :] == permuted_grid).all(axis=1).any() for c in range(3)
        )


class TestPermuteRows:
    @staticmethod
    def test_grid_changed(simple_grid):
        permuted_grid = permute_rows(simple_grid)
        assert not np.array_equal(permuted_grid, simple_grid)

    @staticmethod
    def test_all_rows_present(simple_grid):
        permuted_grid = permute_rows(simple_grid)
        for row in simple_grid:
            assert row in permuted_grid

    @staticmethod
    def test_only_two_rows_swapped(simple_grid):
        permuted_grid = permute_rows(simple_grid)
        assert (
            sum(
                np.array_equal(simple_grid[row], permuted_grid[row])
                for row in range(len(simple_grid))
            )
            == 7
        )


class TestPermuteCols:
    @staticmethod
    def test_grid_changed(simple_grid):
        permuted_grid = permute_cols(simple_grid)
        assert not np.array_equal(permuted_grid, simple_grid)

    @staticmethod
    def test_all_cols_present(simple_grid):
        permuted_grid = permute_rows(simple_grid).T
        for col in simple_grid.T:
            assert col in permuted_grid

    @staticmethod
    def test_only_two_cols_swapped(simple_grid):
        permuted_grid = permute_cols(simple_grid).T
        assert (
            sum(
                np.array_equal(simple_grid.T[col], permuted_grid[col])
                for col in range(len(simple_grid))
            )
            == 7
        )

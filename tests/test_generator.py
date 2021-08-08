import numpy as np
from pyslab.generator import generate_solution, generate_problem
from pyslab.generator import (
    permute_row_blocks,
    permute_col_blocks,
    permute_rows,
    permute_cols,
)
from pyslab.grid import has_unique_solution


class TestGeneraSolution:
    def test_valid(self):
        grid = generate_solution()
        assert has_unique_solution(grid)

    def test_permutations(self, simple_grid):
        grid = generate_solution(simple_grid)
        assert not np.array_equal(grid, simple_grid)


class TestGenerateProblem:
    def test_valid(self):
        grid = generate_solution()
        problem = next(generate_problem(grid))
        assert has_unique_solution(problem)


class TestPermuteRowBlocks:
    def test_grid_changed(self, simple_grid):
        permuted_grid = permute_row_blocks(simple_grid)
        assert not np.array_equal(permuted_grid, simple_grid)

    def test_all_rows_present(self, simple_grid):
        permuted_grid = permute_row_blocks(simple_grid)
        for row in simple_grid:
            assert row in permuted_grid

    def test_all_row_blocks_present(self, simple_grid):
        permuted_grid = permute_row_blocks(simple_grid).reshape([3, 27])
        simple_grid = simple_grid.reshape([3, 27])

        assert all(
            (simple_grid[r, :] == permuted_grid).all(axis=1).any() for r in range(3)
        )


class TestPermuteColBlocks:
    def test_grid_changed(self, simple_grid):
        permuted_grid = permute_col_blocks(simple_grid)
        assert not np.array_equal(permuted_grid, simple_grid)

    def test_all_cols_present(self, simple_grid):
        permuted_grid = permute_col_blocks(simple_grid).T
        for col in simple_grid.T:
            assert col in permuted_grid

    def test_all_col_blocks_present(self, simple_grid):
        permuted_grid = permute_col_blocks(simple_grid).T.reshape([3, 27])
        simple_grid = simple_grid.T.reshape([3, 27])

        assert all(
            (simple_grid[c, :] == permuted_grid).all(axis=1).any() for c in range(3)
        )


class TestPermuteRows:
    def test_grid_changed(self, simple_grid):
        permuted_grid = permute_rows(simple_grid)
        assert not np.array_equal(permuted_grid, simple_grid)

    def test_all_rows_present(self, simple_grid):
        permuted_grid = permute_rows(simple_grid)
        for row in simple_grid:
            assert row in permuted_grid

    def test_only_two_rows_swapped(self, simple_grid):
        permuted_grid = permute_rows(simple_grid)
        assert (
            sum(
                np.array_equal(simple_grid[row], permuted_grid[row])
                for row in range(len(simple_grid))
            )
            == 7
        )


class TestPermuteCols:
    def test_grid_changed(self, simple_grid):
        permuted_grid = permute_cols(simple_grid)
        assert not np.array_equal(permuted_grid, simple_grid)

    def test_all_cols_present(self, simple_grid):
        permuted_grid = permute_rows(simple_grid).T
        for col in simple_grid.T:
            assert col in permuted_grid

    def test_only_two_cols_swapped(self, simple_grid):
        permuted_grid = permute_cols(simple_grid).T
        assert (
            sum(
                np.array_equal(simple_grid.T[col], permuted_grid[col])
                for col in range(len(simple_grid))
            )
            == 7
        )

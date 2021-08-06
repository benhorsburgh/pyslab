import pytest
import numpy as np
from pyslab import naked_singles
from pyslab.generator import generate_solution, generate_problem, generate_example
from pyslab.generator import (
    permute_row_blocks,
    permute_col_blocks,
    permute_rows,
    permute_cols,
)
from pyslab.puzzle_grid import is_solved, has_unique_solution, create_candidate_grid


# class TestGenerateExample:
#     @pytest.mark.parametrize(
#         "finder",
#         [
#             # naked_singles.find_in_rows,
#             # naked_singles.find_in_columns,
#             naked_singles.find_in_nonets,
#         ],
#     )
#     def test_generate_naked_single_row(self, finder):
#         puzzle = generate_example(finder)
#         print()
#         print(puzzle)
#         assert len(finder(puzzle, create_candidate_grid(puzzle))) > 0
#         print("".join([str(int(puzzle[r, c])) for r in range(9) for c in range(9)]))
#         print(finder(puzzle, create_candidate_grid(puzzle)))


class TestGeneraSolution:
    def test_valid(self):
        puzzle = generate_solution()
        assert has_unique_solution(puzzle)

    def test_permutations(self, simple_puzzle):
        puzzle = generate_solution(simple_puzzle)
        assert not np.array_equal(puzzle, simple_puzzle)


class TestGenerateProblem:
    def test_valid(self):
        puzzle = generate_solution()
        problem = next(generate_problem(puzzle))
        assert has_unique_solution(problem)


class TestPermuteRowBlocks:
    def test_puzzle_changed(self, simple_puzzle):
        permuted_puzzle = permute_row_blocks(simple_puzzle)
        assert not np.array_equal(permuted_puzzle, simple_puzzle)

    def test_all_rows_present(self, simple_puzzle):
        permuted_puzzle = permute_row_blocks(simple_puzzle)
        for row in simple_puzzle:
            assert row in permuted_puzzle

    def test_all_row_blocks_present(self, simple_puzzle):
        permuted_puzzle = permute_row_blocks(simple_puzzle).reshape([3, 27])
        simple_puzzle = simple_puzzle.reshape([3, 27])

        assert all(
            (simple_puzzle[r, :] == permuted_puzzle).all(axis=1).any() for r in range(3)
        )


class TestPermuteColBlocks:
    def test_puzzle_changed(self, simple_puzzle):
        permuted_puzzle = permute_col_blocks(simple_puzzle)
        assert not np.array_equal(permuted_puzzle, simple_puzzle)

    def test_all_cols_present(self, simple_puzzle):
        permuted_puzzle = permute_col_blocks(simple_puzzle).T
        for col in simple_puzzle.T:
            assert col in permuted_puzzle

    def test_all_col_blocks_present(self, simple_puzzle):
        permuted_puzzle = permute_col_blocks(simple_puzzle).T.reshape([3, 27])
        simple_puzzle = simple_puzzle.T.reshape([3, 27])

        assert all(
            (simple_puzzle[c, :] == permuted_puzzle).all(axis=1).any() for c in range(3)
        )


class TestPermuteRows:
    def test_puzzle_changed(self, simple_puzzle):
        permuted_puzzle = permute_rows(simple_puzzle)
        assert not np.array_equal(permuted_puzzle, simple_puzzle)

    def test_all_rows_present(self, simple_puzzle):
        permuted_puzzle = permute_rows(simple_puzzle)
        for row in simple_puzzle:
            assert row in permuted_puzzle

    def test_only_two_rows_swapped(self, simple_puzzle):
        permuted_puzzle = permute_rows(simple_puzzle)
        assert (
            sum(
                np.array_equal(simple_puzzle[row], permuted_puzzle[row])
                for row in range(len(simple_puzzle))
            )
            == 7
        )


class TestPermuteCols:
    def test_puzzle_changed(self, simple_puzzle):
        permuted_puzzle = permute_cols(simple_puzzle)
        assert not np.array_equal(permuted_puzzle, simple_puzzle)

    def test_all_cols_present(self, simple_puzzle):
        permuted_puzzle = permute_rows(simple_puzzle).T
        for col in simple_puzzle.T:
            assert col in permuted_puzzle

    def test_only_two_cols_swapped(self, simple_puzzle):
        permuted_puzzle = permute_cols(simple_puzzle).T
        assert (
            sum(
                np.array_equal(simple_puzzle.T[col], permuted_puzzle[col])
                for col in range(len(simple_puzzle))
            )
            == 7
        )

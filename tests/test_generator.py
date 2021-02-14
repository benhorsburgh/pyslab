import numpy as np
from pyslab.generator import permute_row_blocks, permute_col_blocks, permute_rows, permute_cols


class TestPermuteRowBlocks:

    def test_board_changed(self, simple_board):
        permuted_board = permute_row_blocks(simple_board)
        assert not np.array_equal(permuted_board, simple_board)

    def test_all_rows_present(self, simple_board):
        permuted_board = permute_row_blocks(simple_board)
        for row in simple_board:
            assert(row in permuted_board)

    def test_all_row_blocks_present(self, simple_board):
        permuted_board = permute_row_blocks(simple_board).reshape([3, 27])
        simple_board = simple_board.reshape([3, 27])

        assert all(
            (simple_board[r,:] == permuted_board).all(axis=1).any()
            for r in range(3)
        )


class TestPermuteColBlocks:

    def test_board_changed(self, simple_board):
        permuted_board = permute_col_blocks(simple_board)
        assert not np.array_equal(permuted_board, simple_board)

    def test_all_cols_present(self, simple_board):
        permuted_board = permute_col_blocks(simple_board).T
        for col in simple_board.T:
            assert(col in permuted_board)

    def test_all_col_blocks_present(self, simple_board):
        permuted_board = permute_col_blocks(simple_board).T.reshape([3, 27])
        simple_board = simple_board.T.reshape([3, 27])

        assert all(
            (simple_board[c,:] == permuted_board).all(axis=1).any()
            for c in range(3)
        )


class TestPermuteRows:

    def test_board_changed(self, simple_board):
        permuted_board = permute_rows(simple_board)
        assert not np.array_equal(permuted_board, simple_board)

    def test_all_rows_present(self, simple_board):
        permuted_board = permute_rows(simple_board)
        for row in simple_board:
            assert (row in permuted_board)

    def test_only_two_rows_swapped(self, simple_board):
        permuted_board = permute_rows(simple_board)
        assert sum(
            np.array_equal(simple_board[row], permuted_board[row])
            for row in range(len(simple_board))
        ) == 7


class TestPermuteCols:

    def test_board_changed(self, simple_board):
        permuted_board = permute_cols(simple_board)
        assert not np.array_equal(permuted_board, simple_board)

    def test_all_cols_present(self, simple_board):
        permuted_board = permute_rows(simple_board).T
        for col in simple_board.T:
            assert (col in permuted_board)

    def test_only_two_cols_swapped(self, simple_board):
        permuted_board = permute_cols(simple_board).T
        assert sum(
            np.array_equal(simple_board.T[col], permuted_board[col])
            for col in range(len(simple_board))
        ) == 7

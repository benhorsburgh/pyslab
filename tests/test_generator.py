import numpy as np
from pyslab.generator import permute_row_blocks, permute_col_blocks


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

    def test_all_rows_present(self, simple_board):
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

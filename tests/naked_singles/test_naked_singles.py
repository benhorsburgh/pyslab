from pyslab.naked_singles import naked_singles_row


class TestNakedSinglesRow:

    def test_none_in_solved_board(self, simple_board):
        assert not naked_singles_row(simple_board)

    def test_naked_single(self, simple_board):
        expected = simple_board[0, 2]
        simple_board[0, 2] = 0
        assert naked_singles_row(simple_board) == (0, 2, expected)

import random

import pytest

from pyslab.core.digits import row_digits, column_digits, box_digits, peer_digits
from pyslab.core.types import Cell


class TestRowDigits:
    @staticmethod
    @pytest.mark.parametrize("row", list(range(9)))
    def test_all_solved(simple_grid, row):
        assert row_digits(simple_grid, row) == set(range(1, 10))

    @staticmethod
    @pytest.mark.parametrize("row", list(range(9)))
    def test_some_solved(simple_grid, row):
        simple_grid[row, ::2] = 0
        assert row_digits(simple_grid, row) == set(simple_grid[row, 1::2])

    @staticmethod
    @pytest.mark.parametrize("row", list(range(9)))
    def test_none_solved(simple_grid, row):
        simple_grid[row, :] = 0
        assert row_digits(simple_grid, row) == set()


class TestColumnDigits:
    @staticmethod
    @pytest.mark.parametrize("col", list(range(9)))
    def test_all_solved(simple_grid, col):
        assert column_digits(simple_grid, col) == set(range(1, 10))

    @staticmethod
    @pytest.mark.parametrize("col", list(range(9)))
    def test_some_solved(simple_grid, col):
        simple_grid[::2, col] = 0
        assert column_digits(simple_grid, col) == set(simple_grid[1::2, col])

    @staticmethod
    @pytest.mark.parametrize("col", list(range(9)))
    def test_none_solved(simple_grid, col):
        simple_grid[:, col] = 0
        assert column_digits(simple_grid, col) == set()


class TestBoxDigits:
    @staticmethod
    @pytest.mark.parametrize("box", list(range(9)))
    def test_all_solved(simple_grid, box):
        assert box_digits(simple_grid, box) == set(range(1, 10))

    @staticmethod
    @pytest.mark.parametrize("box", list(range(9)))
    def test_some_solved(simple_grid, box):
        row, col = (box // 3) * 3, (box % 3) * 3
        remove = (row + random.randint(0, 2), col + random.randint(0, 2))
        simple_grid[remove] = 0
        assert box_digits(simple_grid, box) == set(
            digit
            for digit in simple_grid[row : row + 3, col : col + 3].flatten()
            if digit != 0
        )

    @staticmethod
    @pytest.mark.parametrize("box", list(range(9)))
    def test_none_solved(simple_grid, box):
        simple_grid[:, :] = 0
        assert box_digits(simple_grid, box) == set()


class TestPeerDigits:
    @staticmethod
    @pytest.mark.parametrize("cell", [Cell(r, c) for r in range(9) for c in range(9)])
    def test_cell_digit_not_included(simple_grid, cell):
        assert simple_grid[cell] not in peer_digits(simple_grid, cell)

    @staticmethod
    @pytest.mark.parametrize("cell", [Cell(r, c) for r in range(9) for c in range(9)])
    def test_non_cell_digit_included(simple_grid, cell):
        assert peer_digits(simple_grid, cell) == {
            digit for digit in range(1, 10) if digit != simple_grid[cell]
        }

import random

import pytest

from core.types import Cell
from core.digits import row_digits, column_digits, box_digits, peer_digits


class TestRowDigits:
    @pytest.mark.parametrize("row", list(range(9)))
    def test_all_solved(self, simple_grid, row):
        assert row_digits(simple_grid, row) == set(range(1, 10))

    @pytest.mark.parametrize("row", list(range(9)))
    def test_some_solved(self, simple_grid, row):
        simple_grid[row, ::2] = 0
        assert row_digits(simple_grid, row) == set(simple_grid[row, 1::2])

    @pytest.mark.parametrize("row", list(range(9)))
    def test_none_solved(self, simple_grid, row):
        simple_grid[row, :] = 0
        assert row_digits(simple_grid, row) == set()


class TestColumnDigits:
    @pytest.mark.parametrize("col", list(range(9)))
    def test_all_solved(self, simple_grid, col):
        assert column_digits(simple_grid, col) == set(range(1, 10))

    @pytest.mark.parametrize("col", list(range(9)))
    def test_some_solved(self, simple_grid, col):
        simple_grid[::2, col] = 0
        assert column_digits(simple_grid, col) == set(simple_grid[1::2, col])

    @pytest.mark.parametrize("col", list(range(9)))
    def test_none_solved(self, simple_grid, col):
        simple_grid[:, col] = 0
        assert column_digits(simple_grid, col) == set()


class TestBoxDigits:
    @pytest.mark.parametrize("box", list(range(9)))
    def test_all_solved(self, simple_grid, box):
        assert box_digits(simple_grid, box) == set(range(1, 10))

    @pytest.mark.parametrize("box", list(range(9)))
    def test_some_solved(self, simple_grid, box):
        row, col = (box // 3) * 3, (box % 3) * 3
        remove = (row + random.randint(0, 2), col + random.randint(0, 2))
        simple_grid[remove] = 0
        assert box_digits(simple_grid, box) == set(
            digit
            for digit in simple_grid[row : row + 3, col : col + 3].flatten()
            if digit != 0
        )

    @pytest.mark.parametrize("box", list(range(9)))
    def test_none_solved(self, simple_grid, box):
        simple_grid[:, :] = 0
        assert box_digits(simple_grid, box) == set()


class TestPeerDigits:
    @pytest.mark.parametrize("cell", [Cell(r, c) for r in range(9) for c in range(9)])
    def test_cell_digit_not_included(self, simple_grid, cell):
        assert simple_grid[cell] not in peer_digits(simple_grid, cell)

    @pytest.mark.parametrize("cell", [Cell(r, c) for r in range(9) for c in range(9)])
    def test_non_cell_digit_included(self, simple_grid, cell):
        assert peer_digits(simple_grid, cell) == {
            digit for digit in range(1, 10) if digit != simple_grid[cell]
        }

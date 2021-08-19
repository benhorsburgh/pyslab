import pytest

from pyslab.core.cells import row_cells, column_cells, box_cells
from pyslab.strategies.hidden_single import find_placements
from ..conftest import str_to_grid_candidates


class TestFindPlacements:
    @staticmethod
    def test_one_single_in_row():

        grid, candidates = str_to_grid_candidates(
            "403010005056480100200000040900004000005020600000700008020000006008036910600090507"
        )
        cell, digit, *_ = find_placements(grid, candidates, row_cells(6)).pop()

        assert cell == (6, 2)
        assert digit == 9

    @staticmethod
    def test_two_single_in_row():

        grid, candidates = str_to_grid_candidates(
            "008006002020500070070010005001060000046275810000040600800050090010008060500900300"
        )
        singles = list(find_placements(grid, candidates, row_cells(0)))

        assert ((0, 1), 5) in singles
        assert ((0, 3), 7) in singles

    @staticmethod
    def test_one_single_in_column():

        grid, candidates = str_to_grid_candidates(
            "005036800080920005000000002507000009290607084300000506100000000900048020004210900"
        )
        cell, digit, *_ = find_placements(grid, candidates, column_cells(0)).pop()

        assert cell == (8, 0)
        assert digit == 8

    @staticmethod
    def test_two_singles_in_column():

        grid, candidates = str_to_grid_candidates(
            "000019567090060000007430090906000002004000900100000405010087600000040010683190000"
        )
        singles = list(find_placements(grid, candidates, column_cells(1)))

        assert ((0, 1), 4) in singles
        assert ((2, 1), 6) in singles

    @staticmethod
    def test_one_single_in_box():

        grid, candidates = str_to_grid_candidates(
            "006830000009006040800109000040200600013090480007005030000502004060900700000068200"
        )
        cell, digit, *_ = find_placements(grid, candidates, box_cells(8)).pop()

        assert cell == (6, 7)
        assert digit == 6

    @staticmethod
    def test_two_singles_in_box():

        grid, candidates = str_to_grid_candidates(
            "001007000600102000050043001006000120019060830084000700100970040000301007000800200"
        )
        singles = list(find_placements(grid, candidates, box_cells(7)))

        assert ((7, 4), 2) in singles
        assert ((8, 5), 4) in singles

    @staticmethod
    @pytest.mark.parametrize("i", list(range(9)))
    def test_naked_single_ignored(simple_grid, simple_candidates, i):

        simple_grid[0, 0] = 0
        assert not list(find_placements(simple_grid, simple_candidates, row_cells(i)))
        assert not list(
            find_placements(simple_grid, simple_candidates, column_cells(i))
        )
        assert not list(find_placements(simple_grid, simple_candidates, box_cells(i)))

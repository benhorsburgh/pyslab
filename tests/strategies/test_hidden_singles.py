import pytest
from pyslab.strategies.hidden_singles import find_placements


class TestFindPlacements:
    def test_one_single_in_row(self, str_to_grid_candidates):

        grid, candidates = str_to_grid_candidates(
            "403010005056480100200000040900004000005020600000700008020000006008036910600090507"
        )
        cell, digit = find_placements(grid, candidates, 6).pop()

        assert cell == (6, 2)
        assert digit == 9

    def test_two_single_in_row(self, str_to_grid_candidates):

        grid, candidates = str_to_grid_candidates(
            "008006002020500070070010005001060000046275810000040600800050090010008060500900300"
        )
        singles = list(find_placements(grid, candidates, 0))

        assert ((0, 1), 5) in singles
        assert ((0, 3), 7) in singles

    def test_one_single_in_column(self, str_to_grid_candidates):

        grid, candidates = str_to_grid_candidates(
            "005036800080920005000000002507000009290607084300000506100000000900048020004210900"
        )
        cell, digit = find_placements(grid, candidates, 9).pop()

        assert cell == (8, 0)
        assert digit == 8

    def test_two_singles_in_column(self, str_to_grid_candidates):

        grid, candidates = str_to_grid_candidates(
            "000019567090060000007430090906000002004000900100000405010087600000040010683190000"
        )
        singles = list(find_placements(grid, candidates, 10))

        assert ((0, 1), 4) in singles
        assert ((2, 1), 6) in singles

    def test_one_single_in_box(self, str_to_grid_candidates):

        grid, candidates = str_to_grid_candidates(
            "006830000009006040800109000040200600013090480007005030000502004060900700000068200"
        )
        cell, digit = find_placements(grid, candidates, 26).pop()

        assert cell == (6, 7)
        assert digit == 6

    def test_two_singles_in_box(self, str_to_grid_candidates):

        grid, candidates = str_to_grid_candidates(
            "001007000600102000050043001006000120019060830084000700100970040000301007000800200"
        )
        singles = list(find_placements(grid, candidates, 25))

        assert ((7, 4), 2) in singles
        assert ((8, 5), 4) in singles

    @pytest.mark.parametrize("box", list(range(27)))
    def test_naked_single_ignored(self, simple_grid, simple_candidates, box):

        simple_grid[0, 0] = 0
        singles = list(find_placements(simple_grid, simple_candidates, box))

        assert not singles

from pyslab.core.cells import row_cells, column_cells, box_cells
from pyslab.strategies.hidden_pair import find_eliminations
from ..conftest import str_to_grid_candidates


class TestFindPlacements:
    @staticmethod
    def test_hidden_pair_in_row():

        grid, candidates = str_to_grid_candidates(
            "000800900300100870000057030007540010540000069010069500030910000029005004006003000"
        )
        eliminations = list(find_eliminations(grid, candidates, row_cells(3)))

        assert eliminations[0].candidates == [
            ((3, 0), 2),
            ((3, 0), 8),
            ((3, 1), 8),
        ]

    @staticmethod
    def test_hidden_pair_in_column():
        grid, candidates = str_to_grid_candidates(
            "900700003027360809006000050065800000100000008000001560030000400408032970600005002"
        )
        eliminations = list(find_eliminations(grid, candidates, column_cells(8)))

        assert eliminations[0].candidates == [
            ((6, 8), 1),
            ((7, 8), 1),
        ]

    @staticmethod
    def test_hidden_pair_in_box():
        grid, candidates = str_to_grid_candidates(
            "060030040001580007008009302000100083000705000910003000207900600100026500030050020"
        )
        eliminations = list(find_eliminations(grid, candidates, box_cells(0)))

        assert eliminations[0].candidates == [
            ((0, 2), 5),
            ((1, 1), 4),
        ]

    @staticmethod
    def test_naked_single_ignored():
        grid, candidates = str_to_grid_candidates(
            "023100070810000400704800001201607000000000000000901607400002709006000013030006540"
        )
        eliminations = list(find_eliminations(grid, candidates, box_cells(8)))

        assert len(eliminations) == 0

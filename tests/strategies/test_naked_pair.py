from pyslab.core.cells import row_cells, column_cells, box_cells
from pyslab.core.types import Cell
from pyslab.strategies.naked_pair import find_eliminations
from ..conftest import str_to_grid_candidates


class TestFindPlacements:
    @staticmethod
    def test_naked_pair_in_row():

        grid, candidates = str_to_grid_candidates(
            "000000805300457000000918030030700102700000004109003050090231000000584009405000000"
        )
        eliminations = list(find_eliminations(grid, candidates, row_cells(0)))

        assert eliminations[0].candidates == [
            (Cell(0, 0), 2),
            (Cell(0, 0), 6),
            (Cell(0, 1), 2),
            (Cell(0, 1), 6),
            (Cell(0, 2), 2),
            (Cell(0, 2), 6),
            (Cell(0, 3), 6),
            (Cell(0, 7), 2),
            (Cell(0, 7), 6),
        ]

    @staticmethod
    def test_naked_pair_in_column():
        grid, candidates = str_to_grid_candidates(
            "009300008860050000075910300302004000000201000000600102008065920000040076600002800"
        )
        eliminations = list(find_eliminations(grid, candidates, column_cells(3)))

        assert eliminations[0].candidates == [
            (Cell(row=1, column=3), 7),
            (Cell(row=3, column=3), 7),
            (Cell(row=7, column=3), 1),
        ]

    @staticmethod
    def test_naked_pair_in_box():
        grid, candidates = str_to_grid_candidates(
            "023100070810000400704800001201607000000000000000901607400002709006000013030006540"
        )
        eliminations = list(find_eliminations(grid, candidates, box_cells(8)))

        assert eliminations[0].candidates == [(Cell(row=6, column=7), 8)]

    @staticmethod
    def test_hidden_single_ignored():
        grid, candidates = str_to_grid_candidates(
            "060030040001580007008009302000100083000705000910003000207900600100026500030050020"
        )
        eliminations = list(find_eliminations(grid, candidates, box_cells(0)))

        assert len(eliminations) == 0

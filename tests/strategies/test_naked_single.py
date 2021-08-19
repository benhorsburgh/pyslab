from pyslab.core.cells import row_cells, column_cells, box_cells
from pyslab.strategies.naked_single import find_placements
from ..conftest import str_to_grid_candidates


class TestFindPlacements:
    @staticmethod
    def test_ignore_hidden_singles():

        grid, candidates = str_to_grid_candidates(
            "403010005056480100200000040900004000005020600000700008020000006008036910600090507"
        )
        assert len(find_placements(grid, candidates, row_cells(6))) == 0

    @staticmethod
    def test_one_single_in_row(simple_grid, simple_candidates):
        simple_grid[0, 0] = 0
        assert find_placements(simple_grid, simple_candidates, row_cells(0)) == [
            ((0, 0), 1)
        ]

    @staticmethod
    def test_two_single_in_row(simple_grid, simple_candidates):
        simple_grid[0, 0] = 0
        simple_grid[0, 5] = 0
        assert find_placements(simple_grid, simple_candidates, row_cells(0)) == [
            ((0, 0), 1),
            ((0, 5), 6),
        ]

    @staticmethod
    def test_one_single_in_column(simple_grid, simple_candidates):
        simple_grid[5, 0] = 0
        assert find_placements(simple_grid, simple_candidates, column_cells(0)) == [
            ((5, 0), 8)
        ]

    @staticmethod
    def test_two_single_in_column(simple_grid, simple_candidates):
        simple_grid[6, 1] = 0
        simple_grid[7, 1] = 0
        assert find_placements(simple_grid, simple_candidates, column_cells(1)) == [
            ((6, 1), 3),
            ((7, 1), 4),
        ]

    @staticmethod
    def test_one_single_in_box(simple_grid, simple_candidates):
        simple_grid[0, 0] = 0
        assert find_placements(simple_grid, simple_candidates, box_cells(0)) == [
            ((0, 0), 1)
        ]

    @staticmethod
    def test_two_single_in_box(simple_grid, simple_candidates):
        simple_grid[0, 0] = 0
        simple_grid[1, 1] = 0
        assert find_placements(simple_grid, simple_candidates, box_cells(0)) == [
            ((0, 0), 1),
            ((1, 1), 5),
        ]

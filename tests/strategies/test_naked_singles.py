from pyslab.strategies.naked_singles import find_placements


class TestFindPlacements:
    def test_ignore_hidden_singles(self, str_to_grid_candidates):

        grid, candidates = str_to_grid_candidates(
            "403010005056480100200000040900004000005020600000700008020000006008036910600090507"
        )
        assert len(find_placements(grid, candidates, 6)) == 0

    def test_one_single_in_row(self, simple_grid, simple_candidates):
        simple_grid[0, 0] = 0
        assert find_placements(simple_grid, simple_candidates, 0) == [((0, 0), 1)]

    def test_two_single_in_row(self, simple_grid, simple_candidates):
        simple_grid[0, 0] = 0
        simple_grid[0, 5] = 0
        assert find_placements(simple_grid, simple_candidates, 0) == [
            ((0, 0), 1),
            ((0, 5), 6),
        ]

    def test_one_single_in_column(self, simple_grid, simple_candidates):
        simple_grid[5, 0] = 0
        assert find_placements(simple_grid, simple_candidates, 9) == [((5, 0), 8)]

    def test_two_single_in_column(self, simple_grid, simple_candidates):
        simple_grid[6, 1] = 0
        simple_grid[7, 1] = 0
        assert find_placements(simple_grid, simple_candidates, 10) == [
            ((6, 1), 3),
            ((7, 1), 4),
        ]

    def test_one_single_in_box(self, simple_grid, simple_candidates):
        simple_grid[0, 0] = 0
        assert find_placements(simple_grid, simple_candidates, 18) == [((0, 0), 1)]

    def test_two_single_in_box(self, simple_grid, simple_candidates):
        simple_grid[0, 0] = 0
        simple_grid[1, 1] = 0
        assert find_placements(simple_grid, simple_candidates, 18) == [
            ((0, 0), 1),
            ((1, 1), 5),
        ]

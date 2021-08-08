import random
import pytest
import numpy as np
from pyslab.grid import (
    unsolved_cells,
    solved_cells,
    row_cells,
    column_cells,
    box_cells,
    row_digits,
    column_digits,
    box_digits,
    peer_digits,
    peer_row_cells,
    peer_column_cells,
    peer_box_cells,
    peer_cells,
    is_solved,
    brute_force_solution,
    brute_force_solutions,
    has_unique_solution,
    create_candidate_grid,
)


class TestUnsolvedCells:
    """Test behaviour of unsolved cells method"""

    def test_no_unsolved(self, simple_grid):
        with pytest.raises(StopIteration):
            next(unsolved_cells(simple_grid))

    def test_one_unsolved(self, simple_grid):
        simple_grid[0, 0] = 0
        to_solve = unsolved_cells(simple_grid)
        _ = next(to_solve)
        with pytest.raises(StopIteration):
            _ = next(to_solve)

    def test_multi_unsolved(self, simple_grid):
        simple_grid[0:3, 0] = 0
        to_solve = unsolved_cells(simple_grid)
        for _ in range(3):
            _ = next(to_solve)
        with pytest.raises(StopIteration):
            _ = next(to_solve)


class TestSolvedCells:
    """Test behaviour of solved cells method"""

    def test_all_solved(self, simple_grid):
        assert len(list(solved_cells(simple_grid))) == 81

    def test_one_unsolved(self, simple_grid):
        simple_grid[0, 0] = 0
        solved = list(solved_cells(simple_grid))
        assert len(solved) == 80
        assert (0, 0) not in solved

    def test_multi_unsolved(self, simple_grid):
        simple_grid[0:3, :] = 0
        solved = list(solved_cells(simple_grid))
        assert all((r, c) in solved for r in range(3, 9) for c in range(9))
        assert all((r, c) not in solved for r in range(3) for c in range(9))


class TestRowCells:
    @pytest.mark.parametrize(
        "row,expected",
        [
            (
                0,
                [
                    (0, 0),
                    (0, 1),
                    (0, 2),
                    (0, 3),
                    (0, 4),
                    (0, 5),
                    (0, 6),
                    (0, 7),
                    (0, 8),
                ],
            ),
            (
                1,
                [
                    (1, 0),
                    (1, 1),
                    (1, 2),
                    (1, 3),
                    (1, 4),
                    (1, 5),
                    (1, 6),
                    (1, 7),
                    (1, 8),
                ],
            ),
            (
                2,
                [
                    (2, 0),
                    (2, 1),
                    (2, 2),
                    (2, 3),
                    (2, 4),
                    (2, 5),
                    (2, 6),
                    (2, 7),
                    (2, 8),
                ],
            ),
            (
                3,
                [
                    (3, 0),
                    (3, 1),
                    (3, 2),
                    (3, 3),
                    (3, 4),
                    (3, 5),
                    (3, 6),
                    (3, 7),
                    (3, 8),
                ],
            ),
            (
                4,
                [
                    (4, 0),
                    (4, 1),
                    (4, 2),
                    (4, 3),
                    (4, 4),
                    (4, 5),
                    (4, 6),
                    (4, 7),
                    (4, 8),
                ],
            ),
            (
                5,
                [
                    (5, 0),
                    (5, 1),
                    (5, 2),
                    (5, 3),
                    (5, 4),
                    (5, 5),
                    (5, 6),
                    (5, 7),
                    (5, 8),
                ],
            ),
            (
                6,
                [
                    (6, 0),
                    (6, 1),
                    (6, 2),
                    (6, 3),
                    (6, 4),
                    (6, 5),
                    (6, 6),
                    (6, 7),
                    (6, 8),
                ],
            ),
            (
                7,
                [
                    (7, 0),
                    (7, 1),
                    (7, 2),
                    (7, 3),
                    (7, 4),
                    (7, 5),
                    (7, 6),
                    (7, 7),
                    (7, 8),
                ],
            ),
            (
                8,
                [
                    (8, 0),
                    (8, 1),
                    (8, 2),
                    (8, 3),
                    (8, 4),
                    (8, 5),
                    (8, 6),
                    (8, 7),
                    (8, 8),
                ],
            ),
        ],
    )
    def test_expected(self, row, expected):
        assert row_cells(row) == expected


class TestColumnCells:
    @pytest.mark.parametrize(
        "column,expected",
        [
            (
                0,
                [
                    (0, 0),
                    (1, 0),
                    (2, 0),
                    (3, 0),
                    (4, 0),
                    (5, 0),
                    (6, 0),
                    (7, 0),
                    (8, 0),
                ],
            ),
            (
                1,
                [
                    (0, 1),
                    (1, 1),
                    (2, 1),
                    (3, 1),
                    (4, 1),
                    (5, 1),
                    (6, 1),
                    (7, 1),
                    (8, 1),
                ],
            ),
            (
                2,
                [
                    (0, 2),
                    (1, 2),
                    (2, 2),
                    (3, 2),
                    (4, 2),
                    (5, 2),
                    (6, 2),
                    (7, 2),
                    (8, 2),
                ],
            ),
            (
                3,
                [
                    (0, 3),
                    (1, 3),
                    (2, 3),
                    (3, 3),
                    (4, 3),
                    (5, 3),
                    (6, 3),
                    (7, 3),
                    (8, 3),
                ],
            ),
            (
                4,
                [
                    (0, 4),
                    (1, 4),
                    (2, 4),
                    (3, 4),
                    (4, 4),
                    (5, 4),
                    (6, 4),
                    (7, 4),
                    (8, 4),
                ],
            ),
            (
                5,
                [
                    (0, 5),
                    (1, 5),
                    (2, 5),
                    (3, 5),
                    (4, 5),
                    (5, 5),
                    (6, 5),
                    (7, 5),
                    (8, 5),
                ],
            ),
            (
                6,
                [
                    (0, 6),
                    (1, 6),
                    (2, 6),
                    (3, 6),
                    (4, 6),
                    (5, 6),
                    (6, 6),
                    (7, 6),
                    (8, 6),
                ],
            ),
            (
                7,
                [
                    (0, 7),
                    (1, 7),
                    (2, 7),
                    (3, 7),
                    (4, 7),
                    (5, 7),
                    (6, 7),
                    (7, 7),
                    (8, 7),
                ],
            ),
            (
                8,
                [
                    (0, 8),
                    (1, 8),
                    (2, 8),
                    (3, 8),
                    (4, 8),
                    (5, 8),
                    (6, 8),
                    (7, 8),
                    (8, 8),
                ],
            ),
        ],
    )
    def test_expected(self, column, expected):
        assert column_cells(column) == expected


class TestBoxCells:
    @pytest.mark.parametrize(
        "box,expected",
        [
            (
                0,
                [
                    (0, 0),
                    (0, 1),
                    (0, 2),
                    (1, 0),
                    (1, 1),
                    (1, 2),
                    (2, 0),
                    (2, 1),
                    (2, 2),
                ],
            ),
            (
                1,
                [
                    (0, 3),
                    (0, 4),
                    (0, 5),
                    (1, 3),
                    (1, 4),
                    (1, 5),
                    (2, 3),
                    (2, 4),
                    (2, 5),
                ],
            ),
            (
                2,
                [
                    (0, 6),
                    (0, 7),
                    (0, 8),
                    (1, 6),
                    (1, 7),
                    (1, 8),
                    (2, 6),
                    (2, 7),
                    (2, 8),
                ],
            ),
            (
                3,
                [
                    (3, 0),
                    (3, 1),
                    (3, 2),
                    (4, 0),
                    (4, 1),
                    (4, 2),
                    (5, 0),
                    (5, 1),
                    (5, 2),
                ],
            ),
            (
                4,
                [
                    (3, 3),
                    (3, 4),
                    (3, 5),
                    (4, 3),
                    (4, 4),
                    (4, 5),
                    (5, 3),
                    (5, 4),
                    (5, 5),
                ],
            ),
            (
                5,
                [
                    (3, 6),
                    (3, 7),
                    (3, 8),
                    (4, 6),
                    (4, 7),
                    (4, 8),
                    (5, 6),
                    (5, 7),
                    (5, 8),
                ],
            ),
            (
                6,
                [
                    (6, 0),
                    (6, 1),
                    (6, 2),
                    (7, 0),
                    (7, 1),
                    (7, 2),
                    (8, 0),
                    (8, 1),
                    (8, 2),
                ],
            ),
            (
                7,
                [
                    (6, 3),
                    (6, 4),
                    (6, 5),
                    (7, 3),
                    (7, 4),
                    (7, 5),
                    (8, 3),
                    (8, 4),
                    (8, 5),
                ],
            ),
            (
                8,
                [
                    (6, 6),
                    (6, 7),
                    (6, 8),
                    (7, 6),
                    (7, 7),
                    (7, 8),
                    (8, 6),
                    (8, 7),
                    (8, 8),
                ],
            ),
        ],
    )
    def test_expected(self, box, expected):
        assert box_cells(box) == expected


class TestRowNumbers:
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


class TestColumnNumbers:
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


class TestBoxNumbers:
    @pytest.mark.parametrize("row, col", [(r, c) for r in range(9) for c in range(9)])
    def test_all_solved(self, simple_grid, row, col):
        assert box_digits(simple_grid, row, col) == set(range(1, 10))

    @pytest.mark.parametrize(
        "row, col", [(r, c) for r in range(0, 9, 3) for c in range(0, 9, 3)]
    )
    def test_some_solved(self, simple_grid, row, col):
        remove = (row + random.randint(0, 2), col + random.randint(0, 2))
        check = (row + random.randint(0, 2), col + random.randint(0, 2))
        simple_grid[remove] = 0
        assert box_digits(simple_grid, *check) == set(
            digit
            for digit in simple_grid[row : row + 3, col : col + 3].flatten()
            if digit != 0
        )

    @pytest.mark.parametrize("row, col", [(r, c) for r in range(9) for c in range(9)])
    def test_none_solved(self, simple_grid, row, col):
        simple_grid[:, :] = 0
        assert box_digits(simple_grid, row, col) == set()


class TestPeerNumbers:
    @pytest.mark.parametrize("row, col", [(r, c) for r in range(9) for c in range(9)])
    def test_cell_digit_not_included(self, simple_grid, row, col):
        assert simple_grid[row, col] not in peer_digits(simple_grid, row, col)

    @pytest.mark.parametrize("row, col", [(r, c) for r in range(9) for c in range(9)])
    def test_non_cell_digit_included(self, simple_grid, row, col):
        assert peer_digits(simple_grid, row, col) == {
            digit for digit in range(1, 10) if digit != simple_grid[row, col]
        }


class TestPeerRowCells:
    def test_correct_peers(self):
        peer_cols = [c for c in range(9)]
        random.shuffle(peer_cols)
        col = peer_cols.pop()
        row = random.randint(0, 8)
        peers = peer_row_cells(row, col)
        assert {(row, c) for c in peer_cols} == peers


class TestPeerColumnCells:
    def test_correct_peers(self):
        peer_rows = [c for c in range(9)]
        random.shuffle(peer_rows)
        row = peer_rows.pop()
        col = random.randint(0, 8)
        peers = peer_column_cells(row, col)
        assert {(r, col) for r in peer_rows} == peers


class TestPeerBoxCells:
    def test_correct_peers(self):
        peers = peer_box_cells(3, 3)
        assert {
            (r, c) for r in range(3, 6) for c in range(3, 6) if not (r == c == 3)
        } == peers


class TestPeerCells:
    def test_correct_peers(self):
        peers = peer_cells(0, 3)
        assert peers == {(0, c) for c in range(9) if c != 3}.union(
            (r, 3) for r in range(9) if r != 0
        ).union({(1, 4), (1, 5), (2, 4), (2, 5)})


class TestIsSolved:
    def test_solved_valid(self, simple_grid):
        assert is_solved(simple_grid)

    def test_solved_invalid_row(self, simple_grid):
        simple_grid[0, :] = np.ones(9)
        assert not is_solved(simple_grid)

    def test_solved_invalid_col(self, simple_grid):
        simple_grid[:] = np.array(range(1, 10))
        assert not is_solved(simple_grid)

    def test_solved_invalid_box(self, simple_grid):
        for i in range(9):
            simple_grid[i, :] = np.roll(np.array(range(1, 10)), -i)
        assert not is_solved(simple_grid)

    def test_unsolved(self, simple_grid):
        simple_grid[0, 0] = 0
        assert not is_solved(simple_grid)


class TestBruteForceSolution:
    def test_from_empty(self):

        grid = np.zeros([9, 9])
        solution = brute_force_solution(grid)
        assert is_solved(solution)

    def test_simple_problem(self, simple_grid):
        test_grid = np.copy(simple_grid)
        test_grid[0, 5] = 0
        solution = brute_force_solution(test_grid)
        assert np.array_equal(solution, simple_grid)

    def test_unsolveable_problem(self):
        grid = np.ones([9, 9])
        grid[0, 0] = 0
        assert not brute_force_solution(grid)


class TestBruteForceSolutions:
    def test_from_empty(self):
        grid = np.zeros([9, 9])
        solution = next(brute_force_solutions(grid))
        assert is_solved(solution)

    def test_simple_problem(self, simple_grid):
        test_grid = np.copy(simple_grid)
        test_grid[0, 5] = 0
        solution = next(brute_force_solutions(test_grid))
        assert np.array_equal(solution, simple_grid)

    def test_multiple_solutions(self):
        grid = np.zeros([9, 9])
        solution = brute_force_solutions(grid)
        solution_a, solution_b = next(solution), next(solution)
        assert not np.array_equal(solution_a, solution_b)


class TestHasUniqueSolution:
    def test_solved(self, simple_grid):
        assert has_unique_solution(simple_grid)

    def test_unique(self, simple_grid):
        simple_grid[np.where(simple_grid == 1)] = 0
        assert has_unique_solution(simple_grid)

    def test_non_unique(self, simple_grid):
        simple_grid[np.where(simple_grid == 1)] = 0
        simple_grid[np.where(simple_grid == 2)] = 0
        assert not has_unique_solution(simple_grid)

    def test_unsolveable(self):
        grid = np.ones([9, 9])
        grid[0, 0] = 0
        assert not has_unique_solution(grid)


class TestCreateCandidateGrid:
    def test_solved(self, simple_grid):
        candidates = create_candidate_grid(simple_grid)
        assert all(
            candidates[r, c].pop() == simple_grid[r, c]
            for r in range(9)
            for c in range(9)
        )

    def test_unsolved(self, simple_grid):
        simple_grid[0, :] = 0
        simple_grid[1, :] = 0
        candidates = create_candidate_grid(simple_grid)
        assert all(len(candidates[r, c]) == 2 for r in range(2) for c in range(9))
        assert all(
            candidates[r, c].pop() == simple_grid[r, c]
            for r in range(2, 9)
            for c in range(9)
        )

import random
import pytest
import numpy as np
from pyslab.puzzle_grid import (
    unsolved_elements,
    solved_elements,
    row_elements,
    column_elements,
    nonet_elements,
    row_numbers,
    column_numbers,
    nonet_numbers,
    peer_numbers,
    peer_row_elements,
    peer_column_elements,
    peer_nonet_elements,
    peer_elements,
    is_solved,
    brute_force_solution,
    brute_force_solutions,
    has_unique_solution,
    create_candidate_grid,
)


class TestUnsolvedElements:
    """Test behaviour of unsolved elements method"""

    def test_no_unsolved(self, simple_puzzle):
        with pytest.raises(StopIteration):
            next(unsolved_elements(simple_puzzle))

    def test_one_unsolved(self, simple_puzzle):
        simple_puzzle[0, 0] = 0
        to_solve = unsolved_elements(simple_puzzle)
        _ = next(to_solve)
        with pytest.raises(StopIteration):
            _ = next(to_solve)

    def test_multi_unsolved(self, simple_puzzle):
        simple_puzzle[0:3, 0] = 0
        to_solve = unsolved_elements(simple_puzzle)
        for _ in range(3):
            _ = next(to_solve)
        with pytest.raises(StopIteration):
            _ = next(to_solve)


class TestSolvedElements:
    """Test behaviour of solved elements method"""

    def test_all_solved(self, simple_puzzle):
        assert len(list(solved_elements(simple_puzzle))) == 81

    def test_one_unsolved(self, simple_puzzle):
        simple_puzzle[0, 0] = 0
        solved = list(solved_elements(simple_puzzle))
        assert len(solved) == 80
        assert (0, 0) not in solved

    def test_multi_unsolved(self, simple_puzzle):
        simple_puzzle[0:3, :] = 0
        solved = list(solved_elements(simple_puzzle))
        assert all((r, c) in solved for r in range(3, 9) for c in range(9))
        assert all((r, c) not in solved for r in range(3) for c in range(9))


class TestRowElements:
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
        assert row_elements(row) == expected


class TestColumnElements:
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
        assert column_elements(column) == expected


class TestNonetElements:
    @pytest.mark.parametrize(
        "nonet,expected",
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
    def test_expected(self, nonet, expected):
        assert nonet_elements(nonet) == expected


class TestRowNumbers:
    @pytest.mark.parametrize("row", list(range(9)))
    def test_all_solved(self, simple_puzzle, row):
        assert row_numbers(simple_puzzle, row) == set(range(1, 10))

    @pytest.mark.parametrize("row", list(range(9)))
    def test_some_solved(self, simple_puzzle, row):
        simple_puzzle[row, ::2] = 0
        assert row_numbers(simple_puzzle, row) == set(simple_puzzle[row, 1::2])

    @pytest.mark.parametrize("row", list(range(9)))
    def test_none_solved(self, simple_puzzle, row):
        simple_puzzle[row, :] = 0
        assert row_numbers(simple_puzzle, row) == set()


class TestColumnNumbers:
    @pytest.mark.parametrize("col", list(range(9)))
    def test_all_solved(self, simple_puzzle, col):
        assert column_numbers(simple_puzzle, col) == set(range(1, 10))

    @pytest.mark.parametrize("col", list(range(9)))
    def test_some_solved(self, simple_puzzle, col):
        simple_puzzle[::2, col] = 0
        assert column_numbers(simple_puzzle, col) == set(simple_puzzle[1::2, col])

    @pytest.mark.parametrize("col", list(range(9)))
    def test_none_solved(self, simple_puzzle, col):
        simple_puzzle[:, col] = 0
        assert column_numbers(simple_puzzle, col) == set()


class TestNonetNumbers:
    @pytest.mark.parametrize("row, col", [(r, c) for r in range(9) for c in range(9)])
    def test_all_solved(self, simple_puzzle, row, col):
        assert nonet_numbers(simple_puzzle, row, col) == set(range(1, 10))

    @pytest.mark.parametrize(
        "row, col", [(r, c) for r in range(0, 9, 3) for c in range(0, 9, 3)]
    )
    def test_some_solved(self, simple_puzzle, row, col):
        remove = (row + random.randint(0, 2), col + random.randint(0, 2))
        check = (row + random.randint(0, 2), col + random.randint(0, 2))
        simple_puzzle[remove] = 0
        assert nonet_numbers(simple_puzzle, *check) == set(
            num
            for num in simple_puzzle[row : row + 3, col : col + 3].flatten()
            if num != 0
        )

    @pytest.mark.parametrize("row, col", [(r, c) for r in range(9) for c in range(9)])
    def test_none_solved(self, simple_puzzle, row, col):
        simple_puzzle[:, :] = 0
        assert nonet_numbers(simple_puzzle, row, col) == set()


class TestPeerNumbers:
    @pytest.mark.parametrize("row, col", [(r, c) for r in range(9) for c in range(9)])
    def test_element_number_not_included(self, simple_puzzle, row, col):
        assert simple_puzzle[row, col] not in peer_numbers(simple_puzzle, row, col)

    @pytest.mark.parametrize("row, col", [(r, c) for r in range(9) for c in range(9)])
    def test_non_element_number_included(self, simple_puzzle, row, col):
        assert peer_numbers(simple_puzzle, row, col) == {
            num for num in range(1, 10) if num != simple_puzzle[row, col]
        }


class TestPeerRowElements:
    def test_correct_peers(self):
        peer_cols = [c for c in range(9)]
        random.shuffle(peer_cols)
        col = peer_cols.pop()
        row = random.randint(0, 8)
        peers = peer_row_elements(row, col)
        assert {(row, c) for c in peer_cols} == peers


class TestPeerColumnElements:
    def test_correct_peers(self):
        peer_rows = [c for c in range(9)]
        random.shuffle(peer_rows)
        row = peer_rows.pop()
        col = random.randint(0, 8)
        peers = peer_column_elements(row, col)
        assert {(r, col) for r in peer_rows} == peers


class TestPeerNonetElements:
    def test_correct_peers(self):
        peers = peer_nonet_elements(3, 3)
        assert {
            (r, c) for r in range(3, 6) for c in range(3, 6) if not (r == c == 3)
        } == peers


class TestPeerElements:
    def test_correct_peers(self):
        peers = peer_elements(0, 3)
        assert peers == {(0, c) for c in range(9) if c != 3}.union(
            (r, 3) for r in range(9) if r != 0
        ).union({(1, 4), (1, 5), (2, 4), (2, 5)})


class TestIsSolved:
    def test_solved_valid(self, simple_puzzle):
        assert is_solved(simple_puzzle)

    def test_solved_invalid_row(self, simple_puzzle):
        simple_puzzle[0, :] = np.ones(9)
        assert not is_solved(simple_puzzle)

    def test_solved_invalid_col(self, simple_puzzle):
        simple_puzzle[:] = np.array(range(1, 10))
        assert not is_solved(simple_puzzle)

    def test_solved_invalid_nonet(self, simple_puzzle):
        for i in range(9):
            simple_puzzle[i, :] = np.roll(np.array(range(1, 10)), -i)
        assert not is_solved(simple_puzzle)

    def test_unsolved(self, simple_puzzle):
        simple_puzzle[0, 0] = 0
        assert not is_solved(simple_puzzle)


class TestBruteForceSolution:
    def test_from_empty(self):

        puzzle = np.zeros([9, 9])
        solution = brute_force_solution(puzzle)
        assert is_solved(solution)

    def test_simple_problem(self, simple_puzzle):
        test_puzzle = np.copy(simple_puzzle)
        test_puzzle[0, 5] = 0
        solution = brute_force_solution(test_puzzle)
        assert np.array_equal(solution, simple_puzzle)

    def test_unsolveable_problem(self):
        puzzle = np.ones([9, 9])
        puzzle[0, 0] = 0
        assert not brute_force_solution(puzzle)


class TestBruteForceSolutions:
    def test_from_empty(self):
        puzzle = np.zeros([9, 9])
        solution = next(brute_force_solutions(puzzle))
        assert is_solved(solution)

    def test_simple_problem(self, simple_puzzle):
        test_puzzle = np.copy(simple_puzzle)
        test_puzzle[0, 5] = 0
        solution = next(brute_force_solutions(test_puzzle))
        assert np.array_equal(solution, simple_puzzle)

    def test_multiple_solutions(self):
        puzzle = np.zeros([9, 9])
        solution = brute_force_solutions(puzzle)
        solution_a, solution_b = next(solution), next(solution)
        assert not np.array_equal(solution_a, solution_b)


class TestHasUniqueSolution:
    def test_solved(self, simple_puzzle):
        assert has_unique_solution(simple_puzzle)

    def test_unique(self, simple_puzzle):
        simple_puzzle[np.where(simple_puzzle == 1)] = 0
        assert has_unique_solution(simple_puzzle)

    def test_non_unique(self, simple_puzzle):
        simple_puzzle[np.where(simple_puzzle == 1)] = 0
        simple_puzzle[np.where(simple_puzzle == 2)] = 0
        assert not has_unique_solution(simple_puzzle)

    def test_unsolveable(self):
        puzzle = np.ones([9, 9])
        puzzle[0, 0] = 0
        assert not has_unique_solution(puzzle)


class TestCreateCandidateGrid:
    def test_solved(self, simple_puzzle):
        candidates = create_candidate_grid(simple_puzzle)
        assert all(
            candidates[r, c].pop() == simple_puzzle[r, c]
            for r in range(9)
            for c in range(9)
        )

    def test_unsolved(self, simple_puzzle):
        simple_puzzle[0, :] = 0
        simple_puzzle[1, :] = 0
        candidates = create_candidate_grid(simple_puzzle)
        assert all(len(candidates[r, c]) == 2 for r in range(2) for c in range(9))
        assert all(
            candidates[r, c].pop() == simple_puzzle[r, c]
            for r in range(2, 9)
            for c in range(9)
        )

"""Find naked singles"""
from typing import Tuple, List, Callable
from collections import Counter
import numpy as np
from pyslab.puzzle_grid import row_elements, column_elements, nonet_elements


def _count_candidates_in_elements(
    puzzle: np.ndarray, candidates: np.ndarray, elements: List[Tuple[int, int]]
) -> Counter:
    return Counter(
        num
        for element in elements
        for num in candidates[element]
        if puzzle[element] == 0  # only for unsolved elements
    )


def _find_in_elements(
    puzzle: np.ndarray,
    candidates: np.ndarray,
    f_elements: Callable[[int], List[Tuple[int, int]]],
):
    row_elems = {row: f_elements(row) for row in range(9)}

    row_singles = {
        row: [
            num
            for num, cnt in _count_candidates_in_elements(
                puzzle, candidates, row_elems[row]
            ).items()
            if cnt == 1
        ]
        for row in range(9)
    }

    return [
        (elem, single)
        for row in range(9)
        for elem in row_elems[row]
        for single in row_singles[row]
        if single in candidates[elem]
    ]


def find_in_rows(
    puzzle: np.ndarray, candidates: np.ndarray
) -> List[Tuple[Tuple[int, int], int]]:
    """
    Find all naked singles in puzzle rows

    Args:
        puzzle: 2-d array sudoku puzzle
        candidates: 2-d array sudoku candidates

    Returns:
        List of (row,col) -> number
    """
    return _find_in_elements(puzzle, candidates, row_elements)


def find_in_columns(
    puzzle: np.ndarray, candidates: np.ndarray
) -> List[Tuple[Tuple[int, int], int]]:
    """
    Find all naked singles in puzzle columns

    Args:
        puzzle: 2-d array sudoku puzzle
        candidates: 2-d array sudoku candidates

    Returns:
        List of (row,col) -> number
    """

    return _find_in_elements(puzzle, candidates, column_elements)


def find_in_nonets(
    puzzle: np.ndarray, candidates: np.ndarray
) -> List[Tuple[Tuple[int, int], int]]:
    """
    Find all naked singles in puzzle nonets

    Args:
        puzzle: 2-d array sudoku puzzle
        candidates: 2-d array sudoku candidates

    Returns:
        List of (row,col) -> number
    """

    return _find_in_elements(puzzle, candidates, nonet_elements)

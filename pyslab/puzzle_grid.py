"""Sudoku puzzle grid inspection and manipulation"""
from typing import Iterator, Tuple, Set, Generator, Any, List
import numpy as np


def unsolved_elements(puzzle: np.ndarray) -> Iterator[Tuple[int, int]]:
    """
    Find all unsolved elements within a puzzle
    Args:
        puzzle: 2-d array sudoku puzzle

    Returns:
        Iterator of (row, col) element ids
    """
    return zip(*np.where(puzzle == 0))


def solved_elements(puzzle: np.ndarray) -> Iterator[Tuple[int, int]]:
    """
    Find all solved elements within a puzzle
    Args:
        puzzle: 2-d array sudoku puzzle

    Returns:
        Iterator of (row, col) element ids
    """
    return zip(*np.where(puzzle > 0))


def row_elements(row: int) -> List[Tuple[int, int]]:
    return [(row, c) for c in range(9)]


def column_elements(column: int) -> List[Tuple[int, int]]:
    return [(r, column) for r in range(9)]


def nonet_elements(nonet: int) -> List[Tuple[int, int]]:
    corner_r, corner_c = nonet // 3 * 3, nonet % 3 * 3
    return [
        (r, c)
        for r in range(corner_r, corner_r + 3)
        for c in range(corner_c, corner_c + 3)
    ]


def row_numbers(puzzle: np.ndarray, row: int) -> Set[int]:
    """
    Find all numbers in a row
    Args:
        puzzle: 2-d array sudoku puzzle
        row: row-index to search

    Returns:
        Set of all numbers in a row
    """
    return set(puzzle[row, :]) - {0}


def column_numbers(puzzle: np.ndarray, col: int) -> Set[int]:
    """
    Find all numbers in a column
    Args:
        puzzle: 2-d array sudoku puzzle
        col: column-index to search

    Returns:
        Set of all numbers in a column
    """
    return set(puzzle[:, col]) - {0}


def nonet_numbers(puzzle: np.ndarray, row: int, col: int) -> Set[int]:
    """
    Find all numbers in a nonet with specified row/col element in it
    Args:
        puzzle: 2-d array sudoku puzzle
        row: row-index to identify nonet
        col: column-index to identify nonet

    Returns:
        Set of all numbers in a nonet
    """
    r, c = row // 3 * 3, col // 3 * 3
    return set(puzzle[r : r + 3, c : c + 3].flatten()) - {0}


def peer_numbers(puzzle: np.ndarray, row: int, col: int) -> Set[int]:
    """
    Find all numbers in a peer group of row / column / nonet
    Args:
        puzzle: 2-d array sudoku puzzle
        row: row-index
        col: column-index
    See Also:
        row_values
        col_values
        nonet_values
    Returns:
        Set of all numbers in a nonet
    """
    return row_numbers(puzzle, row).union(column_numbers(puzzle, col)).union(
        nonet_numbers(puzzle, row, col)
    ) - {puzzle[row, col]}


def peer_row_elements(row: int, col: int) -> Set[Tuple[int, int]]:
    return {(row, c) for c in range(9) if c != col}


def peer_column_elements(row: int, col: int) -> Set[Tuple[int, int]]:
    return {(r, col) for r in range(9) if r != row}


def peer_nonet_elements(row: int, col: int) -> Set[Tuple[int, int]]:
    corner_r, corner_c = row // 3 * 3, col // 3 * 3
    return {
        (r, c)
        for r in range(corner_r, corner_r + 3)
        for c in range(corner_c, corner_c + 3)
        if not (r == row and c == col)
    }


def peer_elements(row: int, col: int) -> Set[Tuple[int, int]]:

    return (
        peer_row_elements(row, col)
        .union(peer_column_elements(row, col))
        .union(peer_nonet_elements(row, col))
    )


def is_solved(puzzle: np.ndarray) -> bool:
    """
    Check if a puzzle has been solved completely
    Args:
        puzzle: 2-d array sudoku puzzle

    Returns:
        True if the puzzle is completely solved
    """

    numbers = set(range(1, 10))

    # rows
    if not all(set(puzzle[row, :]) == numbers for row in range(9)):
        return False

    # cols
    if not all(set(puzzle[:, col]) == numbers for col in range(9)):
        return False

    # nonets
    if not all(
        set(puzzle[i : i + 3, j : j + 3].flatten()) == numbers
        for i in range(0, 9, 3)
        for j in range(0, 9, 3)
    ):
        return False

    return True


def brute_force_solutions(puzzle: np.ndarray) -> Generator[np.ndarray, Any, None]:
    """
    Generate brute force solutions to an unsolved puzzle
    Args:
        puzzle: 2-d array sudoku puzzle

    Returns:
        Solved puzzles
    """
    try:
        next_to_solve = next(unsolved_elements(puzzle))
        possible_values = set(range(1, 10)) - peer_numbers(puzzle, *next_to_solve)

        for v in possible_values:
            possible_puzzle = np.copy(puzzle)
            possible_puzzle[next_to_solve] = v
            yield from brute_force_solutions(possible_puzzle)
    except StopIteration:
        if is_solved(puzzle):
            yield puzzle


def brute_force_solution(puzzle: np.ndarray):
    """
    Find single solution by brute force search
    Args:
        puzzle: 2-d array sudoku puzzle

    Returns:
        Solved puzzle
    """
    try:
        return next(brute_force_solutions(puzzle))
    except StopIteration:
        return None


def has_unique_solution(puzzle: np.ndarray) -> bool:
    """
    Check if puzzle has a unique solution
    Args:
        puzzle: 2-d array sudoku puzzle

    Returns:
        True if puzzle has a unique solution
    """
    solutions = brute_force_solutions(puzzle)
    try:
        _ = next(solutions)
    except StopIteration:
        return False

    try:
        _ = next(solutions)
        return False
    except StopIteration:
        return True


def create_candidate_grid(puzzle: np.ndarray) -> np.ndarray:
    """
    Generate a 2-d array of candidate Sets. Each element in the
    array contains a set of candidates that may occur in that
    position. A fully solved puzzle will return a candidate
    grid of single-element sets.

    Args:
        puzzle: 2-d array sudoku puzzle

    Returns:
        Candidate grid
    """
    return np.array(
        [
            [
                set(range(1, 10)) - peer_numbers(puzzle, r, c)
                if puzzle[r, c] == 0
                else {puzzle[r, c]}
                for c in range(9)
            ]
            for r in range(9)
        ]
    )

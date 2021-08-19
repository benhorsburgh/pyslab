from typing import Generator, Any, Iterator

import numpy as np

from ..core.digits import peer_digits
from ..core.types import Cell


def is_solved(grid: np.ndarray) -> bool:
    """
    Check if a core has been solved completely
    Args:
        grid: 2-d array sudoku core

    Returns:
        True if the core is completely solved
    """

    digits = set(range(1, 10))

    # rows
    if not all(set(grid[row, :]) == digits for row in range(9)):
        return False

    # cols
    if not all(set(grid[:, col]) == digits for col in range(9)):
        return False

    # boxes
    if not all(
        set(grid[i : i + 3, j : j + 3].flatten()) == digits
        for i in range(0, 9, 3)
        for j in range(0, 9, 3)
    ):
        return False

    return True


def brute_force_solutions(grid: np.ndarray) -> Generator[np.ndarray, Any, None]:
    """
    Generate brute force solutions to an unsolved core
    Args:
        grid: 2-d array sudoku core

    Returns:
        Solved grids
    """
    try:
        next_to_solve = next(unsolved_cells(grid))
        possible_values = set(range(1, 10)) - peer_digits(grid, next_to_solve)

        for v in possible_values:
            possible_grid = np.copy(grid)
            possible_grid[next_to_solve] = v
            yield from brute_force_solutions(possible_grid)
    except StopIteration:
        if is_solved(grid):
            yield grid


def brute_force_solution(grid: np.ndarray):
    """
    Find single solution by brute force search
    Args:
        grid: 2-d array sudoku core

    Returns:
        Solved core
    """
    try:
        return next(brute_force_solutions(grid))
    except StopIteration:
        return None


def has_unique_solution(grid: np.ndarray) -> bool:
    """
    Check if core has a unique solution
    Args:
        grid: 2-d array sudoku core

    Returns:
        True if core has a unique solution
    """
    solutions = brute_force_solutions(grid)
    try:
        _ = next(solutions)
    except StopIteration:
        return False

    try:
        _ = next(solutions)
        return False
    except StopIteration:
        return True


def unsolved_cells(grid: np.ndarray) -> Iterator[Cell]:
    """
    Find all unsolved cells within a core
    Args:
        grid: 2-d array sudoku core

    Returns:
        Iterator of (row, col) cell ids
    """
    return iter(Cell(row, column) for row, column in zip(*np.where(grid == 0)))


def solved_cells(grid: np.ndarray) -> Iterator[Cell]:
    """
    Find all solved cells within a core
    Args:
        grid: 2-d array sudoku core

    Returns:
        Iterator of (row, col) cell ids
    """
    return iter(Cell(row, column) for row, column in zip(*np.where(grid > 0)))

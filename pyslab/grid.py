"""Sudoku grid inspection and manipulation"""
from typing import Iterator, Tuple, Set, Generator, Any, List
import numpy as np


def unsolved_cells(grid: np.ndarray) -> Iterator[Tuple[int, int]]:
    """
    Find all unsolved cells within a grid
    Args:
        grid: 2-d array sudoku grid

    Returns:
        Iterator of (row, col) cell ids
    """
    return zip(*np.where(grid == 0))


def solved_cells(grid: np.ndarray) -> Iterator[Tuple[int, int]]:
    """
    Find all solved cells within a grid
    Args:
        grid: 2-d array sudoku grid

    Returns:
        Iterator of (row, col) cell ids
    """
    return zip(*np.where(grid > 0))


def row_cells(row: int) -> List[Tuple[int, int]]:
    return [(row, c) for c in range(9)]


def column_cells(column: int) -> List[Tuple[int, int]]:
    return [(r, column) for r in range(9)]


def box_cells(box: int) -> List[Tuple[int, int]]:
    corner_r, corner_c = box // 3 * 3, box % 3 * 3
    return [
        (r, c)
        for r in range(corner_r, corner_r + 3)
        for c in range(corner_c, corner_c + 3)
    ]


def row_houses() -> List[int]:
    return list(range(9))


def column_houses() -> List[int]:
    return list(range(10, 18))


def box_houses() -> List[int]:
    return list(range(19, 27))


def house_cells(house: int) -> List[Tuple[int, int]]:
    if house // 9 == 0:
        return row_cells(house)
    if house // 9 == 1:
        return column_cells(house - 9)
    return box_cells(house - 18)


def row_digits(grid: np.ndarray, row: int) -> Set[int]:
    """
    Find all digits in a row
    Args:
        grid: 2-d array sudoku grid
        row: row-index to search

    Returns:
        Set of all digits in a row
    """
    return set(grid[row, :]) - {0}


def column_digits(grid: np.ndarray, col: int) -> Set[int]:
    """
    Find all digits in a column
    Args:
        grid: 2-d array sudoku grid
        col: column-index to search

    Returns:
        Set of all digits in a column
    """
    return set(grid[:, col]) - {0}


def box_digits(grid: np.ndarray, row: int, col: int) -> Set[int]:
    """
    Find all digits in a box with specified row/col cell in it
    Args:
        grid: 2-d array sudoku grid
        row: row-index to identify box
        col: column-index to identify box

    Returns:
        Set of all digits in a box
    """
    r, c = row // 3 * 3, col // 3 * 3
    return set(grid[r : r + 3, c : c + 3].flatten()) - {0}


def peer_digits(grid: np.ndarray, row: int, col: int) -> Set[int]:
    """
    Find all digits in a peer group of row / column / box
    Args:
        grid: 2-d array sudoku grid
        row: row-index
        col: column-index
    See Also:
        row_values
        col_values
        box
    Returns:
        Set of all digits in a box
    """
    return row_digits(grid, row).union(column_digits(grid, col)).union(
        box_digits(grid, row, col)
    ) - {grid[row, col]}


def peer_row_cells(row: int, col: int) -> Set[Tuple[int, int]]:
    return {(row, c) for c in range(9) if c != col}


def peer_column_cells(row: int, col: int) -> Set[Tuple[int, int]]:
    return {(r, col) for r in range(9) if r != row}


def peer_box_cells(row: int, col: int) -> Set[Tuple[int, int]]:
    corner_r, corner_c = row // 3 * 3, col // 3 * 3
    return {
        (r, c)
        for r in range(corner_r, corner_r + 3)
        for c in range(corner_c, corner_c + 3)
        if not (r == row and c == col)
    }


def peer_cells(row: int, col: int) -> Set[Tuple[int, int]]:

    return (
        peer_row_cells(row, col)
        .union(peer_column_cells(row, col))
        .union(peer_box_cells(row, col))
    )


def is_solved(grid: np.ndarray) -> bool:
    """
    Check if a grid has been solved completely
    Args:
        grid: 2-d array sudoku grid

    Returns:
        True if the grid is completely solved
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
    Generate brute force solutions to an unsolved grid
    Args:
        grid: 2-d array sudoku grid

    Returns:
        Solved grids
    """
    try:
        next_to_solve = next(unsolved_cells(grid))
        possible_values = set(range(1, 10)) - peer_digits(grid, *next_to_solve)

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
        grid: 2-d array sudoku grid

    Returns:
        Solved grid
    """
    try:
        return next(brute_force_solutions(grid))
    except StopIteration:
        return None


def has_unique_solution(grid: np.ndarray) -> bool:
    """
    Check if grid has a unique solution
    Args:
        grid: 2-d array sudoku grid

    Returns:
        True if grid has a unique solution
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


def create_candidate_grid(grid: np.ndarray) -> np.ndarray:
    """
    Generate a 2-d array of candidate Sets. Each cell in the
    array contains a set of candidates that may occur in that
    position. A fully solved grid will return a candidate
    grid of single-cell sets.

    Args:
        grid: 2-d array sudoku grid

    Returns:
        Candidate grid
    """
    return np.array(
        [
            [
                set(range(1, 10)) - peer_digits(grid, r, c)
                if grid[r, c] == 0
                else {grid[r, c]}
                for c in range(9)
            ]
            for r in range(9)
        ]
    )

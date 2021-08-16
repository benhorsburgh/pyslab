from typing import Set
from .types import Cell
from .cells import row_cells, column_cells, box_cells
from .peers import all_peer_cells

import numpy as np


def row_digits(grid: np.ndarray, row: int) -> Set[int]:
    """
    Find all digits in a row
    Args:
        grid: 2-d array sudoku core
        row: row-index to search

    Returns:
        Set of all digits in a row
    """
    return set(grid[list(zip(*row_cells(row)))]) - {0}


def column_digits(grid: np.ndarray, column: int) -> Set[int]:
    """
    Find all digits in a column
    Args:
        grid: 2-d array sudoku core
        column: column-index to search

    Returns:
        Set of all digits in a column
    """
    return set(grid[list(zip(*column_cells(column)))]) - {0}


def box_digits(grid: np.ndarray, box: int) -> Set[int]:
    """
    Find all digits in a box with specified row/col cell in it
    Args:
        grid: 2-d array sudoku core
        box: box-index to search

    Returns:
        Set of all digits in a box
    """
    return set(grid[list(zip(*box_cells(box)))]) - {0}


def peer_digits(grid: np.ndarray, cell: Cell) -> Set[int]:
    """
    Find all digits in a peer group of row / column / box
    Args:
        grid: 2-d array sudoku core
        cell: the cell to find peers
    Returns:
        Set of all digits in a box
    """
    return set(grid[list(zip(*all_peer_cells(cell)))]) - {0} - {grid[cell]}

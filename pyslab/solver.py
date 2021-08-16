"""Sudoku Solver"""
import numpy as np

from core.digits import peer_digits
from pyslab.strategies import hidden_singles, naked_singles
from core.locations import row_house_ids, column_house_ids, box_house_ids
from core.types import Cell
from core.peers import all_peer_cells


def solve(grid: np.ndarray):

    candidates = create_candidate_grid(grid)

    progress = True

    while progress:
        progress = False

        for row, house in enumerate(row_house_ids()):
            for cell, digit in naked_singles.find_placements(grid, candidates, house):
                progress = True
                print(f"Naked single in row {row}", cell, digit)
                set_cell(grid, candidates, cell, digit)

            for cell, digit in hidden_singles.find_placements(grid, candidates, house):
                progress = True
                print(f"Hidden single in row {row}", cell, digit)
                set_cell(grid, candidates, cell, digit)

        for column, house in enumerate(column_house_ids()):
            for cell, digit in naked_singles.find_placements(grid, candidates, house):
                progress = True
                print(f"Naked single in column {column}", cell, digit)
                set_cell(grid, candidates, cell, digit)

            for cell, digit in hidden_singles.find_placements(grid, candidates, house):
                progress = True
                print(f"Hidden single in column {column}", cell, digit)
                set_cell(grid, candidates, cell, digit)

        for box, house in enumerate(box_house_ids()):
            for cell, digit in naked_singles.find_placements(grid, candidates, house):
                progress = True
                print(f"Naked single in box {box}", cell, digit)
                set_cell(grid, candidates, cell, digit)

            for cell, digit in hidden_singles.find_placements(grid, candidates, house):
                progress = True
                print(f"Hidden single in box {box}", cell, digit)
                set_cell(grid, candidates, cell, digit)

    return grid


def set_cell(grid: np.ndarray, candidates: np.ndarray, cell: Cell, digit: int):
    grid[cell] = digit
    candidates[cell] = [digit]

    # propagate changes through candidates
    for peer_cell in all_peer_cells(cell):
        if digit in candidates[peer_cell]:
            candidates[peer_cell].remove(digit)


def create_candidate_grid(grid: np.ndarray) -> np.ndarray:
    """
    Generate a 2-d array of candidate Sets. Each cell in the
    array contains a set of candidates that may occur in that
    position. A fully solved core will return a candidate
    core of single-cell sets.

    Args:
        grid: 2-d array sudoku core

    Returns:
        Candidate core
    """
    return np.array(
        [
            [
                [
                    digit
                    for digit in range(1, 10)
                    if digit not in peer_digits(grid, Cell(r, c))
                ]
                if grid[r, c] == 0
                else [grid[r, c]]
                for c in range(9)
            ]
            for r in range(9)
        ]
    )

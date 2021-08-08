"""Sudoku Solver"""
from typing import Tuple
import numpy as np
from pyslab.strategies import hidden_singles, naked_singles
from .grid import (
    create_candidate_grid,
    peer_cells,
    row_houses,
    column_houses,
    box_houses,
)


def solve(grid: np.ndarray):

    candidates = create_candidate_grid(grid)

    progress = True

    while progress:
        progress = False

        for row, house in enumerate(row_houses()):
            for cell, digit in naked_singles.find_placements(grid, candidates, house):
                progress = True
                print(f"Naked single in row {row}", cell, digit)
                set_cell(grid, candidates, cell, digit)

            for cell, digit in hidden_singles.find_placements(grid, candidates, house):
                progress = True
                print(f"Hidden single in row {row}", cell, digit)
                set_cell(grid, candidates, cell, digit)

        for column, house in enumerate(column_houses()):
            for cell, digit in naked_singles.find_placements(grid, candidates, house):
                progress = True
                print(f"Naked single in column {column}", cell, digit)
                set_cell(grid, candidates, cell, digit)

            for cell, digit in hidden_singles.find_placements(grid, candidates, house):
                progress = True
                print(f"Hidden single in column {column}", cell, digit)
                set_cell(grid, candidates, cell, digit)

        for box, house in enumerate(box_houses()):
            for cell, digit in naked_singles.find_placements(grid, candidates, house):
                progress = True
                print(f"Naked single in box {box}", cell, digit)
                set_cell(grid, candidates, cell, digit)

            for cell, digit in hidden_singles.find_placements(grid, candidates, house):
                progress = True
                print(f"Hidden single in box {box}", cell, digit)
                set_cell(grid, candidates, cell, digit)

    return grid


def set_cell(
    grid: np.ndarray, candidates: np.ndarray, cell: Tuple[int, int], digit: int
):
    grid[cell] = digit
    candidates[cell] = {digit}

    # propagate changes through candidates
    for peer_cell in peer_cells(*cell):
        if digit in candidates[peer_cell]:
            candidates[peer_cell].remove(digit)

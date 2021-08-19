"""Sudoku Solver"""
import numpy as np

from .core.cells import row_cells, column_cells, box_cells
from .core.digits import peer_digits
from .core.peers import all_peer_cells
from .core.types import Cell, Elimination, Placement
from .strategies import hidden_single, naked_single, naked_pair


def solve(grid: np.ndarray):

    candidates = create_candidate_grid(grid)

    progress = True

    while progress:
        progress = False

        for house in range(9):
            for desc, cells in [
                (f"row {house}", row_cells(house)),
                (f"column {house}", column_cells(house)),
                (f"box {house}", box_cells(house)),
            ]:

                for placement in naked_single.find_placements(grid, candidates, cells):
                    progress = make_placement(
                        grid,
                        candidates,
                        placement,
                        f"Naked Single in {desc}, ",
                    )

                for placement in hidden_single.find_placements(grid, candidates, cells):
                    progress = make_placement(
                        grid,
                        candidates,
                        placement,
                        f"Hidden Single in {desc}, ",
                    )

                for elimination in naked_pair.find_eliminations(
                    grid, candidates, cells
                ):
                    progress = make_elimination(
                        candidates, elimination, f"Hidden Pair in {desc}, "
                    )
    return grid


def make_placement(
    grid: np.ndarray, candidates: np.ndarray, placement: Placement, message: str = ""
) -> bool:
    print(f"{message}Placing {placement.digit} into {placement.cell}")
    grid[placement.cell] = placement.digit
    candidates[placement.cell] = [placement.digit]

    # propagate changes through candidates
    for peer_cell in all_peer_cells(placement.cell):
        if placement.digit in candidates[peer_cell]:
            candidates[peer_cell].remove(placement.digit)

    return True


def make_elimination(
    candidates: np.ndarray,
    elimination: Elimination,
    message: str = "",
) -> bool:
    print(f"{message}Eliminating {elimination.candidates}")
    for candidate in elimination.candidates:
        candidates[candidate.cell].remove(candidate.digit)

    return True


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

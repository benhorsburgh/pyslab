"""Find hidden singles"""
from collections import Counter
import numpy as np
from pyslab.grid import house_cells


def _count_candidates_in_house(
    grid: np.ndarray, candidates: np.ndarray, house: int
) -> Counter:
    return Counter(
        digit
        for cell in house_cells(house)
        for digit in candidates[cell]
        if grid[cell] == 0  # only for unsolved cells
    )


def find_placements(
    grid: np.ndarray,
    candidates: np.ndarray,
    house: int,
):
    singles = [
        digit
        for digit, cnt in _count_candidates_in_house(grid, candidates, house).items()
        if cnt == 1
    ]

    return [
        (cell, single)
        for cell in house_cells(house)
        for single in singles
        if single in candidates[cell] and len(candidates[cell]) > 1
    ]

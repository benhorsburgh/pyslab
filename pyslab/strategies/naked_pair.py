"""Find naked pairs"""
from itertools import combinations
from collections import Counter
import numpy as np
from core.cells import house_cells


def _count_pairs_in_house(
    grid: np.ndarray, candidates: np.ndarray, house: int
) -> Counter:
    return Counter(
        digit
        for cell in house_cells(house)
        for digit in combinations(candidates[cell], 2)
        if grid[cell] == 0  # only for unsolved cells
    )


def find_placements(
    grid: np.ndarray,
    candidates: np.ndarray,
    house: int,
):

    return [
        (cell, digit)
        for cell in house_cells(house)
        if len(candidates[cell]) == 1 and grid[cell] == 0
        for digit in candidates[cell]
    ]

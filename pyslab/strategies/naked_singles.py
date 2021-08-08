"""Find naked singles"""
import numpy as np
from pyslab.grid import house_cells


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

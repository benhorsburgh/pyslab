"""Find naked singles"""
import numpy as np
from typing import List
from ..core.types import Cell, Placement


def find_placements(
    grid: np.ndarray,
    candidates: np.ndarray,
    cells: List[Cell],
) -> List[Placement]:

    return [
        Placement(cell, digit)
        for cell in cells
        if len(candidates[cell]) == 1 and grid[cell] == 0
        for digit in candidates[cell]
    ]

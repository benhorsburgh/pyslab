"""Find hidden singles"""
from typing import List, Tuple
from collections import Counter
import numpy as np
from ..core.types import Cell, Placement


def find_placements(
    grid: np.ndarray,
    candidates: np.ndarray,
    cells: List[Cell],
) -> List[Placement]:

    digit_counts = Counter(
        digit for cell in cells for digit in candidates[cell] if grid[cell] == 0
    ).items()

    singles = [digit for digit, cnt in digit_counts if cnt == 1]

    return [
        Placement(cell, single)
        for cell in cells
        for single in singles
        if single in candidates[cell] and len(candidates[cell]) > 1
    ]

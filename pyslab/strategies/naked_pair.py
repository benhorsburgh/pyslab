"""Find naked pairs"""
from collections import Counter

from typing import List
import numpy as np
from ..core.types import Cell, Candidate, Elimination


def find_eliminations(
    grid: np.ndarray,
    candidates: np.ndarray,
    cells: List[Cell],
) -> List[Elimination]:
    pair_counts = Counter(
        frozenset(candidates[cell])
        for cell in cells
        if len(candidates[cell]) == 2 and grid[cell] == 0
    )

    pairs = [sorted(list(pair)) for pair, cnt in pair_counts.items() if cnt == 2]

    return [
        elimination
        for elimination in [
            Elimination(
                [
                    Candidate(cell, digit)
                    for cell in cells
                    if grid[cell] == 0 and candidates[cell] != pair
                    for digit in candidates[cell]
                    if digit in pair
                ]
            )
            for pair in pairs
        ]
        # no need to return naked pairs if they don't help to eliminate anything!
        if elimination.candidates
    ]

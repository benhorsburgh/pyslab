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
    naked_pair_counts = Counter(
        frozenset(candidates[cell])
        for cell in cells
        if len(candidates[cell]) == 2 and grid[cell] == 0
    )

    naked_pairs = [
        sorted(list(pair)) for pair, cnt in naked_pair_counts.items() if cnt == 2
    ]

    return [
        elimination
        for elimination in [
            Elimination(
                [
                    Candidate(cell, digit)
                    for cell in cells
                    if grid[cell] == 0 and candidates[cell] != naked_pair
                    for digit in candidates[cell]
                    if digit in naked_pair
                ]
            )
            for naked_pair in naked_pairs
        ]
        # no need to return naked pairs if they don't help to eliminate anything!
        if elimination.candidates
    ]

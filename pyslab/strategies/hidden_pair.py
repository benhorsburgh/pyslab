"""Find hidden pairs"""
from collections import Counter
from itertools import combinations

from typing import List
import numpy as np
from ..core.types import Cell, Candidate, Elimination


def find_eliminations(
    grid: np.ndarray,
    candidates: np.ndarray,
    cells: List[Cell],
) -> List[Elimination]:

    digit_counts = Counter(
        digit for cell in cells if grid[cell] == 0 for digit in candidates[cell]
    )

    pair_counts = Counter(
        pair
        for cell in cells
        if grid[cell] == 0
        for pair in combinations(candidates[cell], 2)
        if all(digit_counts[digit] == 2 for digit in pair)
    )

    pairs = [sorted(list(pair)) for pair, cnt in pair_counts.items() if cnt == 2]

    return [
        elimination
        for elimination in [
            Elimination(
                [
                    Candidate(cell, digit)
                    for cell in cells
                    if grid[cell] == 0 and all(d in candidates[cell] for d in pair)
                    for digit in candidates[cell]
                    if digit not in pair
                ]
            )
            for pair in pairs
        ]
        # no need to return naked pairs if they don't help to eliminate anything!
        if elimination.candidates
    ]

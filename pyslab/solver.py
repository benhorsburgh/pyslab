"""Sudoku Solver"""
from typing import Tuple
import numpy as np
import naked_singles
from puzzle_grid import create_candidate_grid, peer_elements


def solve(puzzle: np.ndarray):

    candidates = create_candidate_grid(puzzle)

    progress = True

    while progress:
        progress = False

        for elem, number in naked_singles.find_in_rows(puzzle, candidates):
            progress = True
            print("Naked single in row", elem, number)
            set_element(puzzle, candidates, elem, number)

        for elem, number in naked_singles.find_in_columns(puzzle, candidates):
            progress = True
            print("Naked single in column", elem, number)
            set_element(puzzle, candidates, elem, number)

        for elem, number in naked_singles.find_in_nonets(puzzle, candidates):
            progress = True
            print("Naked single in nonet", elem, number)
            set_element(puzzle, candidates, elem, number)


def set_element(
    puzzle: np.ndarray, candidates: np.ndarray, element: Tuple[int, int], number: int
):
    puzzle[element] = number
    candidates[element] = {number}

    # propagate changes through candidates
    for elem in peer_elements(*element):
        if number in candidates[elem]:
            candidates[elem].remove(number)

import random
from typing import Callable, List, Tuple
import numpy as np
from pyslab.puzzle_grid import (
    brute_force_solution,
    has_unique_solution,
    solved_elements,
    create_candidate_grid,
)


def generate_example(
    finder: Callable[[np.ndarray, np.ndarray], List[Tuple[Tuple[int, int], int]]],
    seed: np.ndarray = np.zeros([9, 9]),
    num_permutations: int = 1000,
    max_clues: int = 50,
) -> np.ndarray:
    solved_puzzle = generate_solution(seed, num_permutations)

    i = 0
    for puzzle in generate_problem(solved_puzzle, max_clues=max_clues):
        i += 1
        if len(finder(puzzle, create_candidate_grid(puzzle))) == 1:
            print("max clues", max_clues)
            return puzzle
        if i > 5:
            return generate_example(finder, seed, num_permutations, max_clues + 1)

    raise RuntimeError("Could not generate an example")


def generate_solution(
    seed: np.ndarray = np.zeros([9, 9]), num_permutations: int = 1000
):
    puzzle = brute_force_solution(seed)
    for _ in range(num_permutations):
        permute_function = random.choice(
            [permute_rows, permute_cols, permute_row_blocks, permute_col_blocks]
        )
        puzzle = permute_function(puzzle)

    return puzzle


def generate_problem(puzzle: np.ndarray, max_clues: int = 30):
    if has_unique_solution(puzzle):

        candidates = list(solved_elements(puzzle))

        if len(candidates) <= max_clues:
            yield puzzle
        else:
            random.shuffle(candidates)

            for r, c in candidates:
                updated_puzzle = puzzle.copy()
                updated_puzzle[r, c] = 0
                updated_puzzle[8 - r, 8 - c] = 0
                yield from generate_problem(updated_puzzle)


def permute_row_blocks(puzzle: np.ndarray) -> np.ndarray:
    a, b, c = 0, 1, 2
    while (a, b, c) == (0, 1, 2):
        a, b, c = random.sample([0, 1, 2], k=3)
    return np.concatenate(
        [
            puzzle[a * 3 : a * 3 + 3, :],
            puzzle[b * 3 : b * 3 + 3, :],
            puzzle[c * 3 : c * 3 + 3, :],
        ]
    )


def permute_col_blocks(puzzle: np.ndarray) -> np.ndarray:
    a, b, c = 0, 1, 2
    while (a, b, c) == (0, 1, 2):
        a, b, c = random.sample([0, 1, 2], k=3)
    return np.concatenate(
        [
            puzzle[:, a * 3 : a * 3 + 3],
            puzzle[:, b * 3 : b * 3 + 3],
            puzzle[:, c * 3 : c * 3 + 3],
        ],
        axis=1,
    )


def permute_rows(puzzle: np.ndarray) -> np.ndarray:
    puzzle = puzzle.copy()
    block = random.randint(0, 2)
    a, b = random.sample([0, 1, 2], k=2)
    while (a, b) in [(0, 1), (1, 2)]:
        a, b = random.sample([0, 1, 2], k=2)
    puzzle[[block * 3 + a, block * 3 + b]] = puzzle[[block * 3 + b, block * 3 + a]]
    return puzzle


def permute_cols(puzzle: np.ndarray) -> np.ndarray:
    puzzle = puzzle.copy()
    block = random.randint(0, 2)
    a, b = random.sample([0, 1, 2], k=2)
    while (a, b) in [(0, 1), (1, 2)]:
        a, b = random.sample([0, 1, 2], k=2)
    puzzle[:, [block * 3 + a, block * 3 + b]] = puzzle[
        :, [block * 3 + b, block * 3 + a]
    ]
    return puzzle

import numpy as np
import random
from pyslab.puzzle_grid import brute_force_solution, unsolved_elems, has_unique_solution, solved_elems


def generate_solution(
        seed: np.ndarray = np.zeros([9, 9]),
        num_permutations: int = 1000
):
    puzzle = brute_force_solution(seed)
    for _ in range(num_permutations):
        permute_function = random.choice([
            permute_rows,
            permute_cols,
            permute_row_blocks,
            permute_col_blocks
        ])
        puzzle = permute_function(puzzle)

    return puzzle


def generate_problem(
        puzzle: np.ndarray
):
    if has_unique_solution(puzzle):

        candidates = list(solved_elems(puzzle))

        if len(candidates) < 30:
            yield puzzle
        else:
            random.shuffle(candidates)

            for r, c in candidates:
                updated_puzzle = puzzle.copy()
                updated_puzzle[r, c] = 0
                updated_puzzle[8-r, 8-c] = 0
                yield from generate_problem(updated_puzzle)


def permute_row_blocks(puzzle: np.ndarray) -> np.ndarray:
    a, b, c = 0, 1, 2
    while (a, b, c) == (0, 1, 2):
        a, b, c = random.sample([0, 1, 2], k=3)
    return np.concatenate([
        puzzle[a * 3:a * 3 + 3, :],
        puzzle[b * 3:b * 3 + 3, :],
        puzzle[c * 3:c * 3 + 3, :]])


def permute_col_blocks(puzzle: np.ndarray) -> np.ndarray:
    a, b, c = 0, 1, 2
    while (a, b, c) == (0, 1, 2):
        a, b, c = random.sample([0, 1, 2], k=3)
    return np.concatenate(
        [puzzle[:, a * 3:a * 3 + 3],
         puzzle[:, b * 3:b * 3 + 3],
         puzzle[:, c * 3:c * 3 + 3]], axis=1)


def permute_rows(puzzle: np.ndarray) -> np.ndarray:
    puzzle = puzzle.copy()
    block = random.randint(0, 2)
    a, b = random.sample([0, 1, 2], k=2)
    while (a, b) in [(0, 1), (1, 2)]:
        a, b = random.sample([0, 1, 2], k=2)
    puzzle[[block*3+a, block*3+b]] = puzzle[[block*3+b, block*3+a]]
    return puzzle


def permute_cols(puzzle: np.ndarray) -> np.ndarray:
    puzzle = puzzle.copy()
    block = random.randint(0, 2)
    a, b = random.sample([0, 1, 2], k=2)
    while (a, b) in [(0, 1), (1, 2)]:
        a, b = random.sample([0, 1, 2], k=2)
    puzzle[:, [block * 3 + a, block * 3 + b]] = puzzle[:, [block * 3 + b, block * 3 + a]]
    return puzzle

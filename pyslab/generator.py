import random
from functools import partial
from typing import Callable, List, Tuple

import numpy as np

from .core.types import Cell
from .core.validation import brute_force_solution, has_unique_solution, solved_cells
from .solver import create_candidate_grid


def generate_example(
    finders: List[
        Callable[[np.ndarray, np.ndarray], List[Tuple[Tuple[int, int], int]]]
    ],
    min_match: int = 1,
    seed: np.ndarray = np.zeros([9, 9]),
    permutations: int = 1000,
    max_clues: int = 50,
) -> np.ndarray:
    print("Scanning with max_clues =", max_clues)
    solved_grid = generate_solution(seed, permutations)

    i = 0
    for grid in generate_problem(solved_grid, max_clues=max_clues):
        i += 1
        if all(
            len(finder(grid, create_candidate_grid(grid))) >= min_match
            for finder in finders
        ):
            print("max clues", max_clues)
            return grid
        if i > 5:
            return generate_example(
                finders, min_match, seed, permutations, max_clues + 1
            )

    raise RuntimeError("Could not generate an example")


def generate_solution(seed: np.ndarray = np.zeros([9, 9]), permutations: int = 1000):
    grid = brute_force_solution(seed)
    for _ in range(permutations):
        permute_function = random.choice(
            [permute_rows, permute_cols, permute_row_blocks, permute_col_blocks]
        )
        grid = permute_function(grid)

    return grid


def generate_problem(grid: np.ndarray, max_clues: int = 30):
    if has_unique_solution(grid):

        candidates = list(solved_cells(grid))

        if len(candidates) <= max_clues:
            yield grid
        else:
            random.shuffle(candidates)

            for r, c in candidates:
                updated_grid = grid.copy()
                updated_grid[r, c] = 0
                updated_grid[8 - r, 8 - c] = 0
                candidates.remove(Cell(r, c))
                if Cell(8 - r, 8 - c) in candidates:
                    candidates.remove(Cell(8 - r, 8 - c))
                yield from generate_problem(updated_grid)


def permute_row_blocks(grid: np.ndarray) -> np.ndarray:
    a, b, c = 0, 1, 2
    while (a, b, c) == (0, 1, 2):
        a, b, c = random.sample([0, 1, 2], k=3)
    return np.concatenate(
        [
            grid[a * 3 : a * 3 + 3, :],
            grid[b * 3 : b * 3 + 3, :],
            grid[c * 3 : c * 3 + 3, :],
        ]
    )


def permute_col_blocks(grid: np.ndarray) -> np.ndarray:
    a, b, c = 0, 1, 2
    while (a, b, c) == (0, 1, 2):
        a, b, c = random.sample([0, 1, 2], k=3)
    return np.concatenate(
        [
            grid[:, a * 3 : a * 3 + 3],
            grid[:, b * 3 : b * 3 + 3],
            grid[:, c * 3 : c * 3 + 3],
        ],
        axis=1,
    )


def permute_rows(grid: np.ndarray) -> np.ndarray:
    grid = grid.copy()
    block = random.randint(0, 2)
    a, b = random.sample([0, 1, 2], k=2)
    while (a, b) in [(0, 1), (1, 2)]:
        a, b = random.sample([0, 1, 2], k=2)
    grid[[block * 3 + a, block * 3 + b]] = grid[[block * 3 + b, block * 3 + a]]
    return grid


def permute_cols(grid: np.ndarray) -> np.ndarray:
    grid = grid.copy()
    block = random.randint(0, 2)
    a, b = random.sample([0, 1, 2], k=2)
    while (a, b) in [(0, 1), (1, 2)]:
        a, b = random.sample([0, 1, 2], k=2)
    grid[:, [block * 3 + a, block * 3 + b]] = grid[:, [block * 3 + b, block * 3 + a]]
    return grid


def main(finders, min_match):
    grid = generate_example(finders=finders, min_match=min_match)
    print()
    print(grid)
    print(create_candidate_grid(grid))
    print("".join([str(int(grid[r, c])) for r in range(9) for c in range(9)]))
    for finder in finders:
        print(finder(grid, create_candidate_grid(grid)))


if __name__ == "__main__":
    from pyslab.strategies import naked_pair
    from pyslab.core.cells import box_cells

    main(
        [
            partial(naked_pair.find_eliminations, cells=box_cells(8)),
        ],
        1,
    )

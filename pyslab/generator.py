import numpy as np
import random
from pyslab.solver import brute_force


def generate(
        seed: np.ndarray = np.zeros([9, 9]),
        num_permutations: int = 1000
):
    board = brute_force(seed)
    for _ in range(num_permutations):
        permute_function = random.choice([
            permute_rows,
            permute_cols,
            permute_row_blocks,
            permute_col_blocks
        ])
        board = permute_function(board)
    return board


def permute_row_blocks(board: np.ndarray) -> np.ndarray:
    a, b, c = random.sample([0, 1, 2], k=3)
    return np.concatenate([
        board[a * 3:a * 3 + 3, :],
        board[b * 3:b * 3 + 3, :],
        board[c * 3:c * 3 + 3, :]])


def permute_col_blocks(board: np.ndarray) -> np.ndarray:
    a, b, c = random.sample([0, 1, 2], k=3)
    return np.concatenate(
        [board[:, a * 3:a * 3 + 3],
         board[:, b * 3:b * 3 + 3],
         board[:, c * 3:c * 3 + 3]], axis=1)


def permute_rows(board: np.ndarray) -> np.ndarray:
    board = board.copy()
    block = random.randint(0, 2)
    a, b = random.sample([0, 1, 2], k=2)
    board[[block*3+a, block*3+b]] = board[[block*3+b, block*3+a]]
    return board


def permute_cols(board: np.ndarray) -> np.ndarray:
    board = board.copy()
    block = random.randint(0, 2)
    a, b = random.sample([0, 1, 2], k=2)
    board[:, [block * 3 + a, block * 3 + b]] = board[:, [block * 3 + b, block * 3 + a]]
    return board

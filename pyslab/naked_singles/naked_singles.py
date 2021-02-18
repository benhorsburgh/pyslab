from typing import Tuple
import numpy as np
from pyslab.board import unsolved_elems, peer_values


def naked_singles_row(board: np.ndarray) -> Tuple[int, int, int]:

    for r, c in unsolved_elems(board):
        candidates = set(range(1, 10)) - peer_values(board, r, c)
        if len(candidates) == 1:
            return r, c, candidates.pop()


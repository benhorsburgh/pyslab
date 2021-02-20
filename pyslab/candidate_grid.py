# import numpy as np
# from typing import Iterator, Tuple, Set, Generator, Any, Dict, List
#
#
# def row_values(candidates: np.ndarray, row: int) -> Set:
#     return set().union(*[e for e in candidates[row] if len(e) == 1])
#
# def col_values(candidates: np.ndarray, col: int) -> Set:
#     return set().union(*[e for e in candidates[:, col] if len(e) == 1])
#
# def nonet_values(candidates: np.ndarray, row: int, col: int) -> Set:
#     r, c = row//3*3, col//3*3
#     return set().union(*[e for e in candidates[r:r + 3, c:c + 3].flatten() if len(e) == 1])
#
# def peer_values(candidates: np.ndarray, row: int, col: int) -> Set:
#     return row_values(candidates, row).union(col_values(candidates, col)).union(nonet_values(candidates, row, col))
#

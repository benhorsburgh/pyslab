import numpy as np
from typing import Tuple, List
from collections import Counter


def find_in_rows(puzzle: np.ndarray, candidates:np.ndarray) -> List[Tuple[Tuple[int, int], int]]:

    return [single for singles in [[((row, col), elem)
          for col, elems in enumerate(candidates[row,:])
          for elem in [
              num
              for num, cnt in Counter(
                num
                for elem in candidates[row, :]
                for num in elem
                if len(elem) > 1).items()
              if cnt == 1]
          if elem in elems]
         for row in range(9)] for single in singles]

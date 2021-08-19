from typing import List

from .types import Cell


def row_cells(row: int) -> List[Cell]:
    return [Cell(row, c) for c in range(9)]


def column_cells(column: int) -> List[Cell]:
    return [Cell(r, column) for r in range(9)]


def box_cells(box: int) -> List[Cell]:
    corner_r, corner_c = box // 3 * 3, box % 3 * 3
    return [
        Cell(r, c)
        for r in range(corner_r, corner_r + 3)
        for c in range(corner_c, corner_c + 3)
    ]

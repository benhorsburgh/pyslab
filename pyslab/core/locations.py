from typing import List

from .types import Cell


def box_id(cell: Cell) -> int:
    return (cell.row // 3) * 3 + (cell.column // 3)


def row_house_ids() -> List[int]:
    return list(range(9))


def column_house_ids() -> List[int]:
    return list(range(10, 18))


def box_house_ids() -> List[int]:
    return list(range(19, 27))

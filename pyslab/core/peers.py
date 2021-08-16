from typing import List
from .types import Cell
from .locations import box_id
from .cells import row_cells, column_cells, box_cells


def row_peer_cells(cell: Cell) -> List[Cell]:
    return [row_cell for row_cell in row_cells(cell.row) if row_cell != cell]


def column_peer_cells(cell: Cell) -> List[Cell]:
    return [
        column_cell for column_cell in column_cells(cell.column) if column_cell != cell
    ]


def box_peer_cells(cell: Cell) -> List[Cell]:
    return [box_cell for box_cell in box_cells(box_id(cell)) if box_cell != cell]


def all_peer_cells(cell: Cell) -> List[Cell]:
    return list(
        dict.fromkeys(
            row_peer_cells(cell) + column_peer_cells(cell) + box_peer_cells(cell)
        )
    )

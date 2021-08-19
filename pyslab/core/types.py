from typing import NamedTuple, List


class Cell(NamedTuple):
    row: int
    column: int


class Placement(NamedTuple):
    cell: Cell
    digit: int


class Candidate(NamedTuple):
    cell: Cell
    digit: int


class Elimination(NamedTuple):
    candidates: List[Candidate]

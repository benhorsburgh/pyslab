import random
from core.types import Cell
from core.peers import row_peer_cells, column_peer_cells, box_peer_cells, all_peer_cells


class TestRowPeerCells:
    def test_correct_peers(self):
        peer_cols = [c for c in range(9)]
        random.shuffle(peer_cols)
        col = peer_cols.pop()
        row = random.randint(0, 8)
        peers = row_peer_cells(Cell(row, col))
        assert [Cell(row, c) for c in sorted(peer_cols)] == peers


class TestColumnPeerCells:
    def test_correct_peers(self):
        peer_rows = [c for c in range(9)]
        random.shuffle(peer_rows)
        row = peer_rows.pop()
        col = random.randint(0, 8)
        peers = column_peer_cells(Cell(row, col))
        assert [Cell(r, col) for r in sorted(peer_rows)] == peers


class TestBoxPeerCells:
    def test_correct_peers(self):
        peers = box_peer_cells(Cell(3, 3))
        assert [
            Cell(r, c) for r in range(3, 6) for c in range(3, 6) if not (r == c == 3)
        ] == peers


class TestAllPeerCells:
    def test_correct_peers(self):
        peers = all_peer_cells(Cell(0, 3))
        assert sorted(peers) == sorted(
            list(
                {(0, c) for c in range(9) if c != 3}
                .union((r, 3) for r in range(9) if r != 0)
                .union({(1, 4), (1, 5), (2, 4), (2, 5)})
            )
        )

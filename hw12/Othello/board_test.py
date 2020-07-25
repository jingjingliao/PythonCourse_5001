from board import Board


def test_init():
    board = Board([[None, None]], 600, 100)
    assert board.grid == [[None, None]]
    assert board.dimension == 600
    assert board.grid_len == 100
    assert board.space == 6

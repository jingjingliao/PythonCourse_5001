from maze import Maze
from game_controller import GameController


def test_constructor():
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450,
             100, 300, g)
    assert m.LEFT_VERT == 150
    assert m.RIGHT_VERT == 450
    assert m.TOP_HORIZ == 100
    assert m.BOTTOM_HORIZ == 300
    assert m.WIDTH == 600
    assert m.HEIGHT == 400
    assert m.gc is g
    assert m.dots.dots_left() == ((m.dots.WIDTH//m.dots.SPACING + 1) * 2 +
                                  (m.dots.HEIGHT//m.dots.SPACING + 1) * 2)


def test_eat_dots():
    g = GameController(600, 600)
    m = Maze(600, 600, 150, 450,
             150, 450, g)

    # firstly, check the length of the top row which is also the quanitity of
    # the dots, then execute eat_dots method, finally, the the length of the
    # top row will minus one, because one dot has been removed when dots didn't
    # in the right or left, top or bottom edges
    assert len(m.dots.top_row) == 9
    for dot in m.dots.top_row:
        if dot.x == 300 and dot.y == 150:
            m.eat_dots(dot.x, dot.y)

    assert len(m.dots.top_row) == 8

    assert len(m.dots.left_col) == 9
    for dot in m.dots.left_col:
        if dot.x == 150 and dot.y == 225:
            m.eat_dots(dot.x, dot.y)

    assert len(m.dots.left_col) == 8

    # when dot in the bottom_right edges, although the dots in
    # bottom_right edges and bottom_left edges are two seperate dots, but in
    # reality, they are like two "half dots" and will be eaten by Pacman at the
    # same time, so the length of bottom_row will minus two. It is the same
    # with dots in the left and right edges, top and bottom edges
    assert len(m.dots.bottom_row) == 9
    for dot in m.dots.bottom_row:
        if dot.x == 600 and dot.y == 450:
            m.eat_dots(dot.x, dot.y)

    assert len(m.dots.bottom_row) == 7

    assert len(m.dots.right_col) == 9
    for dot in m.dots.right_col:
        if dot.x == 450 and dot.y == 0:
            m.eat_dots(dot.x, dot.y)

    assert len(m.dots.right_col) == 7

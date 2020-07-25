from dots import Dots


def test_constructor():
    ds = Dots(600, 600, 150, 450, 150, 450)
    assert ds.WIDTH == 600
    assert ds.HEIGHT == 600
    assert ds.TH == 150
    assert ds.BH == 450
    assert ds.LV == 150
    assert ds.RV == 450
    assert len(ds.bottom_row) == len(ds.top_row) == ds.WIDTH//ds.SPACING + 1
    assert len(ds.left_col) == len(ds.right_col) == ds.HEIGHT//ds.SPACING + 1
    for i in range(len(ds.left_col)):
        assert ds.left_col[i].x == ds.LV
        assert ds.left_col[i].y == ds.SPACING * i
    for i in range(len(ds.right_col)):
        assert ds.right_col[i].x == ds.RV
        assert ds.right_col[i].y == ds.SPACING * i
    for i in range(len(ds.top_row)):
        assert ds.top_row[i].x == ds.SPACING * i
        assert ds.top_row[i].y == ds.TH
    for i in range(len(ds.bottom_row)):
        assert ds.bottom_row[i].x == ds.SPACING * i
        assert ds.bottom_row[i].y == ds.BH


def test_eat():
    ds = Dots(600, 600, 150, 450, 150, 450)
    # firstly, if the exactly dot in the top row, the distance between
    # Pacman and dot is within eat distance(50).Then execute eat method,
    # check the same dot is not in the top row anymore
    for dot in ds.top_row:
        if dot.x == 300 and dot.y == 150:
            ds.eat(305, 150)
            assert dot not in ds.top_row

    # firstly, if the exactly dot in the bottom_row, the distance between
    # Pacman and dot is more than eat distance(50).Then execute eat method,
    # check the same dot is still in the bottom_row
    for dot in ds.bottom_row:
        if dot.x == 525 and dot.y == 450:
            ds.eat(625, 450)
            assert dot in ds.bottom_row

    # firstly, if the exactly dot in the left_col in the bottom,
    # the distance between Pacman and dot is more than 550.
    # Then execute eat method,check the same dot is not in the left_col anymore
    for dot in ds.left_col:
        if dot.x == 150 and dot.y == 600:
            ds.eat(150, 50)
            assert dot not in ds.left_col

    # firstly, if the exactly dot in the right_col in the middle,
    # the distance between Pacman and dot is more than 50.
    # Then execute eat method,check the same dot is not in the left_col
    for dot in ds.right_col:
        if dot.x == 450 and dot.y == 300:
            ds.eat(443, 300)
            assert dot not in ds.right_col


def test_dots_left():
    ds = Dots(600, 600, 150, 450, 150, 450)
    dl = ds.dots_left()
    assert dl == ((ds.WIDTH//ds.SPACING + 1) * 2 +
                  (ds.HEIGHT//ds.SPACING + 1) * 2)

from game_controller import GameController
from board import Board
from disk import Disk


def test_init():
    """Test initial method"""
    gc = GameController(600, 100)
    assert gc.dimension == 600
    assert gc.grid_len == 100
    assert gc.half_dimension == 300
    assert gc.space == 6
    assert gc.diameter == 90
    assert gc.half_grid_len == 50
    assert gc.black_color == 0
    assert gc.white_color == 255
    assert gc.color == 0
    assert gc.remaining_disk is None
    assert gc.black_disk_count is None
    assert gc.white_disk_count is None
    assert gc.directions == (
                            (0, -1), (0, 1), (-1, 0), (1, 0),
                            (-1, 1), (1, -1), (-1, -1), (1, 1)
                            )
    assert gc.next_step_map == {
                                (2, 1): {(2, 2)},
                                (4, 3): {(3, 3)},
                                (3, 4): {(3, 3)},
                                (1, 2): {(2, 2)}
                                }
    assert gc.human_turn is True
    assert gc.time == 60
    assert gc.message == ""
    assert gc.win == ""
    assert gc.turn == ""

    # gc.grid will be tested in the initial disk function


def test_initial_disk():
    """Test initial board"""
    # Test the board of size is zero
    gc = GameController(0, 100)
    gc.initial_disk()
    assert gc.grid == []

    # Test the board of size is two * two
    # color == 0 means black color
    # color == 255 means black color
    gc = GameController(200, 100)
    gc.initial_disk()
    assert gc.grid[0][0].color == 255
    assert gc.grid[0][1].color == 0
    assert gc.grid[1][0].color == 0
    assert gc.grid[1][1].color == 255

    # Test the board of size is four * four
    # color == 0 means black color
    # color == 255 means black color
    gc = GameController(400, 100)
    gc.initial_disk()
    for i in range(len(gc.grid)):
        for j in range(len(gc.grid)):
            if i == 1 and j == 1:
                assert gc.grid[i][j].color == 255
            elif i == 1 and j == 2:
                assert gc.grid[i][j].color == 0
            elif i == 2 and j == 1:
                assert gc.grid[i][j].color == 0
            elif i == 2 and j == 2:
                assert gc.grid[i][j].color == 255
            else:
                assert gc.grid[i][j] is None


def test_is_in_boundary():
    """Test whether the disk location is out of boundary"""
    gc = GameController(800, 100)
    assert gc.is_in_boundary(5, 7) is True
    assert gc.is_in_boundary(10, 7) is False
    assert gc.is_in_boundary(15, 12) is False
    assert gc.is_in_boundary(4, 17) is False


def test_check_legal_space():
    """Check the legal space for the appropriate color"""
    # when disk color will be black, check all the available space for black
    # disk and store it as the key and the disks need to be flipped over
    # as the value
    gc = GameController(800, 100)
    gc.check_legal_space(0)
    assert gc.next_step_map == {(3, 2): {(3, 3)},
                                (5, 4): {(4, 4)},
                                (4, 5): {(4, 4)},
                                (2, 3): {(3, 3)}}

    gc = GameController(800, 100)
    gc.check_legal_space(255)
    assert gc.next_step_map == {(3, 5): {(3, 4)},
                                (5, 3): {(4, 3)},
                                (4, 2): {(4, 3)},
                                (2, 4): {(3, 4)}}


def test_is_in_next_step():
    """Test click the position which is legal place, which means the location
    should be in self.next_step_map"""
    gc = GameController(800, 100)
    assert gc.is_in_next_step(3, 2) is True
    assert gc.is_in_next_step(5, 4) is True
    assert gc.is_in_next_step(7, 7) is False


def test_ranked_flipped_space():
    """Test ranked flipped space method"""
    gc = GameController(800, 100)
    assert (gc.ranked_flipped_space(
                {(3, 2): {(3, 3)},
                 (5, 4): {(4, 4), (4, 5)},
                 (4, 5): {(4, 4)},
                 (2, 3): {(3, 3)}})) == [((5, 4), {(4, 5), (4, 4)}),
                                         ((3, 2), {(3, 3)}),
                                         ((4, 5), {(4, 4)}),
                                         ((2, 3), {(3, 3)})]


def test_change_color():
    """Test change color"""
    gc = GameController(800, 100)
    # the original color is 0 (black color)
    assert gc.color == 0
    gc.change_color()  # execute change color method
    # new color is 255 (white color)
    assert gc.color == 255


def test_show_score():
    """Test show score method"""
    gc = GameController(800, 100)
    gc.show_score()
    assert gc.black_disk_count == 2
    assert gc.white_disk_count == 2
    assert gc.remaining_disk == 60

    gc.grid[3][2] = Disk(3, 2, 0)
    gc.show_score()
    assert gc.black_disk_count == 3
    assert gc.white_disk_count == 2
    assert gc.remaining_disk == 59

    gc.grid[1][1] = Disk(1, 1, 255)
    gc.show_score()
    assert gc.black_disk_count == 3
    assert gc.white_disk_count == 3
    assert gc.remaining_disk == 58


def test_show_result():
    gc = GameController(400, 100)
    for i in range(len(gc.grid)):
        for j in range(len(gc.grid)):
            if i == 0:
                gc.grid[i][j] = Disk(i, j, 0)
            else:
                gc.grid[i][j] = Disk(i, j, 255)

    gc.show_result()
    assert (gc.remaining_disk) == 0
    assert (gc.black_disk_count) == 4
    assert (gc.white_disk_count) == 12
    assert gc.win == "Robot win!"

    gc = GameController(200, 100)
    for i in range(len(gc.grid)):
        for j in range(len(gc.grid)):
            gc.grid[i][j] = Disk(i, j, 0)

    gc.show_result()
    assert (gc.remaining_disk) == 0
    assert (gc.black_disk_count) == 4
    assert (gc.white_disk_count) == 0
    assert gc.win == "You win!"

    gc = GameController(400, 100)
    gc.message = "No legal move"
    gc.show_result()
    assert (gc.remaining_disk) == 0

    gc = GameController(200, 100)
    for i in range(len(gc.grid)):
        for j in range(len(gc.grid)):
            if i == 0:
                gc.grid[i][j] = Disk(i, j, 0)
            else:
                gc.grid[i][j] = Disk(i, j, 255)
    gc.show_result()
    assert (gc.remaining_disk) == 0
    assert (gc.black_disk_count) == 2
    assert (gc.white_disk_count) == 2
    assert gc.win == "Same score!"


def test_find_max_score():
    """Test find max score method, the max score should be in the first line"""
    gc = GameController(400, 100)
    assert gc.find_max_score("test_score.txt") == 15


def test_save_name_in_file():
    """Test save_name_in_file method"""
    # Lisa play the game and get her score, store her score in the file
    gc = GameController(800, 100)
    gc.save_name_in_file("Lisa", "test_save_name.txt")

    # Lee play the game and get his score, store his score in the file, it
    # shoule be on the top, because his score is higher than lisa's score
    for i in range(len(gc.grid)):
        for j in range(len(gc.grid)):
            gc.grid[i][j] = Disk(i, j, 0)
    gc.save_name_in_file("Lee", "test_save_name.txt")

    # Chris play the game and get his score, store his score in the file, it
    # shoule be on the bottom, because his score is lower than lee's score
    gc = GameController(800, 100)
    for i in range(len(gc.grid)):
        for j in range(len(gc.grid)):
            if i == 0:
                gc.grid[i][j] = Disk(i, j, 0)
    gc.save_name_in_file("Chris", "test_save_name.txt")

    # Check the first person and the last person in the file
    with open("test_save_name.txt") as file:
        assert file.readline().strip() == "Lee 64"
        assert file.readlines()[-1].strip() == "Chris 10"

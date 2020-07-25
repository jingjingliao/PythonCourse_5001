from disk import Disk


def test_init():
    disk = Disk(100, 200, "Blue")
    assert disk.column == 100
    assert disk.row == 200
    assert disk.color == "Blue"
    assert disk.diameter == 90
    assert disk.spacing == 100
    assert disk.half_space == 50

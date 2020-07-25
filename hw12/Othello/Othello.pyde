from game_controller import GameController

DIMENSION = 800
GRID_LEN = 100

gc = GameController(DIMENSION, GRID_LEN)

BG = (1, 100, 0)


def setup():
    size(DIMENSION, DIMENSION)


def draw():
    background(*BG)
    if gc.human_turn is False:
        gc.robot_run()
    gc.display()


def mouseClicked():
    gc.human_run()

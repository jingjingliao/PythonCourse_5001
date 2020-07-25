from game_controller import GameController

DIMENSION = 400
GRID_LEN = 100
BG = (1, 100, 0)

gc = GameController(DIMENSION, GRID_LEN)

def setup():
    size(DIMENSION, DIMENSION)

def draw():
    background(*BG)
    gc.display()

def mouseClicked():
    gc.click()
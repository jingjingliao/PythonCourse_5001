from board import Board
from disk import Disk


class GameController:
    """Control the game, initialize two players and the board, create the grid
    of the board"""

    def __init__(self, DIMENSION, GRID_LEN):
        self.dimension = DIMENSION
        self.grid_len = GRID_LEN
        self.space = self.dimension // self.grid_len
        self.grid = [[None] * self.space for _ in range(self.space)]

        self.black_color = 0
        self.white_color = 255
        self.color = 0

        self.board = Board(self.grid, DIMENSION, GRID_LEN)
        self.initial_disk()

    def initial_disk(self):
        """Initialize the first four disks"""
        middle = self.dimension // 200
        DIFF = 1
        self.grid[middle - DIFF][middle - DIFF] \
            = Disk(middle - DIFF, middle - DIFF, self.white_color)
        self.grid[middle - DIFF][middle] \
            = Disk(middle - DIFF, middle, self.black_color)
        self.grid[middle][middle - DIFF] \
            = Disk(middle, middle - DIFF, self.black_color)
        self.grid[middle][middle] = Disk(middle, middle, self.white_color)

    def click(self):
        """click the button and put the disk on the board"""
        x = mouseX // 100
        y = mouseY // 100
        if self.grid[x][y] is None:
            self.grid[x][y] = Disk(x, y, self.color)

            if self.color == self.black_color:
                self.color = self.white_color
            else:
                self.color = self.black_color
        self.show_result()

    def display(self):
        """Draw the board"""
        self.board.display()

    def show_result(self):
        black_disk_count = 0
        white_disk_count = 0
        for row in self.grid:
            for disk in row:
                if disk is not None:
                    if disk.color == self.black_color:
                        black_disk_count += 1
                    else:
                        white_disk_count += 1
        print("Black disk", black_disk_count)
        print("White disk", white_disk_count)
        remaining_disk = self.space * self.space - black_disk_count - \
                         white_disk_count
        print("Remaining disk", remaining_disk)
        print("======================")

        if remaining_disk == 0:
            print("Game Over")
            if  black_disk_count > white_disk_count:
                print("Black disk win")
            elif black_disk_count < white_disk_count:
                print("White disk win")
            else:
                print("They got the same score")

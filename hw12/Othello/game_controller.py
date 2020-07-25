from board import Board
from disk import Disk


class GameController:
    def __init__(self, DIMENSION, GRID_LEN):
        self.dimension = DIMENSION
        self.grid_len = GRID_LEN
        self.half_dimension = DIMENSION // 2
        self.space = self.dimension // self.grid_len
        self.grid = [[None] * self.space for _ in range(self.space)]
        self.board = Board(self.grid, DIMENSION, GRID_LEN)

        self.diameter = 90
        self.half_grid_len = self.grid_len // 2

        self.black_color = 0
        self.white_color = 255
        self.color = 0

        self.remaining_disk = None
        self.black_disk_count = None
        self.white_disk_count = None

        self.directions = (
            (0, -1), (0, 1), (-1, 0), (1, 0),
            (-1, 1), (1, -1), (-1, -1), (1, 1)
        )

        self.next_step_map = dict()

        self.human_turn = True
        self.time = 60

        self.message = ""
        self.win = ""
        self.turn = ""

        self.initial_disk()

    def initial_disk(self):
        """Initialize the first four disks"""
        DIVISOR = 200
        DIFF = 1
        middle = self.dimension // DIVISOR
        if self.grid != []:
            self.grid[middle - DIFF][middle - DIFF] \
                = Disk(middle - DIFF, middle - DIFF, self.white_color)
            self.grid[middle - DIFF][middle] \
                = Disk(middle - DIFF, middle, self.black_color)
            self.grid[middle][middle - DIFF] \
                = Disk(middle, middle - DIFF, self.black_color)
            self.grid[middle][middle] = Disk(middle, middle, self.white_color)

        # at the beginning, self.color is black, get all the legal place for
        # black disk on the board
        self.check_legal_space(self.color)

    def is_in_boundary(self, i, j):
        """Checking disk's eight direction, making sure the new location is
        still within board boundary"""
        if 0 <= i <= len(self.grid) - 1 and 0 <= j <= len(self.grid[0]) - 1:
            return True
        else:
            return False

    def check_legal_space(self, color):
        """Check disk's legal place, based on the color"""
        if color == self.black_color:
            opposite_color = self.white_color
        else:
            opposite_color = self.black_color

        self.next_step_map = dict()
        # the key is the legal place, the value is a set with tuple inside,
        # each tuple contains the position of a disk that need to be flipped
        # over

        for i, row in enumerate(self.grid):
            for j, disk in enumerate(row):
                if disk is not None and disk.color == color:
                    # if there is a disk object on the self.grid, and the color
                    # equals to the color that we are ready to put. Then, we
                    # check the eight directions of this disk and find out
                    # all the available place for upcoming disk
                    for direction in self.directions:
                        path = set()
                        has_opponent = False    # whether there is an opposite
                        # color beside this disk

                        # disk position add one of the directions and get a new
                        # disk position
                        temp_i = i + direction[0]
                        temp_j = j + direction[1]

                        # check whether this new disk postion is within board
                        # boundary, the postion has a disk object here and the
                        # color should be opposite to the original disk
                        while (self.is_in_boundary(temp_i, temp_j) and
                                self.grid[temp_i][temp_j] is not None and
                                self.grid[temp_i][temp_j].color ==
                                opposite_color):

                            # add the location to the path and move forward to
                            # checking the same direction
                            has_opponent = True
                            path.add((temp_i, temp_j))
                            temp_i += direction[0]
                            temp_j += direction[1]

                        # get out of the while loop, if the new postion is
                        # within board boundary, and there is no disk object
                        # in it and there exists an opposite disk on the way
                        # back, then add the disk location in the directionary
                        # as legal place. If this legal place is not in the
                        # dictionary, add it directly. If it is already in the
                        # directionary, keep the position of legal place and
                        # union their path, remove duplicate ones
                        if (self.is_in_boundary(temp_i, temp_j)
                                and self.grid[temp_i][temp_j] is None
                                and has_opponent):
                            existing = self.next_step_map.get((temp_i, temp_j))
                            if existing:
                                self.next_step_map[(
                                    temp_i, temp_j)] = existing.union(path)
                            else:
                                self.next_step_map[(temp_i, temp_j)] = path

    def show_available_space(self):
        """Show available space for current disk"""
        CIRCLE = (1, 100, 0)
        WEIGHT = 0.5
        if self.next_step_map:
            for next in self.next_step_map:
                strokeWeight(WEIGHT)
                fill(*CIRCLE)
                ellipse(next[0] * self.grid_len + self.half_grid_len,
                        next[1] * self.grid_len + self.half_grid_len,
                        self.diameter, self.diameter)

    def flipover(self, disk_x, disk_y, color):
        """Flipped over all the disks in the value of self.next_step_map
        dictionary"""
        flip_set = self.next_step_map[(disk_x, disk_y)]
        for location in flip_set:
            self.grid[location[0]][location[1]].change_color(color)

    def is_in_next_step(self, x, y):
        """Whether the robot or the human, when they click, the mouse position
        should be within the legal place"""
        return (x, y) in self.next_step_map

    def human_run(self):
        """Human click"""
        if self.next_step_map != {}:  # there is legal place for black disk
            x = mouseX // self.grid_len
            y = mouseY // self.grid_len
            if self.is_in_next_step(x, y):
                self.play(x, y)  # flipover, change to white color
                self.human_turn = False
        else:  # there is no legal place for black disk
            self.human_turn = False
            self.change_color()     # change to white color
            self.check_legal_space(self.color)  # check whether there is legal
            # place for white color
            self.show_result()
            if self.next_step_map == {} and self.remaining_disk != 0:
                self.no_legal_move()
            # if there is no legal move for white color as well, that means
            # both sides have no legal move, end the game

    def robot_run(self):
        """Robot move"""
        MINUS_TIME = 1
        DELAY_TIME = 60
        if self.next_step_map != {}:  # there is legal place for white disk
            # rank the dictionary by the length of its value, get the fist
            # position, which means the flipped over path is the longest
            available_space = self.ranked_flipped_space(self.next_step_map)
            x = available_space[0][0][0]
            y = available_space[0][0][1]
            self.time -= MINUS_TIME
            if self.time == 0:
                self.play(x, y)
                self.human_turn = True
                self.human_run()
                self.time = DELAY_TIME
        else:  # there is no legal place for white disk
            self.human_turn = True
            self.change_color()  # change to human's color
            self.check_legal_space(self.color)  # check the available space
            self.human_run()
            self.show_result()
            # there is no legal move for white color and black color
            if self.next_step_map == {} and self.remaining_disk != 0:
                self.no_legal_move()

    def no_legal_move(self):
        """When both sides has no legal move, end the game"""
        self.message = "No legal move"
        self.print_on_screen()
        self.show_result()

    def ranked_flipped_space(self, dic):
        """Sorted the dictionary and ranked by the length of its value, which
        means the longest path that need to be flipped over"""
        new_dic = sorted(dic.items(),
                         key=lambda x: len(x[1]),
                         reverse=True)
        return new_dic

    def announce(self):
        """Announce the winner"""
        if self.remaining_disk == 0:
            return
        elif self.human_turn is True:
            self.turn = "Your turn"
        elif self.human_turn is False:
            self.turn = "Robot's turn"
        self.print_on_screen()

    def play(self, x, y):
        """Put the disk, flipped the color and check legal space for the
        following disk"""
        self.grid[x][y] = Disk(x, y, self.color)
        self.flipover(x, y, self.color)
        self.change_color()
        self.check_legal_space(self.color)

    def change_color(self):
        """Change the color of the disk"""
        if self.color == self.black_color:
            self.color = self.white_color
        else:
            self.color = self.black_color

    def display(self):
        """Display the board, the turn, the available space and winner"""
        MINUS_TIME = 1
        self.board.display()
        self.announce()
        self.print_on_screen()
        self.show_available_space()
        if self.win != "":
            self.time -= MINUS_TIME
            if self.time == 0:
                self.get_player_name()

    def show_score(self):
        """Calculate the score"""
        self.black_disk_count = 0
        self.white_disk_count = 0
        for row in self.grid:
            for disk in row:
                if disk is not None:
                    if disk.color == self.black_color:
                        self.black_disk_count += 1
                    else:
                        self.white_disk_count += 1
        self.remaining_disk = self.space * self.space - \
            self.black_disk_count - self.white_disk_count
        return (self.black_disk_count,
                self.white_disk_count,
                self.remaining_disk)

    def show_result(self):
        """Show the result of the game"""
        self.black_disk_count, self.white_disk_count, self.remaining_disk = \
            self.show_score()
        if self.message == "No legal move":
            self.remaining_disk = 0
        if self.remaining_disk == 0:
            if self.black_disk_count > self.white_disk_count:
                self.win = "You win!"
            elif self.black_disk_count < self.white_disk_count:
                self.win = "Robot win!"
            else:
                self.win = "Same score!"

    def print_on_screen(self):
        """Put the result on the board"""
        FILL_RED = (255, 69, 0)
        TEXT_SIZE = 40
        WEIGHT = 3
        self.show_result()
        strokeWeight(WEIGHT)
        textSize(TEXT_SIZE)
        textAlign(CENTER)
        fill(*FILL_RED)
        if self.message != "":
            text(self.message, self.half_dimension,
                 self.half_dimension - self.half_grid_len)
        if self.win != "":
            text(self.win, self.half_dimension, self.half_dimension)
        elif self.message != "No legal move" and self.turn != "":
            text(self.turn, self.half_dimension, self.half_dimension)

    def input(self, message='Please enter your name:'):
        """Get the player's name"""
        from javax.swing import JOptionPane
        answer = (JOptionPane.showInputDialog(frame, message))
        if answer:
            return answer
        elif answer == "":
            return "Unknown"
        else:
            return answer

    def get_player_name(self):
        """Get the user's name from input function and save it in a file"""
        answer = self.input()
        self.save_name_in_file(answer)

    def find_max_score(self, file_name):
        """Read the first line in the file, extract the score which should be
        the highest"""
        max_score = 0
        try:
            with open(file_name) as file:
                max_score = int(file.readline().strip().split(" ")[-1])
        except Exception:
            with open(file_name, "w+") as file:
                file.write("")
        return max_score

    def save_name_in_file(self, name, file_name="scores.txt"):
        """Promped the player's name, if player input nothing, just
        ignore it, if the player's score is the highest, put it in the first
        place, otherwise, append it at the end"""
        self.black_disk_count = self.show_score()[0]
        if name is not None and name != "Unknown":
            add_content = name + " " + str(self.black_disk_count) + "\n"
            score = self.find_max_score(file_name)
            if self.black_disk_count > score:
                with open(file_name, "r+") as file:
                    readcontent = file.read()
                    file.seek(0, 0)
                    file.write(add_content)
                    file.write(readcontent)
            else:
                with open(file_name, "a") as file:
                    file.write(add_content)

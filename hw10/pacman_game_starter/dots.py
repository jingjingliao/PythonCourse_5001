from dot import Dot


class Dots:
    """A collection of dots."""

    def __init__(self, WIDTH, HEIGHT,
                 LEFT_VERT, RIGHT_VERT,
                 TOP_HORIZ, BOTTOM_HORIZ):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TH = TOP_HORIZ
        self.BH = BOTTOM_HORIZ
        self.LV = LEFT_VERT
        self.RV = RIGHT_VERT
        self.SPACING = 75
        self.EAT_DIST = 50
        # Initialize four rows of dots, based on spacing and width of the maze
        self.top_row = [Dot(self.SPACING * i, self.TH)
                        for i in range(self.WIDTH//self.SPACING + 1)]
        self.bottom_row = [Dot(self.SPACING * i, self.BH)
                           for i in range(self.WIDTH//self.SPACING + 1)]
        self.left_col = [Dot(self.LV, self.SPACING * i)
                         for i in range(self.HEIGHT//self.SPACING + 1)]
        self.right_col = [Dot(self.RV, self.SPACING * i)
                          for i in range(self.HEIGHT//self.SPACING + 1)]

    def display(self):
        """Calls each dot's display method"""
        for i in range(0, len(self.top_row)):
            self.top_row[i].display()
        for i in range(0, len(self.bottom_row)):
            self.bottom_row[i].display()
        for i in range(0, len(self.left_col)):
            self.left_col[i].display()
        for i in range(0, len(self.right_col)):
            self.right_col[i].display()

    def eat(self, x, y):
        # if the dot in the top row, the absolute x_distance of dot location
        # and pacman's location is less than 50(eat distance) or more than 550(
        # width - eat_distance when pacman is on the edge), their y_distance
        # should also within eat_distance, then the dot will be eaten. It is
        # the same for dot in bottom row, or left_col, or right_col
        for dot in self.top_row:
            if ((abs(dot.x - x) <= self.EAT_DIST or
                 abs(dot.x - x) >= self.WIDTH - self.EAT_DIST) and
                    abs(dot.y - y) <= self.EAT_DIST):
                self.top_row.remove(dot)

        for dot in self.bottom_row:
            if ((abs(dot.x - x) <= self.EAT_DIST
                 or abs(dot.x - x) >= self.WIDTH - self.EAT_DIST)
                    and abs(dot.y - y) <= self.EAT_DIST):
                self.bottom_row.remove(dot)

        for dot in self.left_col:
            if (abs(dot.x - x) <= self.EAT_DIST
                and (abs(dot.y - y) <= self.EAT_DIST
                     or abs(dot.y - y) >= self.WIDTH - self.EAT_DIST)):
                self.left_col.remove(dot)

        for dot in self.right_col:
            if (abs(dot.x - x) <= self.EAT_DIST
                and (abs(dot.y - y) <= self.EAT_DIST
                     or abs(dot.y - y) >= self.WIDTH - self.EAT_DIST)):
                self.right_col.remove(dot)

    def dots_left(self):
        """Returns the number of remaing dots in the collection"""
        return (len(self.top_row) +
                len(self.bottom_row) +
                len(self.left_col) +
                len(self.right_col))

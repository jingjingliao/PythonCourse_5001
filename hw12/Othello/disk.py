class Disk:
    def __init__(self, column, row, color):
        self.column = column
        self.row = row
        self.color = color
        self.diameter = 90
        self.spacing = 100
        self.half_space = self.spacing // 2

    def draw_disk(self):
        fill(self.color)
        ellipse(self.column * self.spacing + self.half_space,
                self.row * self.spacing + self.half_space,
                self.diameter, self.diameter)

    def change_color(self, color):
        self.color = color
        self.draw_disk()

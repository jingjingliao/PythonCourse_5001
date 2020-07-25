class Board:
    def __init__(self, grid, DIMENSION, GRID_LEN):
        self.grid = grid
        self.dimension = DIMENSION
        self.grid_len = GRID_LEN
        self.space = self.dimension // self.grid_len

    def display(self):
        """Draw a board, and change the board based on the grid information"""
        start_point = 0
        start_hori_line = 0
        start_verti_line = 0
        end_hori_line = 0
        end_verti_line = 0
        WEIGHT = 2

        for _ in range(self.space):
            start_hori_line += self.grid_len
            end_hori_line += self.grid_len

            start_verti_line += self.grid_len
            end_verti_line += self.grid_len

            strokeWeight(WEIGHT)
            line(start_point, start_hori_line, self.dimension, end_hori_line)
            line(start_verti_line, start_point, end_verti_line, self.dimension)

        for i in range(self.space):
            for j in range(self.space):
                if self.grid[i][j] is not None:
                    self.grid[i][j].draw_disk()

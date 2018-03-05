class Board:

    def __init__(self):

        # The board grid will be a 5x5 2d list of cells
        # Each cell will be a list of characters occupying it
        self.grid = [[None for x in range(5)] for y in range(5)]

    def add(self, ent, x, y):

        assert x >= 0 and x <= 4, "x must be in range [0,4], x = " + str(x)
        assert y >= 0 and y <= 4, "y must be in range [0,4], y = " + str(y)

        self.grid[y][x] = ent
        ent.set_coordinates(x, y)

    def __str__(self):

        words = ""

        for row in self.grid:
            for cell in row:

                if cell is None:
                    words = words + " - "
                else:
                    words = words + str(cell)

            words = words + "\n"

        return words

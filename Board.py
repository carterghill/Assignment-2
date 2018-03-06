class Board:

    def __init__(self):

        # The board grid will be a 5x5 2d list of cells
        # Each cell will be a list of characters occupying it
        self.grid = [[None for x in range(5)] for y in range(5)]

    def add(self, ent, x, y):

        assert x >= 1 and x <= 5, "x must be in range [1, 5], x = " + str(x)
        assert y >= 1 and y <= 5, "y must be in range [1, 5], y = " + str(y)

        self.grid[abs(y-5)][x-1] = ent
        ent.set_coordinates(x, y)

    def get_cell(self, x, y):

        assert x >= 1 and x <= 5, "x must be in range [1,5], x = " + str(x)
        assert y >= 1 and y <= 5, "y must be in range [1,5], y = " + str(y)

        return self.grid[abs(y-5)][x-1]

    def delete(self, x, y):

        assert x >= 1 and x <= 5, "x must be in range [1, 5], x = " + str(x)
        assert y >= 1 and y <= 5, "y must be in range [1, 5], y = " + str(y)

        self.grid[abs(y-5)][x-1] = None


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

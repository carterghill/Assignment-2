from Queen import Queen
from Dragon import Dragon
from Wight import Wight


class Board:

    def __init__(self):

        # The board grid will be a 5x5 2d list of cells
        # Each cell will be a list of characters occupying it
        self.grid = [[[] for x in range(5)] for y in range(5)]
        self.add(Queen(), 0, 2)
        self.add(Dragon(), 1, 1)
        self.add(Dragon(), 1, 2)
        self.add(Dragon(), 1, 3)
        self.add(Wight(), 4, 1)
        self.add(Wight(), 4, 2)
        self.add(Wight(), 4, 3)
        self.add(Wight(), 4, 0)
        self.add(Wight(), 4, 4)

    def add(self, ent, x, y):

        assert x >= 0 and x <= 4, "x must be in range [0,4], x = " + str(x)
        assert y >= 0 and y <= 4, "y must be in range [0,4], y = " + str(y)

        self.grid[x][y].append(ent)
        ent.set_coordinates(x, y)

    def to_string(self):

        words = ""

        for row in self.grid:
            for cell in row:

                # If no one is on the cell, its length will be 0
                if len(cell) == 0:
                    words = words + " - "

                # If no one is on the cell, its length will be 0
                if len(cell) == 1:
                    if type(cell[0]) is Queen:
                        words = words + " Q "
                    elif type(cell[0]) is Dragon:
                        words = words + " D "
                    elif type(cell[0]) is Wight:
                        words = words + " W "
                    else:
                        words = words + str(type(cell[0]))

            words = words + "\n"

        return words

b = Board()
print(b.to_string())

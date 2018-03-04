class Board:

    def __init__(self):

        # The board grid will be a 5x5 2d list of cells
        # Each cell will be a list of characters occupying it
        self.grid = [[[] for x in range(5)] for y in range(5)]

    def to_string(self):

        words = ""

        for row in self.grid:
            for cell in row:

                # If no one is on the cell, its length will be 0
                if len(cell) == 0:
                    words = words + " - "

            words = words + "\n"

        return words

b = Board()
print(b.to_string())

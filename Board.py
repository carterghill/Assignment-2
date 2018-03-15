class Board:

    def __init__(self):

        """
        Purpose:
            Creates a 5x5 board ADT
        Pre-Conditions:
            :param self: The board that is going to be created
        Return:
            :return: the board
        """

        # The board grid will be a 5x5 2d list of cells
        # Each cell will be a list of characters occupying it
        self.grid = [[None for x in range(5)] for y in range(5)]

    def copy(self):

        """
        Purpose:
            Creates a copy of the board and gives it back
        Pre-Conditions:
            :param self: An existing board class
        Return:
            :return: a new board
        """

        b = Board()

        for i in range(5):
            for j in range(5):
                if (str(self.grid[i][j]) == " W "
                or str(self.grid[i][j]) == " Q "
                or str(self.grid[i][j]) == " D "):
                    b.grid[i][j] = self.grid[i][j].copy(b)

        return b

    def add(self, ent, x, y):

        """
        Purpose:
            Adds an entity to the given x and y
        Pre-Conditions:
            :param self: the board that the ent will be added onto
            :param ent: The entity being placed onto the board
            :param x: The entity's x position on the Board
            :param y: The entity's y position on the Board
        Post-conditions:
            :self: Will contain the entity at x and y
        """

        assert x >= 1 and x <= 5, "x must be in range [1, 5], x = " + str(x)
        assert y >= 1 and y <= 5, "y must be in range [1, 5], y = " + str(y)

        self.grid[abs(y-5)][x-1] = ent
        ent.set_coordinates(x, y)

    def get_cell(self, x, y):

        """
        Purpose:
            Get the cell stored at the x and y
        Pre-Conditions:
            :param self: the board
            :param x: The x position on the Board
            :param y: The y position on the Board
        Return:
            :ent: The entity stored at x and y or None
        """

        assert x >= 1 and x <= 5, "x must be in range [1,5], x = " + str(x)
        assert y >= 1 and y <= 5, "y must be in range [1,5], y = " + str(y)

        return self.grid[abs(y-5)][x-1]

    def delete(self, x, y):

        """
        Purpose:
            Delete the entity store at position x and y
        Pre-Conditions:
            :param self: the board that the ent will be added onto
            :param x: The entity's x position on the Board
            :param y: The entity's y position on the Board
        Post-conditions:
            : The cell at x and y will be None
        """

        assert x >= 1 and x <= 5, "x must be in range [1, 5], x = " + str(x)
        assert y >= 1 and y <= 5, "y must be in range [1, 5], y = " + str(y)

        self.grid[abs(y-5)][x-1] = None

    def has_queen(self):

        """
        Purpose:
            Checks if there is currently a queen on the game board
        Pre-Conditions:
            :param self: the board that we are checking
        Return:
            :True: if the board contains a queen
            :False: if the board does not contain a queen
        """

        q = False

        for i in range(1, 6):
            for j in range(1, 6):
                if str(self.get_cell(i, j)) == " Q ":
                    q = True

        return q


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

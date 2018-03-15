##################################
# By  : Carter Hill & Bryce Keeler
# NSID: cgh418      & bpk802
# Date: March 14, 2018
# For : Assignment#2 - CMPT 317
##################################

from Board import Board

class Dragon:

    def __init__(self, board, x, y):
        """
        Purpose:
			Initializes a dragon piece
		Pre-Conditions:
            :param board: The board object the piece will be placed on
			:param x    : The x-coordinate of the piece
			:param y    : The y-coordinate of the piece
        Return:
            N/A
        """

        self.x = x
        self.y = x

        assert type(board) is Board, "Expect Board, got: " + str(type(board))
        self.board = board
        board.add(self, x, y)

    def copy(self, board):
        """
        Purpose:
            Creates a copy of the current dragonn piece
        Pre-Conditions:
            :param board: The board that the piece will be placed on
        Return:
            :return: the copy
        """

        return Dragon(board, int(self.x), int(self.y))

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

    def move(self, coor):
        """
        Purpose:
			Moves the current piece to a specified coordinate
		Pre-Conditions:
            :param coor: A tuple describing the coordinates the piece will be moved to
        Return:
			N/A
        """
        x = coor[0]
        y = coor[1]
        assert x >= 1 and x <= 5, "x must be in range [1, 5], x = " + str(x)
        assert y >= 1 and y <= 5, "y must be in range [1, 5], y = " + str(y)

        self.board.delete(self.x, self.y)
        self.x = coor[0]
        self.y = coor[1]
        self.board.add(self, self.x, self.y)

    def evaluate(self):
		# Evaluation for the Dragon piece
        return 5 + abs(self.y-6)*2

    def get_moves(self):
        """
        Purpose:
            Gets a list of coordinates that the Queen ca move to
        Pre-Conditions:
            :param self: a Queen on the board
        Return:
            :return: list of moves
        """

        moves = []
        # If x is greater than 1, check possible moves on left side
        if self.x > 1:
            if (self.board.get_cell(self.x-1, self.y) is None
            or str(self.board.get_cell(self.x-1, self.y)) == " W "):
                moves.append([self.x-1, self.y])
            if self.y > 1:
                if (self.board.get_cell(self.x-1, self.y-1) is None
                or str(self.board.get_cell(self.x-1, self.y-1)) == " W "):
                    moves.append([self.x-1, self.y-1])
            if self.y < 5:
                 if (self.board.get_cell(self.x-1, self.y+1) is None
                 or str(self.board.get_cell(self.x-1, self.y+1)) == " W "):
                    moves.append([self.x-1, self.y+1])

        # If x is less than 5, check possible moves on the right side
        if self.x < 5:
            if (self.board.get_cell(self.x+1, self.y) is None
            or str(self.board.get_cell(self.x+1, self.y)) == " W "):
                moves.append([self.x+1, self.y])
            if self.y > 1:
                if (self.board.get_cell(self.x+1, self.y-1) is None
                or str(self.board.get_cell(self.x+1, self.y-1)) == " W "):
                    moves.append([self.x+1, self.y-1])
            if self.y < 5:
                if (self.board.get_cell(self.x+1, self.y+1) is None
                or str(self.board.get_cell(self.x+1, self.y+1)) == " W "):
                    moves.append([self.x+1, self.y+1])

        # Check if you can move forward or backward
        if self.y > 1:
            if (self.board.get_cell(self.x, self.y-1) is None
            or str(self.board.get_cell(self.x, self.y-1)) == " W "):
                moves.append([self.x, self.y-1])
        if self.y < 5:
            if (self.board.get_cell(self.x, self.y+1) is None
            or str(self.board.get_cell(self.x, self.y+1)) == " W "):
                moves.append([self.x, self.y+1])

        return moves

    def __str__(self):
        return " D "

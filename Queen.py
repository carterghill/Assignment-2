from Board import Board
from Wight import Wight
from Dragon import Dragon

class Queen:

    def __init__(self, board, x, y):

        self.x = x
        self.y = x

        assert type(board) is Board, "Expect Board, got: " + str(type(board))
        self.board = board
        board.add(self, x, y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

    def move(self, coor):

        self.board.delete(self.x, self.y)
        self.x = coor[0]
        self.y = coor[1]
        self.board.add(self, self.x, self.y)

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
        if self.x > 1:
            if (self.board.get_cell(self.x-1, self.y) is None
            or str(self.board.get_cell(self.x-1, self.y)) is " W "):
                moves.append([self.x-1, self.y])
            if self.y > 1:
                if (self.board.get_cell(self.x-1, self.y-1) is None
                or str(self.board.get_cell(self.x-1, self.y-1)) is " W "):
                    moves.append([self.x-1, self.y-1])
            if self.y < 5:
                 if (type(self.board.get_cell(self.x-1, self.y+1)) is None
                 or type(self.board.get_cell(self.x-1, self.y+1)) is Wight):
                    moves.append([self.x-1, self.y+1])

        if self.x < 5:
            if (self.board.get_cell(self.x+1, self.y) is None
            or str(self.board.get_cell(self.x+1, self.y)) is " W "):
                moves.append([self.x+1, self.y])
            if self.y > 1:
                if (self.board.get_cell(self.x+1, self.y-1) is None
                or str(self.board.get_cell(self.x+1, self.y-1)) is " W "):
                    moves.append([self.x+1, self.y-1])
            if self.y < 5:
                if (type(self.board.get_cell(self.x+1, self.y+1)) is None
                or type(self.board.get_cell(self.x+1, self.y+1)) is Wight):
                    moves.append([self.x+1, self.y+1])

        if self.y > 1:
            if (self.board.get_cell(self.x, self.y-1) is None
            or type(self.board.get_cell(self.x, self.y-1)) is Wight):
                moves.append([self.x, self.y-1])
        if self.y < 5:
            if (self.board.get_cell(self.x, self.y+1) is None
            or type(self.board.get_cell(self.x, self.y+1)) is Wight):
                moves.append([self.x, self.y+1])

        return moves

    def __str__(self):
        return " Q "

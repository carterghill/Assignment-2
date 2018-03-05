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
        if self.x > 0:
            if self.board.grid[self.y-1][self.x] is None or type(self.board.grid[self.y-1][self.x]) is Wight:
                moves.append([self.x-1, self.y])
            if self.y > 0 and type(self.board.grid[self.y-1][self.x-1]) is None or type(self.board.grid[self.y-1][self.x-1]) is Wight:
                moves.append([self.x-1, self.y-1])
            if self.y < 4 and type(self.board.grid[self.y-1][self.x+1]) is None or type(self.board.grid[self.y-1][self.x+1]) is Wight:
                moves.append([self.x-1, self.y+1])

        if self.x < 4:
            if self.board.grid[self.y+1][self.x] is None or type(self.board.grid[self.y+1][self.x]) is Wight:
                moves.append([self.x+1, self.y])
            if self.y > 0 and type(self.board.grid[self.y+1][self.x-1]) is None or type(self.board.grid[self.y+1][self.x-1]) is Wight:
                moves.append([self.x+1, self.y-1])
            if self.y < 4 and type(self.board.grid[self.y+1][self.x+1]) is None or type(self.board.grid[self.y+1][self.x+1]) is Wight:
                moves.append([self.x+1, self.y+1])

        if self.y > 0 and type(self.board.grid[self.y][self.x-1]) is None or type(self.board.grid[self.y][self.x-1]) is Wight:
            moves.append([self.x, self.y-1])
        if self.y < 4 and type(self.board.grid[self.y][self.x+1]) is None or type(self.board.grid[self.y][self.x+1]) is Wight:
            moves.append([self.x, self.y+1])

        return moves

    def __str__(self):
        return " Q "

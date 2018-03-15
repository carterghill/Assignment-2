from Board import Board

class Wight:

    def __init__(self, board, x, y):

        self.x = x
        self.y = x

        assert type(board) is Board, "Expect Board, got: " + str(type(board))
        self.board = board
        board.add(self, x, y)

    def copy(self, board):

        return Wight(board, int(self.x), int(self.y))

    def evaluate(self):

        x = 1
        y = 1

        for i in range(1, 6):
            for j in range(1, 6):
                p = self.board.get_cell(i, j)
                if str(p) == " Q ":
                    x = i
                    y = j

        x = abs(self.x - x)
        y = abs(self.y - y)

        # Distance away from Queen
        dis = x + y

        # Value will be highest if you're distance of 2 from Queen
        return (self.y+8 - abs(dis-2))

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

    def move(self, coor):

        x = coor[0]
        y = coor[1]
        assert x >= 1 and x <= 5, "x must be in range [1, 5], x = " + str(x)
        assert y >= 1 and y <= 5, "y must be in range [1, 5], y = " + str(y)

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
            if self.board.get_cell(self.x-1, self.y) is None:
                moves.append([self.x-1, self.y])
            if self.y > 1:
                if (str(self.board.get_cell(self.x-1, self.y-1)) == " Q "
                or str(self.board.get_cell(self.x-1, self.y-1)) == " D "):
                    moves.append([self.x-1, self.y-1])
            if self.y < 5:
                if (str(self.board.get_cell(self.x-1, self.y+1)) == " Q "
                or str(self.board.get_cell(self.x-1, self.y+1)) == " D "):
                    moves.append([self.x-1, self.y+1])

        if self.x < 5:
            if self.board.get_cell(self.x+1, self.y) is None:
                moves.append([self.x+1, self.y])
            if self.y > 1:
                if (str(self.board.get_cell(self.x+1, self.y-1)) == " Q "
                or str(self.board.get_cell(self.x+1, self.y-1)) == " D "):
                    moves.append([self.x+1, self.y-1])
            if self.y < 5:
                if (str(self.board.get_cell(self.x+1, self.y+1)) == " Q "
                or str(self.board.get_cell(self.x+1, self.y+1)) == " D "):
                    moves.append([self.x+1, self.y+1])

        if (self.y > 1 and self.board.get_cell(self.x, self.y-1) is None):
            moves.append([self.x, self.y-1])
        if self.y < 5 and self.board.get_cell(self.x, self.y+1) is None:
            moves.append([self.x, self.y+1])

        return moves

    def __str__(self):
        return " W "

from Queen import Queen
from Wight import Wight
from Dragon import Dragon
from Board import Board

class Game:

    def __init__(self):

        self.board = Board()        # The game board
        Queen(self.board, 3, 5)     # Place Queen at top center
        Dragon(self.board, 2, 4)    # Three Dragons in front of the queen
        Dragon(self.board, 3, 4)
        Dragon(self.board, 4, 4)
        Wight(self.board, 1, 1)     # Wight's all along the bottom row
        Wight(self.board, 2, 1)
        Wight(self.board, 3, 1)
        Wight(self.board, 4, 1)
        Wight(self.board, 5, 1)

        self.player = 2             # Player whose turn it is

    def get_pieces(self):

        pieces = []

        for i in range(1, 6):
            for j in range(1, 6):
                p = self.board.get_cell(i, j)
                if self.player == 2 and type(p) is Wight:
                    pieces.append(p)
                elif self.player == 1 and (type(p) is Dragon or type(p) is Queen):
                    pieces.append(p)

        return pieces

    def select_piece(self, x=None):

        pieces = self.get_pieces()

        if x is None:
            for i in range(len(pieces)):
                print(str(i+1) + ":" + str(pieces[i]) + str(pieces[i].get_coordinates()))

            x = int(input("Select piece by #: "))

        assert x <= len(pieces), "Seleced " + str(x) + " but only have " + str(len(pieces))
        assert x > 0, "Piece # must be higher than 0"

        x = x - 1

        return pieces[x]

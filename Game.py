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
        self.gameover = False       # Game over flag

    def get_pieces(self):

        pieces = []
        queen_found = False         # Used for game over detection

        for i in range(1, 6):
            for j in range(1, 6):
                p = self.board.get_cell(i, j)
                if type(p) is Queen:
                    queen_found = True
                if self.player == 2 and type(p) is Wight:
                    pieces.append(p)
                elif self.player == 1 and (type(p) is Dragon or type(p) is Queen):
                    pieces.append(p)

        if not queen_found:
            self.gameover = True

        return pieces

    def select_piece(self, x=None):

        pieces = self.get_pieces()

        if x is None:
            print(self)
            for i in range(len(pieces)):
                print(str(i+1) + ":" + str(pieces[i]) + str(pieces[i].get_coordinates()))

            x = int(input("\nSelect piece by #: "))

        assert x <= len(pieces), "Seleced " + str(x) + " but only have " + str(len(pieces))
        assert x > 0, "Piece # must be higher than 0"

        return pieces[x-1]

    def select_move(self, piece=None, move=None):

        piece = self.select_piece(piece)
        moves = piece.get_moves()

        if move is None:
            print("\nMoves for" + str(piece) + "at " + str(piece.get_coordinates()))
            for m in moves:
                print("1. " + str(m))

            move = int(input("\nSelect move by #: "))

        piece.move(moves[move-1])

    def __str__(self):
        s = "Player " + str(self.player) + "\'s turn.\n\n"
        return (s + str(self.board))

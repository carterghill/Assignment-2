from Queen import Queen
from Wight import Wight
from Dragon import Dragon
from Board import Board
from Player1AI import Player1AI
from Player2AI import Player2AI

class Game:

    def __init__(self, player1_is_ai=True, player2_is_ai=True):

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

        if player1_is_ai:
            self.ai1 = Player1AI()
        else:
            self.ai1 = None

        if player2_is_ai:
            self.ai2 = Player2AI(game=self)
        else:
            self.ai2 = None

    def copy(self):

        g = Game()
        g.board = self.board.copy()
        g.player = int(self.player)
        g.ai1 = self.ai1
        g.ai2 = self.ai2

        return g

    def get_pieces(self, player=None):

        if player == None:
            player = self.player

        pieces = []

        for i in range(1, 6):
            for j in range(1, 6):
                p = self.board.get_cell(i, j)
                if player == 2 and type(p) is Wight:
                    pieces.append(p)
                elif player == 1 and (type(p) is Dragon or type(p) is Queen):
                    pieces.append(p)

        return pieces

    def select_piece(self, x=None):

        pieces = self.get_pieces()

        if x is None:
            print(self)
            for i in range(len(pieces)):
                print(str(i+1) + ":" + str(pieces[i]) + str(pieces[i].get_coordinates()))

            x = int(input("\nSelect piece by #: "))

        assert x <= len(pieces), "Seleced piece # " + str(x) + " but only have " + str(len(pieces))
        assert x > 0, "Piece # must be higher than 0"

        return pieces[x-1]

    def select_move(self, piece=None, move=None):

        piece = self.select_piece(piece)
        moves = piece.get_moves()

        if move is None:
            print("\nMoves for" + str(piece) + "at " + str(piece.get_coordinates()))
            for i in range(len(moves)):
                print(str(i+1) + ". " + str(moves[i]))

            move = int(input("\nSelect move by #: "))

        assert move <= len(moves), "Seleced " + str(x) + " but only have " + str(len(moves))
        assert move > 0, "Move # must be higher than 0"

        piece.move(moves[move-1])

        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def victory(self):

        for i in range(1, 6):
            for j in range(1, 6):
                if str(self.board.get_cell(i, j)) == " Q ":
                    if j == 1:
                        return 1
                    else:
                        return None

        return 2

    def play(self):

        while True:

            if self.victory() == 1:
                print(self.board)
                print("\n\n/////////////////\n Player 1 Wins!! \n/////////////////\n")
                break

            if self.victory() == 2:
                print(self.board)
                print("\n\n/////////////////\n Player 2 Wins!! \n/////////////////\n")
                break

            if self.ai2 is not None and self.player == 2:
                print(self.board)
                self.ai2.move()

            if self.ai1 is not None and self.player == 1:
                print(self.board)
                print(self.ai1)
                print(self.ai2)
                self = self.ai1.move(self)
                self.player = 2



            if self.ai1 is None or self.ai2 is None:

                self.select_move()

    def __str__(self):
        s = "Player " + str(self.player) + "\'s turn.\n\n"
        return (s + str(self.board))

"""
g1 = Game()
g1.select_move(1, 1)
print(g1)

g2 = g1.copy()
g2.select_move(1, 1)
print(g1)
print(g2)"""

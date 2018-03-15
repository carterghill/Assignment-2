##################################
# By  : Carter Hill & Bryce Keeler
# NSID: cgh418      & bpk802
# Date: March 14, 2018
# For : Assignment#2 - CMPT 317
##################################

from Queen import Queen
from Wight import Wight
from Dragon import Dragon
from Board import Board
from AI import AI

class Game:

    def __init__(self, player1_is_ai=True, player2_is_ai=True):

        """
        Purpose:
            Creates a game instance with a board and all the pieces
        Pre-Conditions:
            :param player1_is_ai: Whether or not player 1 is an AI
            :param player2_is_ai: Whether or not player 2 is an AI
        Return:
            :return: A new game state
        """

		# Initializing the starting game board
        self.board = Board()        # The game board
        self.parent = None          # The previous board state
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

		#Checking whether the game is in AI mode or not.
        if player1_is_ai:
            self.ai1 = AI()
        else:
            self.ai1 = None

        if player2_is_ai:
            self.ai2 = AI()
        else:
            self.ai2 = None

    def copy(self):
        """
        Purpose:
            Makes a copy of the current game state
        Pre-Conditions:
            N/A
        Return:
            :return: A copy of the current game state, self
        """

        g = Game()
        g.board = self.board.copy()
        g.player = int(self.player)
        g.ai1 = self.ai1
        g.ai2 = self.ai2

        return g

    def get_pieces(self, player=None):
        """
        Purpose:
			makes a list of all the pieces available for a particular player.
        Pre-Conditions:
            :param player: Chooses the player whose pieces must be returned. (i.e. player 1 gets back Queen and Dragons, 2 gets Wights)
        Return:
            :return: A list containing all the pieces available for a "player"
        """

        if player == None:
            player = self.player

        pieces = []

		# Looping through the board and appending pieces to the list which have the correct type.
        for i in range(1, 6):
            for j in range(1, 6):
                p = self.board.get_cell(i, j)
                if player == 2 and type(p) is Wight:
                    pieces.append(p)
                elif player == 1 and (type(p) is Dragon or type(p) is Queen):
                    pieces.append(p)

        return pieces

    def select_piece(self, x=None):
        """
        Purpose:
            Finds and outputs all of the pieces available to move for a player to the command line.
			The player can then select which piece among these to return.
        Pre-Conditions:
            :param x: Index of the piece to be chosen. This parameter is slightly unecessary,
					  as the function is never used from a place where x might be preemptively
					  known.
        Return:
            :return: The piece which was selected.
        """

		# Finding the available pieces available to the current player.
        pieces = self.get_pieces()

        if x is None:
            print(self)
            for i in range(len(pieces)):
                print(str(i+1) + ":" + str(pieces[i]) + str(pieces[i].get_coordinates()))

            x = int(input("\nSelect piece by #: "))

        assert x <= len(pieces), "Selected piece # " + str(x) + " but only have " + str(len(pieces))
        assert x > 0, "Piece # must be higher than 0"

        return pieces[x-1]

    def select_move(self, piece=None, move=None):
        """
        Purpose:
			Shows the current player the moves available for a
        Pre-Conditions:
            :param piece: The piece chosen by the player (returned by the select_piece function)
            :param  move: Index of the chosen move. This parameter is slightly unecessary.
        Return:
            :return: A new game state
        """
        piece = self.select_piece(piece)
        moves = piece.get_moves()

        if move is None:
            print("\nMoves for" + str(piece) + "at " + str(piece.get_coordinates()))
            for i in range(len(moves)):
                print(str(i+1) + ". " + str(moves[i]))

            move = int(input("\nSelect move by #: "))

        assert move <= len(moves), "Seleced " + str(move) + " but only have " + str(len(moves))
        assert move > 0, "Move # must be higher than 0"

        piece.move(moves[move-1])

		# Toggles the active player after a move has been made
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def victory(self):
        """
        Purpose:
            Asseses whether the current game state is a victory state for one of the players
        Pre-Conditions:
			N/A
        Return:
            :return: Returns 1 if player one has won, returns 2 if palyer 2 has won, returns none if neither has won.
        """
        for i in range(1, 6):
            for j in range(1, 6):
                if str(self.board.get_cell(i, j)) == " Q ":
                    if j == 1:
                        return 1
                    else:
                        return None

        return 2

    def evaluate(self):
        """
        Purpose:
			Evaluates the current game state, and returns a utility value based on this.
        Pre-Conditions:
            N/A
        Return:
            :return: An integer utility value assesing the game state.
        """
        pieces_1 = self.get_pieces(1)
        pieces_2 = self.get_pieces(2)

        p1_score = 0
        p2_score = 0

		# Looping through all the pieces of Player One, and returning their respective evaluations
        for p in pieces_1:
            p1_score = p1_score + p.evaluate()
		# Same thing for Player Two
        for p in pieces_2:
            p2_score = p2_score + p.evaluate()

		# Giving an absolute value to a winning game state.
        if self.victory() == 1:
            p1_score = 999999
        elif self.victory() == 2:
            p2_score = 999999

        # Returning the difference in the score.
        return p1_score - p2_score

    def successor(self):
        """
        Purpose:
            Finds all possible game states which are availabe from the current game state.
        Pre-Conditions:
            N/A
        Return:
            :return: A list containing all possible games states available from the current one
        """

        pieces = self.get_pieces()
        games = []

		# Looping through all the pieces on the board, and finding all game states available to the current state
        for p in pieces:
            moves = p.get_moves()
            for move in moves:
                g = self.copy()
                g_piece = g.board.get_cell(p.x, p.y)
                g_piece.move(move)
                if g.player == 2:
                    g.player = 1
                else:
                    g.player = 2
                games.append(g)

        return games

    def play(self):
        """
        Purpose:
            Runs the game until someone has won
        Pre-Conditions:
            N/A
        Return:
			N/A
        """
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
                self = AI.move(3, self, 2)
                self.player = 1

            if self.ai1 is not None and self.player == 1:
                print(self.board)
                self = AI.move(3, self, 1)
                self.player = 2

            if self.ai1 is None or self.ai2 is None:
                self.select_move()

        if len(AI.searchList) > 0:
            print("Average nodes searched: " + str((sum(AI.searchList)/len(AI.searchList))))
            print("Average time taken: " + str((sum(AI.timeList)/len(AI.timeList))))
            print("Total move time for AI: " + str(sum(AI.timeList)))

            print("Average nodes searched: " + str((sum(AI.searchListWithoutAlpha)/len(AI.searchListWithoutAlpha))))
            print("Average time taken: " + str((sum(AI.timeListWithoutAlpha)/len(AI.timeListWithoutAlpha))))
            print("Total move time for AI: " + str(sum(AI.timeListWithoutAlpha)))


    def __str__(self):
        s = "Player " + str(self.player) + "\'s turn.\n\n"
        return (s + str(self.board))

    def __int__(self):
        return self.evaluate()

    def __lt__(self, other):
        return self.evaluate() < other.evaluate()

    def __gt__(self, other):
        return self.evaluate() > other.evaluate()

    def __le__(self, other):
        return self.evaluate() <= other.evaluate()

    def __ge__(self, other):
        return self.evaluate() >= other.evaluate()

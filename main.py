from Queen import Queen
from Wight import Wight
from Dragon import Dragon
from Board import Board

board = Board()
Queen(board, 3, 1)
Dragon(board, 2, 2)
Dragon(board, 3, 2)
Dragon(board, 4, 2)
Wight(board, 1, 5)
Wight(board, 2, 4)
Wight(board, 3, 5)
Wight(board, 4, 5)
Wight(board, 5, 5)

moves = board.get_cell(3, 1).get_moves()
moves2 = board.get_cell(2, 4).get_moves()
print(str(moves) + "\n")
board.get_cell(3, 1).move(moves[0])
board.get_cell(2, 4).move(moves2[2])
print(board)

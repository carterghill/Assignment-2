from Queen import Queen
from Wight import Wight
from Dragon import Dragon
from Board import Board

board = Board()
Queen(board, 3, 5)
Dragon(board, 2, 4)
Dragon(board, 3, 4)
Dragon(board, 4, 4)
Wight(board, 1, 1)
Wight(board, 2, 1)
Wight(board, 3, 1)
Wight(board, 4, 1)
Wight(board, 5, 1)

moves = board.get_cell(1, 1).get_moves()
print(board.get_cell(1, 1))
print(moves)
board.get_cell(1, 1).move(moves[0])
moves = board.get_cell(1, 2).get_moves()
print(board)

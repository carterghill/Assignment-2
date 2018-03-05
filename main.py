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
Wight(board, 2, 2)
Wight(board, 3, 1)
Wight(board, 4, 1)
Wight(board, 5, 1)

"""moves = board.get_cell(3, 1).get_moves()
moves2 = board.get_cell(2, 4).get_moves()
moves3 = board.get_cell(3, 2).get_moves()
print(str(moves3) + "\n")
board.get_cell(3, 1).move(moves[0])
board.get_cell(2, 4).move(moves2[2])
print(board)
moves4 = board.get_cell(2, 3).get_moves()
print(moves4)"""
moves = board.get_cell(3, 1).get_moves()
print(board.get_cell(3, 1))
print(moves)
print(board)

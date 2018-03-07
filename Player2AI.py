class Player2AI:

    def __init__(self, game):

        self.game = game

    def move(self):

        pieces = self.game.get_pieces()
        if len(pieces) > 0:
            pieces[0].move(pieces[0].get_moves()[0])
        else:
            print("\nPlayer 2 has no pieces left!\n")

        self.game.player = 1

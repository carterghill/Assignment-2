class Player1AI:

    def __init__(self, game):

        self.game = game

    def move(self):

        pieces = self.game.get_pieces()
        pieces[0].move(pieces[0].get_moves()[0])

        self.game.player = 2

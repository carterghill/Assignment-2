class Player1AI:

    #def __init__(self):

        #self.game = game

    def move(self, game):

        pieces = game.get_pieces()
        games = []

        # Create a game instance for every possible move
        for p in pieces:
            m = p.get_moves()
            for move in m:
                g = game.copy()
                g_piece = g.board.get_cell(p.x, p.y)
                g_piece.move(move)
                g.player = 2
                games.append(g)

        # Look at every game instance, choose one with best outcome
        # Assume very bad outcome, replace with best found
        score = -9999999
        bestGame = None
        for g in games:
            s = self.net_score(g)
            print(s)
            if s > score:
                score = s
                bestGame = g

        if bestGame == None:
            game.player = 2
        else:
            return bestGame


    def net_score(self, game):

        pieces_1 = game.get_pieces(1)
        pieces_2 = game.get_pieces(2)

        p1_score = 0
        p2_score = 0

        for p in pieces_1:
            p1_score = p1_score + abs(p.y-6)
        for p in pieces_2:
            p2_score = p2_score + p.y

        return p1_score - p2_score

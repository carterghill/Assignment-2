#from Player1AI import Player1AI

class Player2AI:

    #def __init__(self, game):

        #self.game = game

    @staticmethod
    def get_games(game, r=1):

        # Use terminal function here
        print(game)
        pieces = game.get_pieces()
        games = []

        # Create a game instance for every possible move
        for p in pieces:
            m = p.get_moves()
            for move in m:
                g = game.copy()
                g_piece = g.board.get_cell(p.x, p.y)
                g_piece.move(move)
                g.player = 1
                games.append(g)

        if r > 1:
            glist = []
            for g in games:
                glist = glist + Player1AI.get_games(g, r-1)
            return glist
        else:
            return games

    def move(game, r=1):

        games = Player2AI.get_games(game, r)

        # Look at every game instance, choose one with best outcome
        # Assume very bad outcome, replace with best found
        score = -9999999
        bestGame = None
        for g in games:
            s = g.evaluate()
            if s > score:
                score = s
                bestGame = g

        # If there is no best game, the player did not have any moves
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

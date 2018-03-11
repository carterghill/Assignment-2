from Player2AI import Player2AI

class Player1AI:

    #def __init__(self, game):

        #self.game = game

    @staticmethod
    def get_games(game, r, initialStates):

        # Use terminal function here
        print(game)
        pieces = game.get_pieces()
        games = []

        if len(initialStates) == 0:
            initialStates = games

        # Create a game instance for every possible move
        for p in pieces:
            m = p.get_moves()
            for move in m:
                g = game.copy()
                g_piece = g.board.get_cell(p.x, p.y)
                g_piece.move(move)
                if g.player == 2:
                    g.player = 1
                else:
                    g.player = 2
                games.append(g)

        if r > 1:
            glist = []
            for i in range(len(games)):
                games[i].id = 1
                tempList, x = Player1AI.get_games(games[i], r-1, initialStates)
                glist = glist + tempList

            print(len(glist))
            return glist, initialStates
        else:
            return games, None

    @staticmethod
    def move(game, r=1):

        games, initialStates = Player1AI.get_games(game, r, [])

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
        return initialStates[bestGame.id]




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

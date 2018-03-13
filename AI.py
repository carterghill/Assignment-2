class AI:

    def move(depth, game, player):

        def minimax(depth, game, player):

            if depth == 0 or len(game.successor()) == 0:
                #print(game.evaluate())
                return game

            games = game.successor()

            if player == 1:
                bestGame = games[0]
                for g in games:
                    g.parent = game
                    bestGame = max(bestGame, minimax(depth - 1, g, 2))
                    #game.undo();

                return bestGame
            else:
                bestGame = games[0]
                for g in games:
                    g.parent = game
                    bestGame = min(bestGame, minimax(depth - 1, g, 1))
                    #game.undo()

                return bestGame

        best = minimax(depth, game, player)
        while best.parent is not None:
            if best.parent == game or best == game:
                return best
            best = best.parent

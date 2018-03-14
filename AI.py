class AI:

    def move(depth, game, player):

        def minimax(depth, game, player, alpha=None, beta=None):

            if depth == 0 or len(game.successor()) == 0:
                #print(game.evaluate())
                return game

            games = game.successor()

            if player == 1:
                bestGame = games[0]
                for g in games:
                    g.parent = game
                    bestGame = max(bestGame, minimax(depth - 1, g, 2, alpha, beta))
                    if alpha == None:
                        alpha = bestGame

                    if beta is not None:
                        if beta <= game:
                            return bestGame
                    alpha = max(alpha, bestGame)

                return bestGame
            else:
                bestGame = games[0]
                for g in games:
                    g.parent = game
                    bestGame = min(bestGame, minimax(depth - 1, g, 1, alpha, beta))
                    if beta==None:
                        beta = bestGame
                    else:
                        if alpha is not None:
                            if game <= alpha:
                                return bestGame
                        beta = min(beta, bestGame)

                return bestGame

        best = minimax(depth, game, player)
        while best.parent is not None:
            if best.parent == game or best == game:
                return best
            best = best.parent

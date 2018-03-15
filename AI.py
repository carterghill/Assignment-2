class AI:

    @staticmethod
    def move(depth, game, player):

        """
        Purpose:
            Gets a list of coordinates that the Queen ca move to
        Pre-Conditions:
            :param depth: how deep the recurssion will explore down the tree
            :param game: The game instance in which the move will be enacted on
            :param player: an int representing the play, either 1 or 2
        Return:
            :return: The game state with the decided move enacted on it
        """

        def minimax(depth, game, player, alpha=None, beta=None):

            # If at the bottom of the tree, or the game state has no successors
            if depth == 0 or len(game.successor()) == 0:
                return game

            games = game.successor()

            if player == 1:
                bestGame = games[0]

                # Do minimax on every successor
                for g in games:
                    g.parent = game
                    bestGame = max(bestGame, minimax(depth - 1, g, 2, alpha, beta))
                    if alpha == None:
                        alpha = bestGame

                    if beta is not None:
                        # Return bestgame right away if it can be pruned
                        if beta <= game:
                            return bestGame
                    alpha = max(alpha, bestGame)

                return bestGame
            else:
                bestGame = games[0]

                # Looking for the min since it's player 2
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

        # Minimax returns the resulting games state. Recursively go back to find
        # the parent immediately after the current game state
        best = minimax(depth, game, player)
        while best.parent is not None:
            if best.parent == game or best == game:
                return best
            best = best.parent

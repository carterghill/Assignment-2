from Player2AI import Player2AI

class Player1AI:

    #def __init__(self, game):

        #self.game = game

    @staticmethod
    def get_games(game, r, initialStates):

        # Use terminal function here

        games = game.successor()

        if len(initialStates) == 0:
            initialStates = games
            for i in range(len(games)):
                initialStates[i].id = i

        if r > 1:
            glist = []
            for i in range(len(games)):
                games[i].id = game.id
                tempList, x = Player1AI.get_games(games[i], r-1, initialStates)
                glist = glist + tempList

            #print(len(glist))
            return glist, initialStates
        else:
            return games, None

    @staticmethod
    def move(game, player, r=1):

        games, initialStates = Player1AI.get_games(game, r, [])

        # Look at every game instance, choose one with best outcome
        if player == 1:
            game = max(games)
        elif player == 2:
            game = min(games)

        # If there is no best game, the player did not have any moves
        return initialStates[game.id]

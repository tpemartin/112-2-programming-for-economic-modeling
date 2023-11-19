class Player:
    def __init__(self, name: str, strategies: list[str]):
        self.name = name
        self.strategies = strategies
        self.played_strategy = None
    def play(self, played_strategy):
        play_method(self, played_strategy)

class Game:
    games = []
    def __init__(self, player1, player2, payoffMatrix, name=None):
        self.name = name
        self.players = [player1, player2]
        self.payoffMatrix = payoffMatrix
    def payoff(self):
        played_strategies = self.players[0].played_strategy, self.players[1].played_strategy
        if all(played_strategies):
            # if both players have played their strategies
            return self.payoffMatrix[played_strategies]
        else:
            print("Not all players have played their strategies yet.")


# helper function
def payoff_method(game):
    played_strategies = game.players[0].played_strategy, game.players[1].played_strategy
    if all(played_strategies):
        # if both players have played their strategies
        return game.payoff_function(played_strategies)
    else:
        print("Not all players have played their strategies yet.")

def play_method(player, played_strategy):
    if played_strategy not in player.strategies:
        raise ValueError("Invalid strategy")
    else:
        player.played_strategy = played_strategy

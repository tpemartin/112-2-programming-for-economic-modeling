import random, string, json, os
import py.google.upload as gd
# pay attenton to the import path


class Player:
    def __init__(self, name, strategies):
        self.name = name
        self.strategies = strategies
        self.played_strategy = None
    def play(self, strategy):
        self.played_strategy = strategy
        return strategy

class Game:
    def __init__(self, playerA, playerB, payoffMatrix, cloud=False, gameId=None):
        if playerA and playerB and payoffMatrix:
            self.players = playerA, playerB
            self.payoffMatrix = payoffMatrix
            if cloud:
                self.gameId = create_gameId()
                for player in self.players:
                    player.playerId = create_playerId()
                upload_to_google_drive(self)
        elif gameId:
            self.load(self, gameId)
        else:
            raise Exception("Invalid arguments")
    def payoff(self):
        if self.players[0].played_strategy and self.players[1].played_strategy:
            return self.payoffMatrix[(self.players[0].played_strategy, self.players[1].played_strategy)]
        else:
            print("Not all players have played yet.")
    def load(self, gameId):
        gameInfo = load_from_google_drive(gameId)

# create a random id starting with a letter followed by 8 hex digits
def create_gameId():
    return random.choice(string.ascii_letters) + ''.join(random.choice(string.hexdigits) for _ in range(8)) 
def create_playerId():
    return 'p' + ''.join(random.choice(string.hexdigits) for _ in range(4))

def upload_to_google_drive(game):
    # pass
    gameFolderId = "1EdMkDrkSRATLiYMhjnn0Mk2_JFRzsx46"
    gameInstanceFolder = gd.create_folder_with_parentFolder(game.gameId, gameFolderId)
    gameJson = create_game_for_cloud(game)
    gd.upload_string_to_file(
        gameJson,
        'game.json',
        gameInstanceFolder['id']
    )


def stringfy_keys(d):
    return {str(k):v for k,v in d.items()}

def create_game_for_cloud(game):
    return json.dumps({
        "players": [
            {
        "name": player.name,
        "id": player.playerId,
        "strategies": player.strategies
    } for player in game.players],
        "payoffMatrix": stringfy_keys(game.payoffMatrix),
        "gameId": game.gameId
    })

def create_player_for_cloud(player):
    return json.dumps({
        "name": player.name,
        "id": player.playerId,
        "strategies": player.strategies
    })

def create_payoffMatrix_for_cloud(payoffMatrix):
    return json.dumps(stringfy_keys(payoffMatrix))

def load_from_google_drive(gameId):
    pass

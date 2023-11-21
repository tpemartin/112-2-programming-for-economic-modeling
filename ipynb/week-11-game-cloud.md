# Recap

## Interface


```python
players.name
players.strategies
players.played_strategy
players.play(...)

game.players
game.payoff_func
game.payoff(...)
```

## minor change

Instead of supplying `payoff_func` to `Game`, we now supply `payoff_matrix`. 

- See [week11_game.py](https://github.com/tpemartin/112-2-programming-for-economic-modeling/blob/main/py/game/week11_game.py)



```python
players.name
players.strategies
players.played_strategy
players.play(...)

game.players
game.payoff_matrix
game.payoff(...)
```

# Composition in another angle



```python
player1 = Player("player1", ['C', 'D'])
player2 = Player("player2", ['C', 'D'])
payoffMatrix = {
    ('C', 'C'): (-1, -1),
    ('C', 'D'): (-3, 0),
    ('D', 'C'): (0, -3),
    ('D', 'D'): (-2, -2)
}

game = Game(player1, player2, payoffMatrix)
```

We can design `Game` so that the usage becomes


```python
game = Game(player_names = ["player1", "player2"], 
            player_strategies = [
                ['C', 'D'],
                ['C', 'D']
            ], 
            payoffMatrix = {
            ('C', 'C'): (-1, -1),
            ('C', 'D'): (-3, 0),
            ('D', 'C'): (0, -3),
            ('D', 'D'): (-2, -2)
        })

[player1, player2] = game.players
```

Composites (i.e. players) are formed within the class definition. Here all init arguments for `Player` are used in `Game`'s init. 

- list comprehension
- unpacking

### list/dictionary comprehension

A lot of time, our for loop is to create a list or dictionary. Each iteration will create one element. If this is the case, we can use list/dictionary comprehension.



```python
# Example 1: Squaring numbers in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)
# Output: [1, 4, 9, 16, 25]

# Example 2: Filtering even numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
# Output: [2, 4, 6, 8, 10]

# Example 3: Creating a list of tuples
names = ['Alice', 'Bob', 'Charlie']
name_lengths = [(name, len(name)) for name in names]
print(name_lengths)
# Output: [('Alice', 5), ('Bob', 3), ('Charlie', 7)]

```

    [1, 4, 9, 16, 25]
    [2, 4, 6, 8, 10]
    [('Alice', 5), ('Bob', 3), ('Charlie', 7)]



```python
# Example 1: Squaring numbers and creating a dictionary
numbers = [1, 2, 3, 4, 5]
squared_dict = {x: x**2 for x in numbers}
print(squared_dict)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example 2: Filtering even numbers and creating a dictionary
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_dict = {x: x for x in numbers if x % 2 == 0}
print(even_dict)
# Output: {2: 2, 4: 4, 6: 6, 8: 8, 10: 10}

# Example 3: Creating a dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
merged_dict = {k: v for k, v in zip(keys, values)}
print(merged_dict)
# Output: {'a': 1, 'b': 2, 'c': 3}

```

    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    {2: 2, 4: 4, 6: 6, 8: 8, 10: 10}
    {'a': 1, 'b': 2, 'c': 3}


`zip` like zipper, zip two lists together. 


```python
zippedUp = zip(["John", "Mary", "Bob"], [58, 88, 72])
zippedUp
```




    <zip at 0x1042a5c40>




```python
list(zippedUp)
```




    [('John', 58), ('Mary', 88), ('Bob', 72)]



You can unzip a zip object by using `*` operator together with `zip` function.  


```python
[name, grade] = zip(*zippedUp)

name, grade
```




    (('John', 'Mary', 'Bob'), (58, 88, 72))



# Setup Module

Download [gamepy module](https://github.com/tpemartin/gamepy) and make it available to your environment
- [week-11-module.md](https://github.com/tpemartin/112-2-programming-for-economic-modeling/blob/main/ipynb/week-11-module.md)

If you setup gamepy correctly, you should be able to run the following cell without error.


```python
from gamepy.game import Game


game = Game(player_names = ["player1", "player2"], 
            player_strategies = [
                ['C', 'D'],
                ['C', 'D']
            ], 
            payoffMatrix = {
            ('C', 'C'): (-1, -1),
            ('C', 'D'): (-3, 0),
            ('D', 'C'): (0, -3),
            ('D', 'D'): (-2, -2)
        })

[player1, player2] = game.players
```

# Game Cloud

> Pile up to build something big.

## The Goal

A class that have pre-defined strategies and payoff matrix for various game, such as prisoner's dilemma, rock-paper-scissors, etc. Users only need to choose which one to play.

Users

  - choose which game to play. (A game instance associated with a prespecified game structure is created.)
  - choose to create a player.
  - choose to join a game room to meet the other player.




```python
gc = GameClient() # start app service on user side
game = gc.games("prisoner's dilemma")  # create the corresponding game instance
player1 = game.player("John") # create player instance
player1.join_room("room_id") # join an existing game room, if None, create a new room


```

## Understand your interface

 - Every name that follows by `.` is an instance, which means you have to design its class constructor.
 - When an instance created it is returned.

## Prototyping base on your interface


```python
class GameClient:
    def __init__(self):
        pass
    def games(self, game_name):
        return Games(game_name)

class Games:
    def __init__(self, game_name):
        self.game_name = game_name
    def player(self, player_name):
        return Player(player_name)
    
class Player:
    def __init__(self, player_name):
        self._player_name = player_name
    def join_room(self, room_id):
        pass

```

The `Game` class has to be redesigned to accommodate the new interface that only need game name to create a game instance. For general purpose we use `game_id` instead of `game_name`.


```python
class GameClient:
    def __init__(self):
        pass
    def games(self, game_id):
        return Games(game_id)


class Games:
    def __init__(self, game_id):
        self.game_id = game_id
    def player(self, player_name):
        return Player(player_name)
 
```

# Class property and class method

We want to redesign `Game` so that we can create a game instance with a pre-defined game structure.

## Two games

 - [gamepy.gamemenu](https://github.com/tpemartin/gamepy/blob/d0b49339417cd0d45d49dc725be849c529c19787/gamemenu/menu.py)



## paper scissor rock game

Paper-Scissor-Rock game can be expressed as the following normal form:

| | P | S | R |
| --- | --- | --- | --- |
| P | 0, 0 | -1, 1 | 1, -1 |
| S | 1, -1 | 0, 0 | -1, 1 |
| R | -1, 1 | 1, -1 | 0, 0 |


# Class property


```python
import gamepy.gamemenu.menu as menu

class Games:
    games = menu.games
    game_dict = menu.game_dict
    def __init__(self, game_id):
        self.game_id = game_id
    def player(self, player_name):
        return Player(player_name)
```


```python
Games.games
Games.game_dict
```




    {'g-1': 0, 'g-2': 1}




```python
games = Games("g-1")
```


```python
games.games
games.game_dict
```




    {'g-1': 0, 'g-2': 1}



# TBC


- `GameClient` class: 
  - User side (client side)
  - Handles user: 
    - Create `gameRoom` 
    - Join `gameRoom` 
    - Create

- `GameServer` class:

On user sider (client side):  
```
gameClient = GameClient()
```

On server side:
```
gameServer = GameServer()
```


```python
# Prisoner's Dilemma
player1 = Player("player1", ['C', 'D'])
player2 = Player("player2", ['C', 'D'])
payoffMatrix = {
    ('C', 'C'): (-1, -1),
    ('C', 'D'): (-3, 0),
    ('D', 'C'): (0, -3),
    ('D', 'D'): (-2, -2)
}

game = Game(player1, player2, payoffMatrix, name="Prisoner's Dilemma", save=True, game_id='g-faa1')

```


```python
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
    def save(self):
        self.games.append(self)
    @staticmethod
    def create_gameId():
        return create_gameId()

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

# a function to create a 4 digit random hex number
def create_gameId():
    return 'g-'+''.join(random.choices('0123456789abcdef', k=4))
```

## Prototyping interface


```python
# user create game room
game = GameClient.game(game_id="game_id", room_name = "room_name", player_name = "player_name") # get corresponding game instance

game.dashboard # get the game information

game.dashboard.game_id
game.dashboard.room.room_id
game.dashboard.room.room_name
game.dashboard.room.players # array of player_id
game.dashboard.player.player_id
game.dasgboard.player.player_name
game.dashboard.player.strategies

game.play()
game.payoff()

game.history # array of played history
game.history[0].round_number
game.history[0].played_strategies # array of played strategies
game.history[0].payoff

game.next_round()

```

### Property


```python
game.dashboard.game_id
game.dashboard.room.room_id
game.dashboard.room.room_name
game.dashboard.room.players # array of player_id
game.dashboard.player.player_id
game.dasgboard.player.player_name
game.dashboard.player.strategies
```


```python
class Dashboard:
    def __init__(self, game_id, room, player):
        self.game_id = game_id
        self.room = Room(room_id, room_name, players)
        self.player = player

class Room:
    def __init__(self, room_id, room_name, players):
        self.room_id = room_id
        self.room_name = room_name
        self.players = players

class Player:
    def __init__(self, player_id, player_name, strategies):
        self.player_id = player_id
        self.player_name = player_name
        self.strategies = strategies
```


```python
class Game:
    def __init__(self, game_id, room_name, player_name):
        self.game_id = game_id
        room = Room(room_id, room_name, players)
        self.dashboard = Dashboard()
        self.player_name = player_name
    @property
    def dashboard(self, game_id, room_name, player_name):
        return Game(game_id, room_name, player_name)
```


```python
room = {
    "game_id": "game_id",
    "room_id": "room_id",
    "name": "room_name",
    "players": []
}

game.info = {
    "game_id": "game_id",
    "room": room,
}
```


```python
# player 1 initiate a game instance of a specific game specified by game-id
game = GameCloud(game_id="game-id")
room = game.create_room("room-name")

# with game_id, its corresponding game structure is loaded
game.id
game.gameInfo.payoff_function
game.gameInfo.player_strategies 

# player 1 create a game room waiting for player 2
game.room[0].id
room.id
room.players
room.check_room() # check if two players are ready to play

# player 1 create a player
player1 = game.create_player("player-name")
## create property under the hood
player1.id # player id
player1.name # player name

player1.join_room(game_id="game-id", room_id="room-id")

game.room[0].players[0] # player 1 information

player1.play("strategy") 
player1.payoff() # check if the other player has played
player1.history
```


```python
# Service Account
```

# @property and @{property_name}.setter

```
    @temp.setter
    def temp(self, new_temp):
        self._temp_fahr = new_temp * 9 / 5 + 32
```

# Google Sheets API

  - [Google Sheets API](https://developers.google.com/sheets/api/quickstart/python)

## Quickstart

  - [Python quickstart](https://developers.google.com/sheets/api/quickstart/python)


```python
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
SAMPLE_RANGE_NAME = "Class Data!A2:E"


def main():
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return

    print("Name, Major:")
    for row in values:
      # Print columns A and E, which correspond to indices 0 and 4.
      print(f"{row[0]}, {row[4]}")
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()
```

    Name, Major:
    Alexandra, English
    Andrew, Math
    Anna, English
    Becky, Art
    Benjamin, English
    Carl, Art
    Carrie, English
    Dorothy, Math
    Dylan, Math
    Edward, English
    Ellen, Physics
    Fiona, Art
    John, Physics
    Jonathan, Math
    Joseph, English
    Josephine, Math
    Karen, English
    Kevin, Physics
    Lisa, Art
    Mary, Physics
    Maureen, Physics
    Nick, Art
    Olivia, Physics
    Pamela, Math
    Patrick, Art
    Robert, English
    Sean, Physics
    Stacy, Math
    Thomas, Art
    Will, Math


### REST resources

Python API mimics the REST resources using HTTP verb (the internet data exchange protocol). There are many tools that are developed to handle Google sheets. REST resources use web link to categorize those tools and access them. 

For example, 

  - [spreadsheets.get](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/get) To get the the basic information of a spreadsheet with a `{spreadsheetId}`, like its title, how many sheets it has, and each sheet names. The tool that can do the job is located at the web address `https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}`. The user manual documents its usage details under the section `spreadsheets.get` because Google calls it the `get` method of `spreadsheets` instance.
  - [spreadsheets.values.get](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get) To get the values of a range in a spreadsheet with a `{spreadsheetId}` and `{range}`, the tool that can do the job is located at the web address `https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values/{range}`. The user manual documents its usage details under the section `spreadsheets.values.get` because Google calls it the `get` method of `value` instance that serves as a composition property of `spreadsheet` instance.


So to use Python API you need to pay attention to the section title. 

  - For `spreadsheets.get`, you need to create a `spreadsheets` instance and call its `get` method.
  - For `spreadsheets.values.get`, you need to create a `spreadsheets` instance, under that instance you can create a `values` instance. Within `values` instance, there is the `get` method.


## Build Service Object



```python
from py.gamecloud.googlesheets import create_gsheet_service

service = create_gsheet_service(SCOPES = ["https://www.googleapis.com/auth/spreadsheets"])
```

- The first time you create a service object, there will be a Google login authorization process.  
- How much `service` object can do to your Google Sheets depends on the `scopes` you set.
- It will also create a `token.json` file in your working directory. This file is used to store your authorization information. You can delete it if you want to re-authorize your Google account.

## Choose scopes

Each REST resource has its own scopes requirement. You can find the scopes in the user manual of each REST resource. For example, 

- [Scopes of spreadsheets.get](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/get#authorization-scopes)  
- [Scopes of spreadsheets.values.get](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get#authorization-scopes)


## Create Instance of REST resource


```python
## spreadsheets instance
spreadsheets = service.spreadsheets()
## values instance
values = spreadsheets.values()
```

For `values` instance we can use the following chaining expression as well:


```python
values = service.spreadsheets().values()
```

## An Example

- Example spreadsheets: <https://docs.google.com/spreadsheets/d/1lFqtMo0jicu9JAkHgNisQnIlFQc1mJlJyCLnOuaGQX8/edit?usp=sharing>


```python
# get basic information of the spreadsheets
spreadsheets.get(spreadsheetId="1lFqtMo0jicu9JAkHgNisQnIlFQc1mJlJyCLnOuaGQX8").execute()
```


```python
# get the values of its "play!A1:E1" range
values.get(spreadsheetId="1lFqtMo0jicu9JAkHgNisQnIlFQc1mJlJyCLnOuaGQX8", range="play!A1:E1").execute()
```

# User interface prototyping


```python
gs = GSheetService()

gs.play_sheet # play_sheet instance to control play sheet
gs.game_room_sheet # game_room instance to control game_room sheet

# when a game room created
gs.game_room_sheet.register(game_room)

# when a player join a game room
gs.game_room_sheet.add_players(game_room, player_id)

# when a player play in a game room
gs.play_sheet.register(player_strategy)
gs.game_room_sheet.update_game_room_status(player_strategy)

# when a player create next round
gs.game_room_sheet.update_round(game_room, round_number)
```


```python
game_room = {
    "game_id": "g-1",
    "room_id": "r-1"
}
player_strategy = {
    "game room": game_room,
    "player_id": "p-1",
    "round_number": 2,
    "strategy": "C"
}

```

# Recap

- Inheritance: `Game` inherits from `Games` which inherits its class property `games_played` to track what games have been played, and its `new` method to create a new game, and its `switch` method to play a played game from `games_played`.




```python
from gamepy.games import Games
```


```python
# prisoner's dilemma
game, (player1, player2) = Games().new("g-1")
```


```python
player1.play("C")
player2.play("D")
game.payoff()
```


```python
# scissors paper rock
game, (player1, player2) = game.new("g-2")
```


```python
player1.play("S")
player2.play("R")
game.payoff()
```

- `__init__.py` to constrol package/subpackage imports through `__all__` and objects created in `__init__.py`.


```python
# objects created within gamepy/gamesheet/__init__.py
from gamepy.gamesheet import scopes, spreadsheets_id
# objects exported through __ALL__ definition
from gamepy.gamesheet import GameRoom

# You can combine above into one line as well
```

- `GameRoom` class to control the game-room sheet in Google spreadsheets. 


```python
game_room = GameRoom(scopes=scopes, spreadsheets_id=spreadsheets_id)
```


```python
game_room.register_game_room("g-1:r-14")
game_room.register_player1_name("g-1:r-14", "Alice")
game_room.register_player1_choice("g-1:r-14", "C")
```

## Exercise: GameRoom()
What should you do to make the following code valid?



```python
from gamepy.gamesheet import GameRoom

game_room = GameRoom() # no need to pass scopes and spreadsheets_id again
```

## Exercise: from gamepy import Games

What should you do to make the following code valid?


```python
from gamepy import Games
```

# `Gamesheet` subpackage

- `gamesheet.py` to control the game sheet in Google spreadsheets.
- `gameroom.py` to control the game-room sheet in Google spreadsheets.

## `gamesheet.py`

- `Service` class to initiate a Google sheets service object through `service._build_sheet_service` method.
- `Sheet` class inherits from `Service` to control a Google sheet with **name** from a spreadsheet with **spreadsheet_id** and **scopes** specified. 


```python
from gamepy.gamesheet.gamesheet import Service, Sheet, scopes, spreadsheets_id
```


```python
# initiate a Google sheet service object
service = Service(spreadsheets_id=spreadsheets_id, scopes=scopes)

# check serice property and methods
service._build_sheet_service()
```


```python

sheet_game_room = Sheet("game-room", spreadsheets_id=spreadsheets_id, scopes=scopes)
sheet_play = Sheet("play", spreadsheets_id=spreadsheets_id, scopes=scopes)
```


```python
# check property and method
sheet_game_room._get("B8:E12")

```


```python
sheet_game_room._update(8,[None, None, None, "Jack"])
```


```python
sheet_game_room._append(['g-2:r-7', 'g-2', 'r-7'])
```


```python
sheet_game_room.last_row
```

## Exercise Answers

- [answers](https://github.com/tpemartin/gamepy/commit/5c901ea3121bc376eedd3f85d3c21024088998c0)

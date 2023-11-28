# Recap

## Standalone Game

A standalone app that runs on single computer only. 


### Prisoner's Dilemma

||C|D|
|---|---|---|
|**C**|3,3|0,5|
|**D**|5,0|1,1|



```python
from gamepy.game import Game

# prisioner's dilemma
game = Game(
    ["Alice", "Bob"],
    [["C","D"],["C","D"]],
    {("C","C"):(3,3), ("C","D"):(0,5), 
     ("D","C"):(5,0), ("D","D"):(1,1)}
)
Alice, Bob = game.players
```


```python
Alice.play("C")
Bob.play("C")
game.payoff()
```

### Paper-Rock-Scissors

Paper-Scissor-Rock game can be expressed as the following normal form:

| | P | S | R |
| --- | --- | --- | --- |
| P | 0, 0 | -1, 1 | 1, -1 |
| S | 1, -1 | 0, 0 | -1, 1 |
| R | -1, 1 | 1, -1 | 0, 0 |



```python
game2 = Game(
    ["Alice", "Bob"],
    [["P","S","R"],["P","S","R"]],
    {("P","P"):(0,0), ("P","S"):(-1,1), ("P","R"):(1,-1),
     ("S","P"):(1,-1), ("S","S"):(0,0), ("S","R"):(-1,1),
     ("R","P"):(-1,1), ("R","S"):(1,-1), ("R","R"):(0,0)}
)
Alice2, Bob2 = game2.players
```


```python
Alice2.play("P")
Bob2.play("S")
game2.payoff()
```

## Games class

A class that contains all the games that we want to play. 

  


```python
from gamepy.gamemenu.menu import menus

class Games:
    menus = menus
    def __init__(self):
        pass
    

```

> `menus` is a variable created within the `menu.py` module. No only functions and classes can be imported, but also variables.

# Class properties

## Access the class properties

`menus` is a class property. It can be accessed:


```python
# throuth the class constructor
Games.menus

# through an instance of the class
games = Games()
games.menus

# through the __class__ attribute of an instance
games.__class__.menus
```

- If there is an instance property also called `menus`, the instance property will be used.


```python
class Games:
    menus = menus
    def __init__(self):
        self.menus = "instance menus"
    
```


```python
games = Games()

games.menus, Games.menus
```

## Difference between class property and instance property

- Class property is shared by all instances of the class.
- Instance property is unique to each instance of the class.


```python
class Games:
    menus = menus
    def __init__(self, name):
        self.name = name
    

```


```python
games1 = Games("g1")
games2 = Games("g2")
```


```python
games1.name, games2.name
```


```python
games1.menus, games2.menus
```

> When you need different instances to share the same information, use class property. When you need each instance to have its own information, use instance property.



# Exercise 

Given the Game class that we have created in the lecture that can create a prisoner's dilemma game as:


```python
from gamepy.game import Game

# prisioner's dilemma
game = Game(
    ["player1", "player2"],
    [["C","D"],["C","D"]],
    {("C","C"):(3,3), ("C","D"):(0,5), 
     ("D","C"):(5,0), ("D","D"):(1,1)}
)
Alice, Bob = game.players

game2 = Game(
    ["player1", "player2"],
    [["P","S","R"],["P","S","R"]],
    {("P","P"):(0,0), ("P","S"):(-1,1), ("P","R"):(1,-1),
     ("S","P"):(1,-1), ("S","S"):(0,0), ("S","R"):(-1,1),
     ("R","P"):(-1,1), ("R","S"):(1,-1), ("R","R"):(0,0)}
)
Alice2, Bob2 = game2.players
```

Consider the following Games class prototype:



```python
from gamepy.game import Game
from gamepy.gamemenu.menu import menus

# a prototype
class Games:
    menus = menus
    def __init__(self):
        pass
```

 Develop `Games` further to accommodate the following user interface requirements:


```python
games = Games()
game = games.new('g-1')
Alice, Bob = game.players

game2 = games.new('g-2')
Alice2, Bob2 = game2.players
```

That is to design a `new` method that cann create a `game` instance from `Game` class based in `game_id`.

## @property

`@property` is a decorator that allows us to define a method that can be accessed **AS A PROPERTY**.



```python
games = Games()

```


```python
games.menus['g-1']['name'], games.menus['g-2']['name']
```


```python
# dictionary comprehension
{k: v['name'] for k, v in games.menus.items()}
```


```python
class Games:
    menus = menus
    def __init__(self):
        pass
    @property
    def short_menus(self):
        return {k: v['name'] for k, v in self.menus.items()}
```


```python
games = Games()
games.short_menus
```

# TBC


```python
# GameCient

gc = GameClient()
game = gc.game(game_id="game-1")
room = game.room()
player = game.player(name = "player-1")
player.join(room)
```


```python
class Player:
    def __init__(self, name):
        self.name = name
        self.player_id  = player_id()
    def join(self, room):
        room.register_player(self)
    
class Room:
    def __init__(self, room_id=None):
        self.roomd_id = room_id if room_id else room_id()
        # register in game-room-id, game-id column in sheet game-room
        self.sheet_row = register_room(self) 
        self.players = []
    def register_player(self, player):
        self.players.append(player)

class Game:
    def __init__(self, game_id=None):
        self.game_id = game_id if game_id else game_id()
        self.room = None
    def room(self, room_id=None):
        room = Room(room_id)
        self.rooms.append(room)
        return room
        
# helpers
def register_room(room):
    sheet_row = None
    return sheet_row

def register_player(player):
    pass    

```


```python
player = Player("player-1")
player.name
player.player_id
```


```python
import string
import random

# > Function that creates random id from hex characters
def random_id(prefix, len=4):
    return prefix + '-'+''.join(random.choice(string.digits+string.ascii_lowercase) for _ in range(len))
```


```python
random_id('g')
```


```python
def game_id():
    return random_id('g')
def room_id():
    return random_id('r')
def player_id():
    return random_id('p')
```

# Inheritance

Sometimes classes have parent (super class) and children (sub classes) relationship. The children inherit the attributes and methods of the parent. If you want the sub classes to have all the properties and methods of the parent class, you can use inheritance.


```python
class Differentiable:
    type = "Differentiable"
    def __init__(self, value):
        self.value = value
    def derivative(self, x):
        pass
    
class LogLinear:
    sub_type = "LogLinear"
    def __init__(self, parameters):
        self.parameters = parameters
  
```

All differentiable function can have derivative computed. Loglinear is class of differentiable functions. We can use inheritance to let `LogLinear` class inherit the `derivative` instance method from `Differentiable` class.



```python
class Differentiable:
    type = ["Differentiable"]
    def __init__(self, value):
        self.value = value
    def derivative(self, x):
        pass
    @classmethod
    def change_type(cls, new_type):
        cls.type = new_type
    
class LogLinear(Differentiable):
    sub_type = ["LogLinear"]
    def __init__(self, parameters, value):
        super().__init__(value)
        self.parameters = parameters
    
```

- sub class `__init__` also inherit super class `__init__` input argument `value`.  
- `super().__init__(...)` is used to call the super class `__init__` method.


```python
ll = LogLinear(1, 2)
```


```python
ll.__class__.type, ll.__class__.sub_type, ll.derivative(1)
```

> If the super class property is **mutable**, then modify the sub class same property will change its super class counterpart as well.


```python
# modify the inherited class property
#   also modifies the parent class property
ll.type.append("Continuous")
ll.type
```


```python
Differentiable.type
```

## Games class

`Games` class encapsulates the menu of available games, and the method to start a new game, the history of game played will be tracked underneath. 

`Game` class is to initialize a game, and to play the game. 

When playing a game of `Game` class, users might want to play another game. If we let `Game` class inherit `Games` class, `Game` class will have the method to start a new game -- no need to use `Games` class to start a new game.
 

- `Games` a super class
- `Game` a sub class




```python
# Demo: Do not run

# No inheritance
games = Games()
game = games.new('g-1')
Alice, Bob = game.players

## To play another game, we use games again
game2 = games.new('g-2') # use games

```


```python

# With inheritance
### new game can be initialized with the current game instance
game2 = game.new('g-2') # use game not games

```

### Details


```python
from gamepy.games import Games
```

`Games` in `games.py`:
  
https://github.com/tpemartin/gamepy/blob/681ba5c2b4ff7ffc7eba3f724ab212634c2e388f/games.py#L11_L37

  - All class method must have `@classmethod` decorator.
  - class property `games_played` is a dictionary which is mutable.


### Usage


```python
# The first time to initiate a new game

game, (player1, player2) = Games().new("g-1") 
# Or
# games = Games()
# game = games.new("g-1")

# Afterward, can use `game` to initiate a different new game
# Game class inherits `new` instance method from Games class
game2, (player1, player2) = game.new("g-2")

# a new g-1
game3, (player1, _ ) = game.new("g-1")
# if you don't need player2, use meaningless holder `_`
```

- `Games.new` will return `game` and `players` (a list of two player instances)
- The above code uses unpacking skill.


```python
a = [1, (2, 3)]
a1, other = a
a1, _ = a

```


```python

b = [1, (2, 3), 5]
b1, *other = b # `*` force `other` to take in all the rest
other
```


```python
b1, b2, b3 = b
b2

b1, (c1, c2), b3 = b
c1, c2

```

The instances of the sub class `Game` all inherit properties and methods from super class `Games`.

Instance properties and methods continue to be the instance properties and methods in the sub class (`Game` here), and class properties and methods continue to be the class properties and methods in the sub class (`Game` here).


```python
# All sub class have inherited super class methods and properties
game.new
game.new2 # class method
game.switch
game.switch2 # class method
game.games_played # class property

game2.new
game2.new2
game2.switch
game2.switch2
game.games_played
```

### Modify super class property though subclass

If the super class property is **mutable** and there is method that can change it under the hood. When sub class instance call the method, the super class property will be changed as well -- as long as it is mutable.


```python
# current super class property
Games.games_played
```


```python
# sub class method (inherited) call
game.new('g-2')
game.new('g-2')

# check super class property
Games.games_played
```

> Even the super class `Games` remembers the played game created by its subclasses `game`. The `games_played` class property is in sync between `Games` and its subclasses.

- Inheritance can create a feedback loop from the subclass back to the super class as long as the property value is *mutable*.

### Two types of game play

new game (`game.new()`) vs. returning game (`game.switch()`)


```python
# return to g-2
game, (Alice, Bob) = game.switch('g-2')
Alice.play("S"), Bob.play("R")
Alice.played_strategy, Bob.played_strategy, game.payoff()
```

You can switch through class method `Games.switch2`. Also create new game through `Games.new2`.


```python
game, (Alice, Bob) = Games.switch2('g-1')
game, (Alice, Bob) = Games.new2('g-2')
```

For a game that has multiple instances (like same game played in different rooms), we can `switch` to the specific instance using its index in `game.games_played['game_id'][index]`


```python
# return to first g-1
game, (Alice, Bob) = game.switch('g-1')
Alice.play("C"), Bob.play("D")
Alice.played_strategy, Bob.played_strategy, game.payoff()
```


```python
# return to second g-1
game, (Alice, Bob) = game.switch('g-1',index=1)
Alice.play("D"), Bob.play("D")
Alice.played_strategy, Bob.played_strategy, game.payoff()
```


```python
# check 1st g-1 played_strategy
[p.played_strategy 
    for p in game.games_played['g-1'][0].players]
```


```python
# check 2nd g-1 played_strategy
[p.played_strategy 
    for p in game.games_played['g-1'][1].players]
```

# Exercise: Game Room


Given the following setup of `GameRoom`


```python
from gamepy.gamesheet.gamesheet import spreadsheets_id, scopes
from gamepy.gamesheet.gameroom import GameRoom
game_room = GameRoom(spreadsheets_id, scopes)
```


```python
game_room.register_game_room("g-1:r-1")
game_room.register_player1_name("g-1:r-1", "Alice")
game_room.register_player2_name("g-1:r-1", "Bob")
game_room.register_player1_choice("g-1:r-1", "C")
game_room.register_player2_choice("g-1:r-1", "D")

```

Modify `Game` class and ``


```python
game.create_room(room_id = "r-1")
player1.join_room(room_id = "r-1")
```


```python
game, (player1, player2) = Games().new("g-1")
game.create_room(room_id = "r-1") 
# register game room under game_room_id "g-1:r-1"

player1.join_room(room_id = "r-1")
# register player1 name under game_room_id "g-1:r-1"
player2.join_room(room_id = "r-1")
# register player2 name under game_room_id "g-1:r-1"

player1.play("C")
# register player1 choice under game_room_id "g-1:r-1"
player2.play("D")
# register player2 choice under game_room_id "g-1:r-1"

```

#### Define Package * import

Instead of using `from gamepy.gamesheet.gamesheet import *` where the last `gamesheet` is the module name, we can use `from gamepy.gamesheet import *` if we have `__ALL__` defined what to export in `__init__.py`.


In `__init__.py`
```python
# package attributes used in `test` must 
#  go above the `test` import
from .gamesheet import test

__ALL__ = ['test']
```

> Note: package attributes, like `scopes` used in `test` must go above the `test` import.


```python
# import from package (not from module)
from gamepy.gamesheet import test, scopes
```


```python
test()
```

Import `spreadsheet_id` from package is not allowed since it is not defined in `__ALL__`.


```python
# can not import spreadsheet_id from package,
# since it is not in __ALL__
from gamepy.gamesheet import spreadsheets_id
```

However, if you import `spreadsheet_id` from `gamesheet.py`, it is allowed.

> `__init__.py` only control export in `from {package}` level. It does not control export in `from {package}.{module}` level.


```python
# Can still import from module level though
from gamepy.gamesheet.gamesheet import spreadsheets_id
```

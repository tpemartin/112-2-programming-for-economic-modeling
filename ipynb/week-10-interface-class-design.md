# Game Object

In Game Theory, a game can be presented in two forms: normal form and extensive form. Normal form is a matrix, while extensive form is a tree. In this class, we will focus on normal form games.

Here we only focus on 

  - 2 players game
  - Its payoff matrix (i.e. its normal form) can be presented as a 2 dimensional matrix
    - Each player has a finite number of pure strategies

## Prisoner's Dilemma 

An example is

  - 2 players: Alice (row player) and Bob (column player)
  - Each player has 2 pure strategies: cooperate (C) and defect (D)
  - The payoff matrix is
  
  | | C | D |
  | --- | --- | --- |
  | C | -1, -1 | -3, 0 |
  | D | 0, -3 | -2, -2 |
  


```python
alice = Player("Alice", ['C', 'D'])
bob = Player("Bob", ['C', 'D'])
payoffMatrix = {
    ('C', 'C'): (-1, -1),
    ('C', 'D'): (-3, 0),
    ('D', 'C'): (0, -3),
    ('D', 'D'): (-2, -2)
}
def payoff_func(strategies: tuple[str, str]) -> tuple[float, float]:
    return payoffMatrix[strategies]
```


```python
alice.name
alice.strategies # show pure strategies of Alice
alice.played_strategy # show played strategy of Alice, None by default
alice.play('C')
alice.played_strategy # show 'C'
```




    'C'



### Player class

#### A prototype


```python
# Start from a prototype of only properties

class Player:
    def __init__(self, name: str, strategies: list[str]):
        self.name = name
        self.strategies = strategies
        self.played_strategy = None
    def play(self, played_strategy):
        pass

```

#### Design play method helper


```python
player = Player("Alice", ['C', 'D'])
```


```python
# play method has one input, called played_strategy for example
played_strategy = "C"

# we want the following to happen
## Anything you want to happen under the hood
player.played_strategy = played_strategy

```

> Wrap up above to a `play_method` helper function with first input `player`, and `played_strategy` as the second input.


```python
def play_method(play, played_strategy):
    play.played_strategy = played_strategy
```

#### Attach helper to the class


```python
class Player:
    def __init__(self, name: str, strategies: list[str]):
        self.name = name
        self.strategies = strategies
        self.played_strategy = None
    def play(self, played_strategy):
        play_method(self, played_strategy)

# helper functions
def play_method(play, played_strategy):
    play.played_strategy = played_strategy
```

### Game class


```python
game = Game(alice, bob, payoff_func)
```


```python
game.payoff_function # show payoff_function
game.players # show [alice, bob]

# method payoff
## after
alice.play('C')
bob.play('D')
## we can compute payoff
game.payoff() # show 
```




    (-3, 0)



#### A prototype


```python
class Game:
    def __init__(self, player1, player2, payoff_function):
        self.players = [player1, player2]
        self.payoff_function = payoff_function
    def payoff(self):
        pass
```


```python
game = Game(alice, bob, payoff_func)
```

#### Design payoff helper


```python
## after
alice.play('C')
bob.play('D')

## compute payoff
strategies = game.players[0].played_strategy, game.players[1].played_strategy
game.payoff_function(strategies)
```




    (-3, 0)




```python
# helper function
def payoff(game):
    strategies = game.players[0].played_strategy, game.players[1].played_strategy
    return game.payoff_function(strategies)

```

#### Attach helper to the class


```python
class Game:
    def __init__(self, player1, player2, payoff_function):
        self.players = [player1, player2]
        self.payoff_function = payoff_function
    def payoff(self):
        payoff(self)

# helper function
def payoff(game):
    strategies = game.players[0].played_strategy, game.players[1].played_strategy
    return game.payoff_function(strategies)

```

## Complete Game class

### Beta version


```python
class Player:
    def __init__(self, name: str, strategies: list[str]):
        self.name = name
        self.strategies = strategies
        self.played_strategy = None
    def play(self, played_strategy):
        play_method(self, played_strategy)

class Game:
    def __init__(self, player1, player2, payoff_function):
        self.players = [player1, player2]
        self.payoff_function = payoff_function
    def payoff(self):
        payoff(self)

# helper function
def payoff(game):
    strategies = game.players[0].played_strategy, game.players[1].played_strategy
    return game.payoff_function(strategies)

def play_method(play, played_strategy):
    play.played_strategy = played_strategy
```

### Validate Played Strategy


```python
player = Player("Alice", ['C', 'D'])

```


```python
played_strategy = "M"

if played_strategy not in player.strategies:
    raise ValueError("Invalid strategy")
else:
    player.played_strategy = played_strategy



```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /Users/martin/Documents/GitHub/112-2-programming-for-economic-modeling/ipynb/week-10-class-property-method.ipynb Cell 31 line 4
          <a href='vscode-notebook-cell:/Users/martin/Documents/GitHub/112-2-programming-for-economic-modeling/ipynb/week-10-class-property-method.ipynb#Y106sZmlsZQ%3D%3D?line=0'>1</a> played_strategy = "M"
          <a href='vscode-notebook-cell:/Users/martin/Documents/GitHub/112-2-programming-for-economic-modeling/ipynb/week-10-class-property-method.ipynb#Y106sZmlsZQ%3D%3D?line=2'>3</a> if played_strategy not in player.strategies:
    ----> <a href='vscode-notebook-cell:/Users/martin/Documents/GitHub/112-2-programming-for-economic-modeling/ipynb/week-10-class-property-method.ipynb#Y106sZmlsZQ%3D%3D?line=3'>4</a>     raise ValueError("Invalid strategy")
          <a href='vscode-notebook-cell:/Users/martin/Documents/GitHub/112-2-programming-for-economic-modeling/ipynb/week-10-class-property-method.ipynb#Y106sZmlsZQ%3D%3D?line=4'>5</a> else:
          <a href='vscode-notebook-cell:/Users/martin/Documents/GitHub/112-2-programming-for-economic-modeling/ipynb/week-10-class-property-method.ipynb#Y106sZmlsZQ%3D%3D?line=5'>6</a>     player.played_strategy = played_strategy


    ValueError: Invalid strategy



```python
def play_method(player, played_strategy):
    if played_strategy not in player.strategies:
        raise ValueError("Invalid strategy")
    else:
        player.played_strategy = played_strategy

```

#### Raise an exception

When function bounds to fail, we want it to break as soon as possible and given an usefull error message. This can be done in Python through raising an exception. For example, the following function raises an exception when the input value caused the problem.

```python
raised  {typeOfError}("message")
```

There are several exceptions in Python. The following are the most common ones.

| Exception | Description |
| --- | --- |
| `TypeError` | Raised when an operation or function is applied to an object of inappropriate type. |
| `NameError` | Raised when a local or global name is not found. |
| `ZeroDivisionError` | Raised when the second operand of division or modulo operation is zero. |
| `IndexError` | Raised when a sequence index is out of range. |
| `KeyError` | Raised when a key is not found in a dictionary. |
| `ValueError` | Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified. |
| `AttributeError` | Raised when an attribute reference or assignment fails. |


### Validate Both played


```python
game = Game(alice, bob, payoff_func)
```


```python
def payoff(game):
    played_strategies = game.players[0].played_strategy, game.players[1].played_strategy
    if all(played_strategies):
        # if both players have played their strategies
        return game.payoff_function(played_strategies)
    else:
        print("Not all players have played their strategies yet.")

```

### Upgrade version


```python
class Player:
    def __init__(self, name: str, strategies: list[str]):
        self.name = name
        self.strategies = strategies
        self.played_strategy = None
    def play(self, played_strategy):
        play_method(self, played_strategy)

class Game:
    def __init__(self, player1, player2, payoff_function):
        self.players = [player1, player2]
        self.payoff_function = payoff_function
    def payoff(self):
        payoff(self)

# helper function
def payoff(game):
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

```

# Exercise Another Game User Interface

  | | C | D |
  | --- | --- | --- |
  | C | -1, -1 | -3, 0 |
  | D | 0, -3 | -2, -2 |


```python
payoffMatrix1 = [[-1, -3],[0, -2]]
payoffMatrix2 = [[-1, 0],[-3, -2]]

player1 = Player("Alice", ['C', 'D'])
player2 = Player("Bob", ['C', 'D'])

game = Game([player1, player2], [payoffMatrix1, payoffMatrix2])
```


```python
player1.play('C')
player2.play('D')
game.payoff()
```


```python
player1 = Player("player1", ['P', 'S', 'R'])
player2 = Player("player2", ['P', 'S', 'R'])
payoffMatrix = {
    ('P', 'P'): (0, 0),
    ('P', 'S'): (-1, 1),
    ('P', 'R'): (1, -1),
    ('S', 'P'): (1, -1),
    ('S', 'S'): (0, 0),
    ('S', 'R'): (-1, 1),
    ('R', 'P'): (-1, 1),
    ('R', 'S'): (1, -1),
    ('R', 'R'): (0, 0)
}
def payoff_func(strategies: tuple[str, str]) -> tuple[float, float]:
    return payoffMatrix[strategies]

game_paper_scissor_rock = Game(player1, player2, payoff_func, name="Paper Scissor Rock")
```

# Class Property and Method

Suppose you want to save all the game instances that you created for different game. You can use a class property to do so.


```python
# ideal interface
# Prisoner's Dilemma
player1 = Player("player1", ['C', 'D'])
player2 = Player("player2", ['C', 'D'])
payoffMatrix = {
    ('C', 'C'): (-1, -1),
    ('C', 'D'): (-3, 0),
    ('D', 'C'): (0, -3),
    ('D', 'D'): (-2, -2)
}
def payoff_func(strategies: tuple[str, str]) -> tuple[float, float]:
    return payoffMatrix[strategies]

game = Game(player1, player2, payoff_func, name="Prisoner's Dilemma", save=True)

# paper scissor rock
player1 = Player("player1", ['P', 'S', 'R'])
player2 = Player("player2", ['P', 'S', 'R'])
payoffMatrix = {
    ('P', 'P'): (0, 0),
    ('P', 'S'): (-1, 1),
    ('P', 'R'): (1, -1),
    ('S', 'P'): (1, -1),
    ('S', 'S'): (0, 0),
    ('S', 'R'): (-1, 1),
    ('R', 'P'): (-1, 1),
    ('R', 'S'): (1, -1),
    ('R', 'R'): (0, 0)
}
def payoff_func(strategies: tuple[str, str]) -> tuple[float, float]:
    return payoffMatrix[strategies]

game_paper_scissor_rock = Game(player1, player2, payoff_func, name="Paper Scissor Rock", save=True)
```

- Game init add `save` option, when `True`. The saved game can be seen in `Game.games`.


```python
Game.games # show all saved games
game = Game.create_from_template("game_id") # create a game instance using game[0] structure
```


```python
from py.game_week11 import Game, Player

# ideal interface
# Prisoner's Dilemma
player1 = Player("player1", ['C', 'D'])
player2 = Player("player2", ['C', 'D'])

def payoff_func(strategies: tuple[str, str]) -> tuple[float, float]:
    payoffMatrix = {
        ('C', 'C'): (-1, -1),
        ('C', 'D'): (-3, 0),
        ('D', 'C'): (0, -3),
        ('D', 'D'): (-2, -2)
    }
    return payoffMatrix[strategies]

game = Game(player1, player2, payoff_func, name="Prisoner's Dilemma", save=True, game_id='g-faa1')

# paper scissor rock
player1 = Player("player1", ['P', 'S', 'R'])
player2 = Player("player2", ['P', 'S', 'R'])

def payoff_func(strategies: tuple[str, str]) -> tuple[float, float]:
    payoffMatrix = {
        ('P', 'P'): (0, 0),
        ('P', 'S'): (-1, 1),
        ('P', 'R'): (1, -1),
        ('S', 'P'): (1, -1),
        ('S', 'S'): (0, 0),
        ('S', 'R'): (-1, 1),
        ('R', 'P'): (-1, 1),
        ('R', 'S'): (1, -1),
        ('R', 'R'): (0, 0)
    }
    return payoffMatrix[strategies]

game_paper_scissor_rock = Game(player1, player2, payoff_func, name="Paper Scissor Rock", save=True, game_id='g-42b7')
```


```python
game_paper_scissor_rock.__class__.games # show all saved games
```


```python
Game.games

```


```python
(game, player1, player2) = Game.create_from_template('g-faa1')

```

game.name
player1.play("C")
player2.play("D")
game.payoff()


```python
class Temperature:
    def __init__(self):
        self._temp_fahr = 0
    @property
    def temp(self):
        return (self._temp_fahr - 32) * 5 / 9
    @temp.setter
    def temp(self, new_temp):
        self._temp_fahr = new_temp * 9 / 5 + 32

```


```python
t = Temperature()
```


```python
t.temp

```




    -17.77777777777778




```python
t.temp = 100
t._temp_fahr,t.temp
```




    (212.0, 100.0)



> Be aware `game.games` will also give you the result as `Game.games` This is because Python has a scoping rule saying that if an instance property is not found, it will look for a class property with the same name.

### Mixed strategy

#### How to draw a strategy


```python
import numpy as np

chosen_strategy = np.random.choice(alice.strategies, p=[0.35, 0.65])
chosen_strategy
```




    'C'



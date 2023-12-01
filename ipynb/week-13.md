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




    (['Differentiable'], ['LogLinear'], None)



> If the super class property is **mutable**, then modify the sub class same property will change its super class counterpart as well.


```python
# modify the inherited class property
#   also modifies the parent class property
ll.type.append("Continuous")
ll.type
```




    ['Differentiable', 'Continuous']




```python
Differentiable.type
```




    ['Differentiable', 'Continuous']



## Games class


```python
from gamepy.games import Games
```

Games in games.py:
  
https://github.com/tpemartin/gamepy/blob/681ba5c2b4ff7ffc7eba3f724ab212634c2e388f/games.py#L11-L37




```python
game = Games().new("g-1") 
# Or
# games = Games()
# game = games.new("g-1")

# Game class inherits `new` instance method from Games class
game2 = game.new("g-2")

# a new g-1
game3 = game.new("g-1")
```

The instances of the sub class `Game` all inherit properties and methods from super class `Games`.

Instance properties and methods continue to be the instance properties and methods in the sub class (`Game` here), and class properties and methods continue to be the class properties and methods in the sub class (`Game` here).


```python
# All sub class have inherited super class methods and properties
game.new
game.new2
game.switch
game.switch2
game.games_played

game2.new
game2.new2
game2.switch
game2.switch2
game.games_played
```




    {'g-1': [<gamepy.games.Game at 0x11b9cb210>,
      <gamepy.games.Game at 0x11b9cb3d0>,
      <gamepy.games.Game at 0x11b9da090>,
      <gamepy.games.Game at 0x11c034490>],
     'g-2': [<gamepy.games.Game at 0x11b9cb350>,
      <gamepy.games.Game at 0x11bfb85d0>]}




```python
Games.games_played
```




    {'g-1': [<gamepy.games.Game at 0x11b9cb210>,
      <gamepy.games.Game at 0x11b9cb3d0>,
      <gamepy.games.Game at 0x11b9da090>,
      <gamepy.games.Game at 0x11c034490>],
     'g-2': [<gamepy.games.Game at 0x11b9cb350>,
      <gamepy.games.Game at 0x11bfb85d0>]}



> Even the super class `Games` remembers the played game created by its subclasses `game`. The `games_played` class property is in sync between `Games` and its subclasses.

- Inheritance can create a feedback loop from the subclass back to the super class as long as the property value is *mutable*.


```python
# return to g-2
game = game.switch('g-2')
Alice, Bob = game.players
Alice.play("S"), Bob.play("R")
Alice.played_strategy, Bob.played_strategy, game.payoff()
```




    ('S', 'R', (-1, 1))




```python
# return to first g-1
game = game.switch('g-1')
Alice, Bob = game.players
Alice.play("C"), Bob.play("D")
Alice.played_strategy, Bob.played_strategy, game.payoff()
```




    ('C', 'D', (-3, 0))




```python
# check 1st g-1 played_strategy
[p.played_strategy 
    for p in game.games_played['g-1'][0].players]
```




    ['C', 'D']




```python
# return to second g-1
game = game.switch('g-1',index=1)
Alice, Bob = game.players
Alice.play("D"), Bob.play("D")
Alice.played_strategy, Bob.played_strategy, game.payoff()
```




    ('D', 'D', (-2, -2))




```python
# check 2nd g-1 played_strategy
[p.played_strategy 
    for p in game.games_played['g-1'][1].players]
```




    ['D', 'D']




```python
game = Games().new('g-1')
Alice, Bob = game.players
Alice.play('C')
Bob.play("D")
Alice.played_strategy, Bob.played_strategy
```




    ('C', 'D')




```python
game = Games().new('g-2')
Alice, Bob = game.players
Alice.play('R')
Bob.play("S")
Alice.played_strategy, Bob.played_strategy
```




    ('R', 'S')



Reuse the old 'g-1' game


```python
game = game.games_played['g-1']
Alice, Bob = game.players
Alice.played_strategy, Bob.played_strategy
```




    ('C', 'D')




```python
game = Games.games_played['g-1']
Alice, Bob = game.players
Alice.played_strategy, Bob.played_strategy
```




    ('C', 'D')



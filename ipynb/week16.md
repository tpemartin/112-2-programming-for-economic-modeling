# Nashpy

To use the `nashpy` package in Python, you'll need to follow these steps:

1. Install the `nashpy` package using pip by running the following command in your terminal or command prompt:
   ```
   pip install nashpy
   ```

2. Import the necessary modules in your Python script:
   



```python
import numpy as np
import nashpy as nash
```


4. Define the payoff matrices for the game you want to analyze. Payoff matrices represent the rewards or utilities for each player based on their strategies.

5. Create a `Game` object by passing the payoff matrices as numpy arrays:
   


```python
payoff_matrix_player1 = np.array([[1, 0], [0, 1]])
payoff_matrix_player2 = np.array([[0, 1], [1, 0]])

nashpyGame = nash.Game(payoff_matrix_player1, payoff_matrix_player2)
```


6. Analyze the game using various methods provided by the `Game` object. For example, you can compute the Nash equilibria:
   


```python
equilibria = nashpyGame.support_enumeration()

for eq in equilibria:
    print("Nash Equilibrium:")
    print(f"Player 1: {eq[0]}")
    print(f"Player 2: {eq[1]}")
```


   You can also perform other analyses such as finding the best response strategies or computing utilities for specific strategies.

Remember to replace the payoff matrices with the ones relevant to your game. The `nashpy` package provides additional functionalities for game theory analysis, so you can explore its documentation for more advanced usage.

# gamepy application


```python
from gamepy.games import Games
```


```python
game, (player1, player2) = Games().new('g-1')
```


```python
game.create_room('r-221')
```


```python
player1.join("r-221")
player2.join("r-221")
```


```python
player1.play("C")
player2.play("C")
```


```python
player1.payoff()
```


```python
player1.play_mixed({"C": 0.5, "D": 0.5})
player2.play_mixed({"C": 0.3, "D": 0.7})

```


```python
player1.payoff()
```

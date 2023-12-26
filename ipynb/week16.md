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

# Package

## Steps

1. Run `python setup.py sdist bdist_wheel` to build the package.
2. Commit in Github desktop and add a version tag.
3. In Github.com create new release.

## installation

1. Go to the terminal of your current environment.
2. `pip install git+https://github.com/tpemartin/gamepy.git@<tag>` where `<tag>` is the version tag you created.
3. Reload your vscode window.

> Make sure your local path specification does not point to the local version of the package.

## External file

> How to include a credentials.json to a pip github installable package and use that file in a package module?

### ChatGPT answer

To include a `credentials.json` file in a pip-installable package and use it within a package module, you can follow these steps:

1. Create a directory structure for your package. For example:
   ```
   mypackage/
   ├── mypackage/
   │   ├── __init__.py
   │   └── mymodule.py
   ├── credentials.json
   ├── setup.py
   └── README.md
   ```

2. Place your `credentials.json` file in the root directory of your package.

3. In your `setup.py` file, include the `data_files` parameter to specify that `credentials.json` should be included in the package distribution:

   ```python
   from setuptools import setup

   setup(
       name='mypackage',
       version='1.0',
       packages=['mypackage'],
       package_data={'mypackage': ['../credentials.json']},
       include_package_data=True,
       install_requires=[
           'requests',
       ],
   )
   ```

4. In your package module (`mymodule.py`), you can access the `credentials.json` file using its relative path:

   ```python
   import os
   import json

   def load_credentials():
       credentials_path = os.path.join(os.path.dirname(__file__), '../credentials.json')
       with open(credentials_path) as f:
           credentials = json.load(f)
       return credentials
   ```

   The `os.path.join` function is used to construct the correct path to `credentials.json` relative to your module file.

5. Build and install your package using `pip` or `python setup.py install`. This will include the `credentials.json` file in the package distribution.

When using the installed package, you can import the `mymodule` and call the `load_credentials()` function to load the contents of `credentials.json`.

Please note that including sensitive credentials in a package may pose security risks, especially if the package is distributed publicly. It's generally recommended to use environment variables or other secure methods for storing and accessing credentials.


```python

```

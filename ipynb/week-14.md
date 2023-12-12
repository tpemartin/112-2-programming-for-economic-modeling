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

# pip installable

To create a GitHub pip installable package, you can follow these steps:

1. Create a new repository on GitHub: Go to GitHub (https://github.com/) and create a new repository to host your package.

2. Organize your code: Make sure your code is well-structured and organized in a directory. This directory will be the root of your package.

3. Create a setup.py file: In the root directory of your package, create a file named `setup.py`. This file contains information about your package, such as its name, version, dependencies, and entry points. 

```
from setuptools import setup

setup(
    name='your_package_name',
    version='1.0.0',
    description='Description of your package',
    author='Your Name',
    packages=find_packages(),
    install_requires=['dependency1', 'dependency2'],
)

```

4. Commit your code to the GitHub repository: Initialize a Git repository in your package directory, add your code files, and commit them to the repository.

5. Push the repository to GitHub: Push the Git repository to the remote GitHub repository you created in step 1.

6. Create a release on GitHub: Go to your GitHub repository, navigate to the "Releases" tab, and create a new release. Specify a tag version for the release (e.g., "v1.0.0") and provide a release title and description.

> Next step, you need to do `pip install wheel` first.

7. Upload your package distribution files: Before you upload your package distribution files, you need to build them. Open a terminal or command prompt, navigate to the root directory of your package, and run the following command to build the package:

```
python setup.py sdist bdist_wheel
```

This command creates a `dist` directory containing the distribution files for your package.

Next, in the release creation page on GitHub, click on "Upload assets" and select the distribution files (`*.tar.gz` and `*.whl`) from the `dist` directory.

8. Publish the release: Once you've uploaded the distribution files, click on "Publish release" to make the release and the package files available to users.

Now, users can install your package directly from GitHub using pip by running:
```
pip install git+https://github.com/username/repo.git@tag
```

for example,

```
pip install git+https://github.com/tpemartin/gamepy.git@v1.0.4
```

Replace `username` with your GitHub username, `repo` with the name of your repository, and `tag` with the tag version you provided in step 6.

That's it! Your GitHub pip installable package is ready. Users can install it using pip by referencing your GitHub repository.



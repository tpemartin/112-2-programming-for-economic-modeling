# Package



```python
from gamepy.games import Games
```


```python
game, (player1, _) = Games().new("g-2")
```


```python
# create a room
game.create_room("r-26")
```


```python
player1.name="Alice"
player1.join("r-26")
```


```python
player1.play("P")
```


```python
game2, (_, player2) = Games().new("g-1")
```


```python
player2.name="Jenkins"
player2.join("r-26")
```


```python
player2.play("D")
```

# Read Strategies Played


```python
player1.payoff()
```


```python
player2.payoff()
```


```python
player = player1
```

# Exercise: warning when room full

# pip installable

> Every package/subpackage needs a `__init__.py` file.

To create a GitHub pip installable package, you can follow these steps:

1. Create a new repository on GitHub: Go to GitHub (https://github.com/) and create a new repository to host your package.

2. Organize your code: Make sure your code is well-structured and organized in a directory. This directory will be the root of your package.

3. Create a setup.py file: In the root directory of your package, create a file named `setup.py`. This file contains information about your package, such as its name, version, dependencies, and entry points. 

```
from setuptools import setup, find_packages

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

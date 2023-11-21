# Module



## Search path

We need to configure your Python environment so that when we do `from {moduleName}` it knows where to look for that `{moduleName}` folder. This is done through:

1. Locate the site-packages directory. 
2. Add a `.pth` file, say `my-path.pth` to that directory. Inside `my-path.pth` are directories you want to add to the search path.

To locate your environment's site-packages directory, run the following:



```python
import site
site.getsitepackages()
```




    ['/Users/martin/Documents/GitHub/112-2-programming-for-economic-modeling/.venv/lib/python3.11/site-packages']



Look for the path that ends with `.../pythonX.X/site-packages`. Reload your VScode. Use `sys.path` to check if the path is added to the search path. If you succeed, the following code should show your specified path.




```python
import sys
print(sys.path)
```

## Module folder

In Python, we can turn a folder said named `my-module` into a **SEARCHABLE** module by adding a **EMPTY** `__init__.py` file to it.

Module folder:

- Searchable: `sys.path` will search for it.
- Empty `__init__.py` inside.

Consider the following folder structure with subfolder and files:

```
mymodule
├── __init__.py
├── group1
│   └── extensions.py
└── basic.py
```

- Empty `__init__.py` only needs to sit in the root folder of the module.

Then you can:


```python
import mymodule.basic as basic
import mymodule.group1.extensions as extensions
```

To access functions, objects in `basic.py` through `basic` and `extensions.py` through `extensions`:



## Module Reload


```python
import importlib

importlib.reload(basic) # reload basic module
```

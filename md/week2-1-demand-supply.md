# 1. Demand and Supply

  * Understand how to setup a jupyter notebook lecture node.   
  * Concept of module and package.  
  * Understand how to use pass Python variable to R and vice versa.


## 1.2 Jupyter Notebook

## Select a kernel

![](../img/select%20kernal.png)

Select the kernel you want to use, which should be `.venv` in this case.

![](../img/kernel%20menu.png)

> If you did not see `.venv`, select **Select Another Kernel > Python Environments ...**, then choose the `.venv` you want to use. 

## 1.3 Python identation

Python uses indentation to indicate a block of code.

```python 
if 5 > 2:
  print("Five is greater than two!")
```

# Module not found error

![](../img/Module%20not%20found%20error.png)

To solve this problem, you need to install the missing module in the terminal:

```
pip install <module name>
```



To solve this problem, you need to add the following to `settings.json`:

```
"python.analysis.extraPaths": [
        "./src"
    ],
```
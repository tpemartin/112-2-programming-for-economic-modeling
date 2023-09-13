
# Jupyter Notebook

## Select a kernel

![](../img/select%20kernal.png)

Select the kernel you want to use, which should be `.venv` in this case.

![](../img/kernel%20menu.png)

> If you did not see `.venv`, select **Select Another Kernel > Python Environments ...**, then choose the `.venv` you want to use. 

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
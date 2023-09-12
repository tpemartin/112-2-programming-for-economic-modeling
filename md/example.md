
# Consumption theory

Consider the following Cobb-Douglas consumption function of two goods $x_1$ and $x_2$:  

$$
u(x_1, x_2) = x_1^{\alpha} x_2^{1-\alpha}
$$

where $\alpha \in (0,1)$ is a parameter.

The consumer's budget constraint is given by 

$$
p_1 x_1 + p_2 x_2 = m
$$

where $p_1$ and $p_2$ are the prices of the two goods and $m$ is the consumer's income.

We define the function in Python as follows:

```python
def u(x1, x2, alpha):
    return x1**alpha * x2**(1-alpha)
```



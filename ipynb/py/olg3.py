import numpy as np


def consumer_example():
    
    example = {
    "beta" : 0.96,
    "u": lambda c: np.log(c) # anonymous function
    }
    return example

x = consumer_example()

def saving(w, R):
    return (x["beta"]/(1+x["beta"]))*w

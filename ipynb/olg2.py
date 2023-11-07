import numpy as np


def consumer_example():
    
    example = {
    "beta" : 0.96,
    "u": lambda c: np.log(c) # anonymous function
    }
    return example

def saving(w, R):
    return (ce["beta"]/(1+ce["beta"]))*w

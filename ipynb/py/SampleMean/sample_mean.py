import numpy as np

class SampleMean:
    def __init__(self, draw_x, mu, sigma):
        self.draw_x = draw_x
        self.mu = mu
        self.sigma = sigma
        self.memory = []
    def one_sample(self, n):
        return one_sample(self, n)


# helpers

def one_sample(sm, n):
    X = sm.draw_x(n)
    return (X.mean() - sm.mu)/(sm.sigma/np.sqrt(n))
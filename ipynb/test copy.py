# import AR module
from py.AR.main import AR
import numpy as np

def Epsilon(mu, sigma):
    def draw(size):
        return np.random.normal(mu, sigma, size)
    return draw
    
epsilon = Epsilon(0, 0.4)

ar = AR(0.8, -0.35, epsilon=epsilon, Y0=[0,0])
ar.memory
ar.simulate_nPeriods(10)
ar.memory
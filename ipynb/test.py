# import AR module
# from py.AR.main import AR
import numpy as np
import os
if __name__ == '__main__':
    os.chdir('/Users/martin/Documents/GitHub/112-2-programming-for-economic-modeling/py')

from AR.main import AR

print(os.getcwd())


def Epsilon(mu, sigma):
    def draw(size):
        return np.random.normal(mu, sigma, size)
    return draw
    
epsilon = Epsilon(0, 0.4)

ar = AR(0.8, -0.35, epsilon=epsilon, Y0=[0,0])
ar.memory
ar.simulate_nPeriods(10)
ar.memory

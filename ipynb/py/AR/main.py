import numpy as np

class AR:
    def __init__(self, *args, epsilon, Y0):
        self.phi = np.array(args)
        self.epsilon = epsilon
        self.Y0 = np.array(Y0)
        self.memory = np.array([])
        self.YPast = np.array(self.Y0)
    def simulate_nPeriods(self, n=1):
        simulate_nPeriods(self, n)
    def clear_memory(self):
        self.memory = np.array([])

# helpers

def simulate_onePeriod(ar):
    # Simulate one period of ar process
    y_onePeriod_ahead = ar.phi@ar.YPast + ar.epsilon(1)

    # Update YPast
    ar.YPast = np.append(y_onePeriod_ahead, ar.YPast[:-1])

    ## append the new element to the memory
    ar.memory = np.append(ar.memory, y_onePeriod_ahead)

def simulate_nPeriods(ar, n):
    for i in range(n):
        simulate_onePeriod(ar)
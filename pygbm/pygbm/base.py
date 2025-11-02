import numpy as np

class StochasticProcess:
    '''
    A class for the stochastic process that defines the structure of the process.
    '''
    def __init__(self, y0, mu, sigma):
        self.y0 = y0 #Initial value of the process
        self.mu = mu #The drift value
        self.sigma = sigma #The randomness value

    def simulate_path(self, T: float, N: int):
            """To be implemented by subclasses."""
            raise NotImplementedError("Subclasses must implement simulate_path()")
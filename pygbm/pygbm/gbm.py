from .base import StochasticProcess
import numpy as np

class GBMSimulator(StochasticProcess):
    '''
    Simulate a Geometric Brownian Motion Path
    '''
    def simulate_path(self, T, N):
        dt = T / N
        t_values = np.linspace(0, T, N + 1)
        y_values = np.zeros(N + 1)
        y_values[0] = self.y0

        for i in range(1, N + 1):
            z = np.random.normal()
            y_values[i] = y_values[i - 1] * np.exp(
                (self.mu - 0.5 * self.sigma**2) * dt + self.sigma * np.sqrt(dt) * z
            )

        return t_values, y_values

# PYGMB

Solution to problem set 2 which requires creating our own python package.

# Question

## Geometric Brownian Motion Simulation Package

Geometric Brownian motion is a stochastic process that grows multiplicatively. It follows the stochastic differential equation (SDE):

$$
dY(t) = \mu Y(t)\,dt + \sigma Y(t)\,dB(t)
$$

where \( B(t) \) is Brownian motion, \( \mu \) is the drift, and \( \sigma \) is the diffusion coefficient.  
The solution is:

$$
Y(t) = Y_0 \exp\left(\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma B(t)\right)
$$

Goal: create a Python package `pygbm` that simulates GBM using an object-oriented design.

### Requirements

- Package name: `pygbm`
- Base class + derived class(es)
- Method to simulate GBM path
- Command-line interface (CLI)
- Ability to run code like:

```python
from pygbm import GBM
import matplotlib.pyplot as plt

gbm = GBM(mu=0.05, sigma=0.2, y0=1.0)
t, y = gbm.simulate(t_end=1.0, n_steps=1000)

plt.plot(t, y)
plt.show()

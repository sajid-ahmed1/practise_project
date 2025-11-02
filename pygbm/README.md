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

## 📘 Understanding `gbm.py` and the Mathematics Behind It

### 1. Theoretical Foundation

**Equation (2.1): Stochastic Differential Equation (SDE)**
$dY_t = \mu Y_t,dt + \sigma Y_t,dB_t$

* $\mu$ = the drift rate (expected rate of return per unit of time) - average growth
* $\sigma$ = the volatility (standard deviation of returns per unit of time) - magnitude of randomness
* $dB_t$ = the brownian increment N(0,dt)

This equation says that the change in $Y_t$ has two parts:

1. A **deterministic drift term** → $\mu Y_t dt$
2. A **random diffusion term** → $\sigma Y_t dB_t$

---

**Equation (2.2): Analytical Solution**
$$Y_t = Y_0 \exp!\Big((\mu - \tfrac{1}{2}\sigma^2)t + \sigma W_t\Big)$$

This gives the exact Geometric Brownian Motion path.
It shows that $Y_t$ is always **positive** and follows an **exponential random growth** pattern.

🧠 *Question:* Why is the term $-\tfrac{1}{2}\sigma^2$ subtracted in the exponent?
→ Hint: It corrects for mu so that the mean of $Y_t$ stays consistent with the drift.
→ It corrects for the variance of the exponential term so that the expected value 𝐸[𝑌𝑡] matches the drift 𝜇

---

### 2. How `GBMSimulator` Implements These Equations

**File:** `gbm.py`

```python
class GBMSimulator(StochasticProcess):
    def simulate_path(self, T: float, N: int):
        dt = T / N
        t_values = np.linspace(0, T, N + 1)
        y_values = np.zeros(N + 1)
        y_values[0] = self.y0

        for i in range(1, N + 1):
            z = np.random.normal()
            y_values[i] = y_values[i - 1] * np.exp(
                (self.mu - 0.5 * self.sigma**2) * dt
                + self.sigma * np.sqrt(dt) * z
            )

        return t_values, y_values
```

---

### 3. Code–Math Mapping

| Code part                           | Mathematical equivalent             | Meaning                 |
| ----------------------------------- | ----------------------------------- | ----------------------- |
| `dt = T / N`                        | ( Δt )                              | Time step size          |
| `z = np.random.normal()`            | ( Z \sim N(0,1) )                   | Random shock            |
| `(self.mu - 0.5*self.sigma**2)*dt`  | Drift correction term               | Controls average growth |
| `self.sigma*np.sqrt(dt)*z`          | ( \sigma \sqrt{Δt} Z )              | Random fluctuation      |
| `np.exp(...)`                       | ( e^{(\text{drift + randomness})} ) | Exponential update step |
| `y_values[i] = y_values[i-1] * ...` | ( Y_{t+Δt} = Y_t e^{(...)} )        | Recursive evolution     |

---

### 4. Interpretation

* Each loop step moves the process forward in **time** by ( Δt ).
* `simulate_path()` numerically builds one GBM trajectory using the formula derived from equation (2.2).
* The output `(t_values, y_values)` can be plotted to visualize the stochastic path.

🧩 *Question:*
If you make `N` twice as large while keeping `T` fixed, what happens to `dt` and how does it affect the smoothness of the simulated path?

*Answer:*
* If dt = T / N, doubling N would result in a smaller dt.
* This means we take really small changes in time, which would look smoother than looking at larger dt's because then we introduce more noise. We would also be closer tot he true continous GBM, smaller steps = better approximate of the Brownian motion.
* If dt was close to 0, then the deterministic drift goes to 0 and numerically, we are left with the random diffusion term positively affect the change in Y(t)

*Question:*
If you keep N fixed but increase σ, what happens to the simulated path’s appearance and variance?

*Answer:*
* The random diffusion term increase for each increment of time, so we see more volaitlity.
* In the stock price we would see wilder swings up and down.
* Variance would be larger and the distribution widens.

*Question:*
If μ = 0 and σ ≠ 0, what’s the expected value 𝐸[𝑌𝑡]?

*Answer:*


---

### 5. Summary

* `base.py` defines the **structure** of a stochastic process.
* `gbm.py` defines the **behavior** for Geometric Brownian Motion.
* Together they let you simulate paths for stock-like processes where prices evolve continuously but randomly.

---

Would you like me to add a final short section with a **visual intuition diagram** (ASCII or simple markdown sketch) showing drift vs volatility effects?


import argparse
from .gbm import GBMSimulator

def main():
    parser = argparse.ArgumentParser(description="Simulate a Geometric Brownian Motion")
    parser.add_argument("--s0", type=float, default=100)
    parser.add_argument("--mu", type=float, default=0.05)
    parser.add_argument("--sigma", type=float, default=0.2)
    parser.add_argument("--steps", type=int, default=100)
    args = parser.parse_args()

    gbm = GBMSimulator(args.s0, args.mu, args.sigma)
    path = gbm.simulate(args.steps)
    print(path)

import numpy as np

def generate_returns(n, mu=0.0, sigma=1.0):
    return np.random.normal(mu, sigma, size=n)

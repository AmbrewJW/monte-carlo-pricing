import numpy as np
import matplotlib.pyplot as plt


def generate_returns(n, mu=0.0, sigma=0.01, seed=None):
    """
    Generate n random returns from a normal distribution.

    Parameters:
        n (int): number of returns
        mu (float): mean return
        sigma (float): volatility (standard deviation)
        seed (int, optional): random seed for reproducibility

    Returns:
        np.ndarray: array of returns
    """
    if seed is not None:
        np.random.seed(seed)

    returns = np.random.normal(loc=mu, scale=sigma, size=n)
    return returns


def analyze_returns(returns):
    """
    Compute basic statistics for a return series.
    """
    mean = np.mean(returns)
    variance = np.var(returns)
    std_dev = np.std(returns)

    return mean, variance, std_dev


def plot_returns(returns, bins=50):
    """
    Plot a histogram of returns.
    """
    plt.hist(returns, bins=bins, density=True)
    plt.title("Histogram of Simulated Returns")
    plt.xlabel("Return")
    plt.ylabel("Density")
    plt.show()


if __name__ == "__main__":
    # Step 1 demo
    n = 10_000
    mu = 0.0005     # average return
    sigma = 0.01    # volatility

    returns = generate_returns(n, mu, sigma, seed=42)
    mean, var, std = analyze_returns(returns)

    print(f"Mean: {mean:.6f}")
    print(f"Variance: {var:.6f}")
    print(f"Std Dev: {std:.6f}")

    plot_returns(returns)

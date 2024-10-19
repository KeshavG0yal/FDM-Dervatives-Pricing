import numpy as np

def finite_difference_pricing(S_max, K, T, r, sigma, N_S, N_t, option_type):
    """Finite difference method for option pricing."""
    
    # Discretize the stock price and time
    S = np.linspace(0, S_max, N_S)  # Stock prices
    dt = T / N_t  # Time step
    dS = S_max / (N_S - 1)  # Price step

    # Initialize the option price grid
    V = np.zeros((N_S, N_t + 1))

    # Boundary conditions
    if option_type == 'call':
        V[:, -1] = np.maximum(S - K, 0)  # Call option payoff
    else:
        V[:, -1] = np.maximum(K - S, 0)  # Put option payoff

    # Finite difference method loop
    for j in range(N_t - 1, -1, -1):  # Iterate backward through time steps
        for i in range(1, N_S - 1):  # Iterate through stock prices (avoid boundaries)
            V[i, j] = (V[i, j + 1] + 
                        0.5 * sigma**2 * S[i]**2 * (V[i + 1, j + 1] - 2 * V[i, j + 1] + V[i - 1, j + 1]) * dt / dS**2 +
                        (r * S[i] * V[i + 1, j + 1] - r * S[i - 1] * V[i, j + 1]) * dt / (2 * dS))

    # Interpolate for the option price at S0
    S0_index = np.searchsorted(S, S_max)  # Get the index for the closest stock price
    return S, V

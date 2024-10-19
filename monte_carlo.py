import numpy as np

def monte_carlo_pricing(S0, K, T, r, sigma, N_sim, option_type='call'):
    dt = T / 100  # Number of time steps
    S_sim = np.zeros((N_sim, 101))
    S_sim[:, 0] = S0
    
    # Simulate price paths
    for t in range(1, 101):
        Z = np.random.standard_normal(N_sim)
        S_sim[:, t] = S_sim[:, t-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
    
    # Payoff calculation
    if option_type == 'call':
        payoff = np.maximum(S_sim[:, -1] - K, 0)
    elif option_type == 'put':
        payoff = np.maximum(K - S_sim[:, -1], 0)
    
    price = np.exp(-r * T) * np.mean(payoff)
    return price

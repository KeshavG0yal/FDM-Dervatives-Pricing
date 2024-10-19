import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from monte_carlo import monte_carlo_pricing
from black_scholes import black_scholes_call
from fdm_pricing import finite_difference_pricing
from database import connect_db, save_option_price, get_option_prices

def get_stock_data(ticker):
    """Fetch the latest stock price for the given ticker from Yahoo Finance."""
    stock = yf.Ticker(ticker)
    hist_data = stock.history(period="1y")
    return hist_data['Close'].iloc[-1]  # Use iloc to get the latest closing price

if __name__ == '__main__':
    # Parameters
    ticker = 'AAPL'  # Example: Apple Inc.
    S0 = get_stock_data(ticker)  # Fetch stock price
    K = 150  # Strike price
    T = 1.0  # Time to maturity (1 year)
    r = 0.05  # Risk-free interest rate
    sigma = 0.2  # Volatility

    # Run Monte Carlo pricing
    price_mc = monte_carlo_pricing(S0, K, T, r, sigma, 10000, 'call')

    # Run Black-Scholes pricing
    price_bs = black_scholes_call(S0, K, T, r, sigma)

    # Parameters for Finite Difference Method (FDM)
    S_max = 200  # Max stock price for grid
    N_S = 100  # Number of stock price steps
    N_t = 100  # Number of time steps

    # Run Finite Difference Method (FDM)
    S_grid, V_fdm = finite_difference_pricing(S_max, K, T, r, sigma, N_S, N_t, 'call')

    # Plotting results
    plt.plot(S_grid, V_fdm[:, -1], label='FDM Option Price', color='blue')  # Adjusted for the last time step
    plt.axhline(y=price_mc, color='red', linestyle='--', label=f'Monte Carlo Price: {price_mc:.2f}')
    plt.axhline(y=price_bs, color='green', linestyle='--', label=f'Black-Scholes Price: {price_bs:.2f}')
    plt.title('Option Prices Comparison')
    plt.xlabel('Stock Price')
    plt.ylabel('Option Price')
    plt.legend()
    plt.grid()
    plt.show()

    # Connect to MongoDB and save results
    collection = connect_db()
    save_option_price(collection, 'Monte Carlo', price_mc, {'S0': S0, 'K': K, 'T': T, 'sigma': sigma})
    save_option_price(collection, 'Black-Scholes', price_bs, {'S0': S0, 'K': K, 'T': T, 'sigma': sigma})
    save_option_price(collection, 'Finite Difference', V_fdm[-1, -1], {'S0': S0, 'K': K, 'T': T, 'sigma': sigma})

    # Retrieve and print all saved prices from MongoDB
    prices = get_option_prices(collection)
    print("\nSaved Option Prices:")
    for price in prices:
        print(price)

    # Output results
    print(f"\nMonte Carlo Price: {price_mc:.2f}")
    print(f"Black-Scholes Price: {price_bs:.2f}")
    print(f"Finite Difference Price (last point): {V_fdm[-1, -1]:.2f}")

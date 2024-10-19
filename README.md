# Derivative Pricing Using Finite Difference Method

## Project Overview

This project implements various numerical methods to price European-style options using a Finite Difference Method (FDM), Monte Carlo simulation, and the Black-Scholes formula. It aims to provide an understanding of derivative pricing techniques and their application in financial modeling.

## Features

- **Finite Difference Method**: Implements a grid-based numerical method to calculate option prices based on partial differential equations. The method discretizes both stock prices and time to solve for option prices at maturity and backtracks to the present value.
  
- **Monte Carlo Simulation**: Utilizes stochastic simulation to estimate the price of options by generating random paths for stock prices and calculating the expected payoff based on those paths. This method is particularly useful for pricing complex derivatives.

- **Black-Scholes Model**: Provides a closed-form solution for pricing European options, serving as a benchmark to compare results obtained from numerical methods.

- **Data Storage**: Integrates a MongoDB database to store calculated option prices along with relevant parameters, enabling easy retrieval and analysis of pricing data.

- **Visualization**: Generates plots comparing the results from the different pricing methods, allowing for a visual understanding of how each method performs under varying conditions.

## Technologies Used

- **Python**: The primary programming language for implementing the pricing algorithms.
- **NumPy**: For efficient numerical operations and handling of arrays.
- **Pandas**: For data manipulation and storage of option pricing data.
- **Matplotlib**: For plotting the results of the pricing methods.
- **MongoDB**: For storing and retrieving calculated option prices and parameters.

## Future Enhancements

- Implement additional option types, such as American options.
- Optimize the finite difference method for better performance and accuracy.
- Incorporate more advanced machine learning techniques for pricing derivatives.
- Enhance the user interface for better interaction and visualization of results.


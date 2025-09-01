import math
from scipy.stats import norm

def black_scholes(S0, K, T, r, sigma, option_type='call'):
    """
    Calculate the Black-Scholes option price.
    
    Parameters:
    - S0: Current price of the underlying asset (stock)
    - K: Strike price of the option
    - T: Time to expiration in days
    - r: Risk-free interest rate (annualized)
    - sigma: Volatility of the underlying asset (annualized)
    - option_type: 'call' for call option, 'put' for put option
    
    Returns:
    - Option price
    """
    d1 = (math.log(S0 / K) + (r + 0.5 * sigma ** 2) * (T/365)) / (sigma * math.sqrt((T/365)))
    d2 = d1 - sigma * math.sqrt((T/365))
    
    if option_type == 'call':
        option_price = S0 * norm.cdf(d1) - K * math.exp(-r * (T/365)) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * math.exp(-r * (T/365)) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Choose 'call' or 'put'.")
    
    return option_price

S0 = float(input("Enter the current stock price (S0): "))
K = float(input("Enter the strike price of the option (K): "))
T = float(input("Enter the time to expiration in days (T): "))
r = float(input("Enter the risk-free interest rate (annualized, r): ")) / 100  
sigma = float(input("Enter the volatility of the underlying asset (annualized, sigma): ")) / 100  
option_type = input("Enter the option type ('call' or 'put'): ").strip().lower()


try:
    option_price = black_scholes(S0, K, T, r, sigma, option_type)
    print(f"The price of the {option_type} option is: ${option_price:.2f}")
except ValueError as e:
    print(e)

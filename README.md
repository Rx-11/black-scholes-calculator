# Black-Scholes Option Pricing Calculator

This is a simple Python implementation of the **Black-Scholes model** for calculating the theoretical price of European-style **call** and **put options**. The Black-Scholes model takes several factors into account, including the current stock price, strike price, time to expiration, risk-free interest rate, and volatility, to compute the fair price of an option.

## Requirements

To run this project, you'll need Python installed, along with the following Python packages:
- `math`
- `scipy`

You can install the necessary dependencies using pip:
```bash
pip install scipy
```

## How It Works

This calculator allows you to compute the price of an option (either call or put) based on the following parameters:

- **S0**: The current price of the underlying asset (stock).
- **K**: The strike price of the option.
- **T**: Time to expiration in days.
- **r**: The annual risk-free interest rate (as a percentage, e.g., 5% is entered as 5).
- **sigma**: The annual volatility of the underlying asset (as a percentage, e.g., 20% is entered as 20).
- **option_type**: Choose either 'call' for a call option or 'put' for a put option.

The program uses the Black-Scholes formula to compute the price of the option, outputting either the call or put option price.

## Usage

Run the Python script and provide the required inputs when prompted.

### Example input/output:

```
Enter the current stock price (S0): 100
Enter the strike price of the option (K): 95
Enter the time to expiration in days (T): 365
Enter the risk-free interest rate (annualized, r): 5
Enter the volatility of the underlying asset (annualized, sigma): 20
Enter the option type ('call' or 'put'): call
The price of the call option is: $10.45
```

This will calculate the price of a call option with the given parameters.

## Key Notes

- Risk-free rate (r) and volatility (sigma) should be entered as percentages (e.g., 5 for 5%).
- Time to expiration (T) is provided in days.
- The program uses the Cumulative Normal Distribution Function (CDF) to estimate the likelihood of an option finishing in-the-money, which is crucial for accurate pricing.


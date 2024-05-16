'''
option pricing methods like Black-Scholes-Merton have been used for a long time, but they have some limitations that make them less effective in practice.
'''
import numpy as np
from scipy.stats import norm

def black_scholes_merton(S, K, T, r, sigma):
    """
    Calculate the price of a European call option using the Black-Scholes-Merton model.
    S: Current stock price
    K: Strike price
    T: Time to expiration (in years)
    r: Risk-free interest rate
    sigma: Volatility of the underlying stock
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

def heuristic_option_pricing(S, K, T, r):
    """
    A simple heuristic approach for option pricing.
    S: Current stock price
    K: Strike price
    T: Time to expiration (in years)
    r: Risk-free interest rate
    """
    # Assume a fixed percentage of the strike price as the option price
    call_price = max(S - K, 0) * 0.5  # Just a basic heuristic, not based on any sophisticated model
    return call_price

# Parameters
S = 100  # Current stock price
K = 110  # Strike price
T = 1    # Time to expiration (1 year)
r = 0.05 # Risk-free interest rate
sigma = 0.2  # Volatility

# Calculate option price using Black-Scholes-Merton model
bsm_price = black_scholes_merton(S, K, T, r, sigma)

# Calculate option price using heuristic approach
heuristic_price = heuristic_option_pricing(S, K, T, r)

# Print results
print("Black-Scholes-Merton option price:", bsm_price)
print("Heuristic option price:", heuristic_price)
'''
Ora immagina che tu abbia due strade per far correre le tue macchinine: una strada molto lunga e liscia e un'altra strada corta e un po' accidentata.

Nella prima strada, chiamata "Black-Scholes-Merton", le tue macchinine corrono molto veloci e in modo molto regolare, senza incontrare ostacoli lungo il percorso. Quindi, quando guardi l'andamento delle tue macchinine su questa strada, vedi una linea retta che sale o scende dolcemente.

Nella seconda strada, chiamata "euristica" (che è una parola difficile che significa "fare un'ipotesi basata sull'esperienza"), le tue macchinine corrono in modo un po' più casuale. A volte vanno veloci, altre volte rallentano un po'. Quando guardi l'andamento delle tue macchinine su questa strada, vedi una linea che salta su e giù in modo irregolare.

Quindi, se dovessi disegnare l'andamento delle tue macchinine sulla strada "Black-Scholes-Merton", vedresti una linea retta che sale o scende dolcemente. Ma se dovessi disegnare l'andamento delle tue macchinine sulla strada "euristica", vedresti una linea che salta su e giù in modo irregolare.

Nel nostro esempio, la prima strada rappresenta il modo matematico più preciso di calcolare il prezzo di un'opzione, mentre la seconda strada rappresenta un modo più semplice e approssimato di farlo.
'''

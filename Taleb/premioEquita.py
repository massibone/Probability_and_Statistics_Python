'''
Il "puzzle del premio di equità" si riferisce al fenomeno per cui le azioni hanno storicamente reso un rendimento più elevato rispetto agli investimenti a reddito fisso, senza che questo eccesso di rendimento sia stato arbitrato via nel tempo. Questo studio mette in discussione l'analisi di tale fenomeno, sottolineando l'importanza di considerare gli effetti di secondo ordine, come la mancanza di ergodicità e le code spesse nella distribuzione delle variabili finanziarie.
'''


import numpy as np
from scipy.stats import norm

# Definizione della funzione di valutazione della teoria prospettica
def w_lambda_alpha(x, lambda_val, alpha):
    if x >= 0:
        return x**alpha
    else:
        return -lambda_val * (-x)**alpha

# Calcolo dell'utilità attesa
def expected_utility(t, sigma, mu, alpha, lambda_val):
    sqrt_t = np.sqrt(t)
    sigma_sq_t = sigma**2 * t
    pi_sqrt = np.sqrt(np.pi)
    
    first_term = pi_sqrt / (2 * alpha) * (1 / sigma_sq_t)**(alpha/2)
    second_term = norm.cdf(-t * mu / (2 * sigma**2), 0, 1)
    third_term = (mu * np.sqrt(2 * sigma_sq_t) / (np.sqrt(2 * sigma)) *
                  norm.cdf(t * mu / (2 * sigma**2), 0, 1))
    
    return (first_term * (norm.cdf(-t * mu / (2 * sigma**2), 0, 1) -
                           lambda_val * np.sqrt(sigma_sq_t) * norm.cdf(t * mu / (2 * sigma**2), 0, 1) +
                           mu * np.sqrt(2 * sigma_sq_t) / (np.sqrt(2 * sigma)) *
                           norm.cdf(t * mu / (2 * sigma**2), 0, 1)))

# Esempio di utilizzo della funzione di utilità attesa
t = 1
sigma = 1
mu = 1
alpha = 2
lambda_val = 0.5

utility = expected_utility(t, sigma, mu, alpha, lambda_val)
print("Expected utility:", utility)

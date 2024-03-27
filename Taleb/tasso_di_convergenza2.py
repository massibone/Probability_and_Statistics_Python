import numpy as np
from scipy.special import gammainc

# Definizione dei valori specifici
n = 5

# Calcolo del tasso di convergenza κ1,n
M_1 = 2 * np.sqrt(3) / np.sqrt(np.pi)
M_n = 2 * np.sqrt(3) / (np.sqrt(np.pi) * (np.exp(n**n - n * gammainc(n + 1, n) - 1)))

kappa_1_n = 2 - np.log(n) / np.log(np.exp(n**n - n * gammainc(n + 1, n) - 1))

print(f"Tasso di convergenza κ1,n per n = {n}: {kappa_1_n}")

import numpy as np

# Definizione delle funzioni per il calcolo delle opzioni di put e call
def european_call_option(S0, K, t, r, T):
    F = S0 * np.exp(r * (T - t))
    return max(F - K, 0)

def european_put_option(S0, K, t, r, T):
    F = S0 * np.exp(r * (T - t))
    return max(K - F, 0)


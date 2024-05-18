import numpy as np

# Definizione delle funzioni per il calcolo delle opzioni di put e call
def european_call_option(S0, K, t, r, T):
    F = S0 * np.exp(r * (T - t))
    return max(F - K, 0)

def european_put_option(S0, K, t, r, T):
    F = S0 * np.exp(r * (T - t))
    return max(K - F, 0)

# Definizione dei parametri
S0 = 100  # Prezzo attuale dell'attività sottostante
K = 110  # Prezzo di esercizio dell'opzione
t = 0  # Tempo attuale
r = 0.05  # Tasso di interesse senza rischio
T = 1  # Tempo di scadenza dell'opzione

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

# Calcolo delle opzioni di put e call utilizzando le formule fornite
call_price = european_call_option(S0, K, t, r, T)
put_price = european_put_option(S0, K, t, r, T)

# Stampare i risultati
print("Prezzo dell'opzione di call europea:", call_price)
print("Prezzo dell'opzione di put europea:", put_price)

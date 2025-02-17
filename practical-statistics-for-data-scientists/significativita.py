'''
La significatività statistica misura se un risultato di un esperimento è più estremo di quanto la casualità potrebbe produrre. 
In un esempio di test sul web, due prezzi mostrano tassi di conversione diversi. Anche con oltre 45.000 dati, 
è importante testare la significatività statistica a causa dei bassi tassi di conversione (meno dell'1%). 
Usando una procedura di permutazione, possiamo determinare se la differenza osservata è dovuta al caso o è significativa.
'''
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt


# Dati dell'esperimento di e-commerce
conversion_A = 200
no_conversion_A = 23539
conversion_B = 182
no_conversion_B = 22406

# Calcolare la differenza osservata in percentuale di conversione
obs_pct_diff = 100 * (conversion_A / (conversion_A + no_conversion_A) - conversion_B / (conversion_B + no_conversion_B))
print(f'Observed difference: {obs_pct_diff:.4f}%')

# Creare la lista dei dati di conversione combinati
conversion = [0] * (no_conversion_A + no_conversion_B)
conversion.extend([1] * (conversion_A + conversion_B))
conversion = pd.Series(conversion)
# Funzione di permutazione
def perm_fun(x, nA, nB):
    n = nA + nB
    idx_B = set(random.sample(range(n), nB))
    idx_A = set(range(n)) - idx_B
    return x.iloc[list(idx_B)].mean() - x.iloc[list(idx_A)].mean()

# Numero di campionamenti
nA = conversion_A + no_conversion_A
nB = conversion_B + no_conversion_B

# Calcolare le differenze di conversione permutate
perm_diffs = [100 * perm_fun(conversion, nA, nB) for _ in range(1000)]

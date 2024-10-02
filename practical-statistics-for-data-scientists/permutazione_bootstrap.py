'''
Ci sono due varianti del test di permutazione oltre al test di permutazione casuale:

Test di permutazione esaustivo: consiste nel calcolare tutte le possibili divisioni dei dati, pratico solo per piccoli campioni.
Test di permutazione bootstrap: i campionamenti vengono effettuati con reinserimento, modellando la variabilità sia nell'assegnazione del trattamento che nella selezione dei soggetti.
I test di permutazione sono utili per esplorare il ruolo della variazione casuale, sono facili da codificare, interpretare e spiegare,
e non richiedono le stesse ipotesi sui dati normalmente distribuiti come i metodi basati su formule.
'''

import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

# Dati di esempio: tempi di sessione per le pagine A e B
session_times = pd.DataFrame({
    'Page': ['Page A'] * 21 + ['Page B'] * 15,
    'Time': np.random.normal(200, 50, 21).tolist() + np.random.normal(235, 50, 15).tolist()
})

# Funzione per il test di permutazione bootstrap
def bootstrap_perm_fun(x, nA, nB):
    n = nA + nB
    idx_B = set(random.choices(range(n), k=nB))
    idx_A = set(range(n)) - idx_B
    return x.loc[idx_B].mean() - x.loc[idx_A].mean()

# Numero di campionamenti
nA = 21
nB = 15
mean_a = session_times[session_times.Page == 'Page A'].Time.mean()
mean_b = session_times[session_times.Page == 'Page B'].Time.mean()

# Differenza osservata
observed_diff = mean_b - mean_a

# Calcolare le differenze permutate bootstrap
perm_diffs = [bootstrap_perm_fun(session_times.Time, nA, nB) for _ in range(1000)]

# Grafico della distribuzione delle differenze permutate bootstrap
fig, ax = plt.subplots(figsize=(5, 5))
ax.hist(perm_diffs, bins=11, rwidth=0.9)
ax.axvline(x=observed_diff, color='black', lw=2)
ax.text(observed_diff + 2, max(plt.hist(perm_diffs, bins=11)[0]) / 2, 'Differenza\nosservata', bbox={'facecolor': 'white'})
ax.set_xlabel('Differenze nei tempi di sessione (in secondi)')
ax.set_ylabel('Frequenza')
plt.show()

# Percentuale delle differenze permutate maggiori della differenza osservata
p_value = np.mean(perm_diffs > observed_diff)
print(f"P-value: {p_value:.3f}")

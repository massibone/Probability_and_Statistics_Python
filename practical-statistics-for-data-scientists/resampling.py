'''
Il "Resampling" (ricampionamento) in statistica significa ripetere campionamenti di valori dai dati osservati per valutare la variabilità casuale di una statistica. Può essere utilizzato anche per migliorare l'accuratezza di alcuni modelli di machine learning. Esistono due principali procedure di ricampionamento: il bootstrap e i test di permutazione. Il bootstrap valuta l'affidabilità di una stima, mentre i test di permutazione verificano le ipotesi, tipicamente tra due o più gruppi.
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

# Funzione per il test di permutazione
def perm_fun(x, nA, nB):
    n = nA + nB
    idx_B = set(random.sample(range(n), nB))
    idx_A = set(range(n)) - idx_B
    return x.loc[idx_B].mean() - x.loc[idx_A].mean()

# Numero di campionamenti
nA = 21
nB = 15
mean_a = session_times[session_times.Page == 'Page A'].Time.mean()
mean_b = session_times[session_times.Page == 'Page B'].Time.mean()

# Differenza osservata
observed_diff = mean_b - mean_a

# Calcolare le differenze permutate
perm_diffs = [perm_fun(session_times.Time, nA, nB) for _ in range(1000)]

# Grafico della distribuzione delle differenze permutate
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

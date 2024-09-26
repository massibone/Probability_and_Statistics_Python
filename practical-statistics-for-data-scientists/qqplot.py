'''
Una distribuzione normale standard è una distribuzione normale dove i valori sull'asse x sono espressi in termini di deviazioni standard dalla media. Per confrontare i dati con una distribuzione normale standard, si sottrae la media e si divide per la deviazione standard, un processo noto come standardizzazione o normalizzazione, ottenendo così i cosiddetti z-score. Un QQ-Plot è utilizzato per confrontare visivamente una distribuzione campionaria con una distribuzione specificata, come quella normale. Se i punti del QQ-Plot cadono approssimativamente sulla linea diagonale, significa che la distribuzione del campione è vicina a quella normale.
'''

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Genera un campione di dati da una distribuzione normale
data = np.random.normal(loc=0, scale=1, size=100)

# Calcola i z-score (standardizzazione)
mean = np.mean(data)
std_dev = np.std(data)
z_scores = (data - mean) / std_dev

# Crea un QQ-Plot
fig, ax = plt.subplots(figsize=(4, 4))
stats.probplot(z_scores, dist="norm", plot=ax)
ax.get_lines()[1].set_color('grey')  # Cambia il colore della linea di riferimento
plt.title("QQ-Plot di un campione di 100 valori normalizzati")
plt.show()

'''
In questo codice:
Generiamo 100 dati da una distribuzione di Pareto e da una distribuzione stabile.
Creiamo due grafici a istogramma per visualizzare le distribuzioni generate.
La distribuzione di Pareto è asimmetrica mentre la distribuzione stabile può essere configurata per essere asimmetrica.
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto, levy_stable

# Genera 100 dati da una distribuzione di Pareto
alpha = 3
samples_pareto = (np.random.pareto(alpha, 100) + 1)

# Genera 100 dati da una distribuzione stabile
alpha_stable = 1.7
samples_stable = levy_stable.rvs(alpha_stable, size=100)

# Crea un istogramma per visualizzare le distribuzioni
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(samples_pareto, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribuzione di Pareto')
plt.xlabel('Valore')
plt.ylabel('Frequenza')

plt.subplot(1, 2, 2)
plt.hist(samples_stable, bins=20, color='salmon', edgecolor='black', alpha=0.7)
plt.title('Distribuzione Stabile')
plt.xlabel('Valore')
plt.ylabel('Frequenza')

plt.tight_layout()
plt.show()

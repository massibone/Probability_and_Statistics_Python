'''
utilizzare la distribuzione di Pareto 
con Python per descrivere la 
distribuzione dei redditi, 
dove la maggior parte delle persone 
ha redditi bassi, ma un piccolo numero di individui ha redditi estremamente elevati. 
In un contesto specifico, si potrebbe osservare che ad esempio il 20% della popolazione possiede l'80% della ricchezza totale, un modello che riflette il principio di Pareto.
'''

import numpy as np
import matplotlib.pyplot as plt

# Parametri della distribuzione di Pareto
alpha = 1.5  # parametro di forma
n_samples = 1000  # numero di campioni

# Generare campioni casuali dalla distribuzione di Pareto
incomes = np.random.pareto(alpha, n_samples)

# Visualizzare l'istogramma dei redditi generati
plt.hist(incomes, bins=30, edgecolor='black')
plt.title('Distribuzione dei redditi (Pareto)')
plt.xlabel('Reddito')
plt.ylabel('Frequenza')
plt.grid(True)
plt.show()

# Calcolare la percentuale della popolazione che possiede una certa percentuale della ricchezza totale
percentile_80_20 = np.percentile(incomes, 80)
percentage_80_20 = np.sum(incomes >= percentile_80_20) / n_samples * 100

print(f"Il 20% della popolazione possiede l'80% della ricchezza totale: {percentage_80_20:.2f}%")

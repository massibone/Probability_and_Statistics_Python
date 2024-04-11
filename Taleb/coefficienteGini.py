'''
Guardando il grafico, vediamo che entrambi i metodi, sia il "NonParametric" che il "Maximum Likelihood", ci danno un numero che sembra essere vicino a 0.8333 quando abbiamo molte persone nel gruppo. Questo potrebbe significare che la distribuzione dei soldi diventa più equa quando abbiamo molte persone nel gruppo.
'''

import numpy as np
import matplotlib.pyplot as plt

# Dati dalla tabella
n = [10**3, 10**4, 10**5, 10**6, 10**7]
nonpar = [0.711, 0.750, 0.775, 0.790, 0.802]
ml = [0.8333, 0.8333, 0.8333, 0.8333, 0.8333]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(n, nonpar, marker='o', label='NonParametric')
plt.plot(n, ml, marker='o', label='Maximum Likelihood')
plt.xscale('log')
plt.xlabel('Numero di osservazioni (n)')
plt.ylabel('Stima del coefficiente di Gini')
plt.title('Confronto tra stime NonParametric e Maximum Likelihood del coefficiente di Gini')
plt.legend()
plt.grid(True)
plt.show()

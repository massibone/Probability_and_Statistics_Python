'''
In questo esempio, generiamo due grafici affiancati per rappresentare i dati di esempio sul numero di vittime dei conflitti nel corso del tempo. Il primo grafico mostra il numero effettivo di vittime stimato ogni 25 anni, mentre il secondo grafico rappresenta i dati riscalati rispetto alla popolazione mondiale nel 2015.

L'analisi dei dati e la loro rappresentazione grafica sono fondamentali per comprendere le tendenze nel tempo e per valutare correttamente l'entità degli eventi estremi, come nel caso dei conflitti con un elevato numero di vittime.
'''

import matplotlib.pyplot as plt

# Dati di esempio per il numero di vittime nel corso del tempo
years = list(range(1900, 2025, 25))
actual_victims = [50000, 75000, 100000, 125000, 150000, 175000, 200000, 225000, 250000, 275000]
rescaled_victims = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Plot dei dati effettivi e riscalati nel corso del tempo
plt.figure(figsize=(12, 6))

# Grafico per i dati effettivi
plt.subplot(1, 2, 1)
plt.plot(years, actual_victims, marker='o', linestyle='-', color='b')
plt.title('Numero Effettivo di Vittime dei Conflitti nel Tempo')
plt.xlabel('Anno')
plt.ylabel('Numero di Vittime')
plt.grid(True)

# Grafico per i dati riscalati
plt.subplot(1, 2, 2)
plt.plot(years, rescaled_victims, marker='s', linestyle='--', color='r')
plt.title('Numero di Vittime Riscalato (rispetto al 2015)')
plt.xlabel('Anno')
plt.ylabel('Numero di Vittime (Riscalato)')
plt.grid(True)

plt.tight_layout()  # Per migliorare la disposizione dei grafici
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, bernoulli

# Parametri delle variabili aleatorie
n = 10  # Numero di tentativi
p1 = 0.3  # Probabilità di successo per la variabile aleatoria 1
p2 = 0.5  # Probabilità di successo per la variabile aleatoria 2
p3 = 0.7  # Probabilità di successo per la variabile aleatoria 3
# Generazione dei valori possibili per la variabile aleatoria
x = np.arange(0, n+1)


# Calcolo delle funzioni di massa di probabilità per le variabili aleatorie
pmf1 = binom.pmf(x, n, p1)
pmf2 = binom.pmf(x, n, p2)
pmf3 = binom.pmf(x, n, p3)

# Creazione del grafico
plt.plot(x, pmf1, 'bo-', label='Variabile Aleatoria 1')
plt.plot(x, pmf2, 'go-', label='Variabile Aleatoria 2')
plt.plot(x, pmf3, 'ro-', label='Variabile Aleatoria 3')
plt.xlabel('Numero di successi')
plt.ylabel('Probabilità')
plt.title('Funzione di Massa di Probabilità per Variabili Aleatorie Binomiali')
plt.legend()
plt.grid(True)

# Visualizzazione del grafico
plt.show()

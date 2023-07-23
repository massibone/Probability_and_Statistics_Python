import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import hypergeom

# Parametri della distribuzione ipergeometrica
N = 100  # Popolazione totale
K = 50   # Numero di successi nella popolazione
n = 20   # Numero di estrazioni

# Generazione dei valori possibili per la variabile aleatoria
x = np.arange(0, n+1)

# Calcolo della funzione di massa di probabilità per la distribuzione ipergeometrica
pmf = hypergeom.pmf(x, N, K, n)

# Creazione del grafico
plt.bar(x, pmf, align='center', alpha=0.5)
plt.xlabel('Numero di successi')
plt.ylabel('Probabilità')
plt.title('Funzione di Massa di Probabilità per Distribuzione Ipergeometrica')
plt.grid(True)

# Visualizzazione del grafico
plt.show()

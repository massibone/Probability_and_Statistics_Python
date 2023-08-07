import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

# Parametri della distribuzione di Poisson
lambda_ = 4  # Parametro lambda
omega = 5  # Intervallo di valori fino a omega

# Generazione dei valori possibili per la variabile casuale
x = np.arange(0, omega+1)

# Calcolo della funzione di massa di probabilità per la distribuzione di Poisson
pmf = poisson.pmf(x, lambda_)

# Creazione del grafico
plt.bar(x, pmf, align='center', alpha=0.5)
plt.xlabel('Numero di successi')
plt.ylabel('Probabilità')
plt.title('Funzione di Massa di Probabilità per Distribuzione di Poisson')
plt.grid(True)

# Visualizzazione del grafico
plt.show()

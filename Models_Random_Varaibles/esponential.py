import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon

# Parametro della distribuzione esponenziale
lambda_ = 0.5

# Generazione dei valori possibili per la variabile casuale
x = np.linspace(0, 10, 1000)

# Calcolo della funzione di densità di probabilità per la distribuzione esponenziale
pdf = expon.pdf(x, scale=1/lambda_)
# Creazione del grafico
plt.plot(x, pdf, 'r-', lw=2, label='Variabile Aleatoria Esponenziale')
plt.xlabel('Valore')
plt.ylabel('Densità di Probabilità')
plt.title('Funzione di Densità di Probabilità per Variabile Aleatoria Esponenziale')
plt.legend()
plt.grid(True)

# Visualizzazione del grafico
plt.show()
-gamma.py e png
-degrreFreedom.py e png
-problem.py


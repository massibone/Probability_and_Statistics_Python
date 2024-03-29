import numpy as np
import matplotlib.pyplot as plt

# Funzione per generare dati con distribuzione subexponenziale
def subexponential_distribution(size, cusp):
    return np.random.exponential(scale=cusp, size=size) - cusp

# Parametri per le distribuzioni
size = 1000  # Numero di campioni
variance = 1  # Varianza delle distribuzioni
cusp = variance / 2  # Cusp per la distribuzione subexponenziale

# Genera i dati per entrambe le distribuzioni
gaussian_data = np.random.normal(loc=0, scale=np.sqrt(variance), size=size)
subexp_data = subexponential_distribution(size, cusp)

# Crea il grafico
plt.figure(figsize=(10, 6))

# Grafico della distribuzione gaussiana
plt.hist(gaussian_data, bins=30, alpha=0.5, label='Gaussiana', density=True)

# Grafico della distribuzione subexponenziale
plt.hist(subexp_data, bins=30, alpha=0.5, label='Subexponenziale', density=True)

# Aggiungi titolo e legenda
plt.title('Confronto tra Distribuzione Gaussiana e Subexponenziale')
plt.xlabel('Valore')
plt.ylabel('Densità di probabilità')
plt.legend()

# Mostra il grafico
plt.show()


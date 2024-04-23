import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import genpareto

# Dati di esempio (esceedances dai dati duali)
exceedances = [0.5, 0.7, 1.2, 1.5, 2.0]  # Esempio di exceedances (Z)

# Threshold (u) e stima del numero di exceedances
u = 1.0
nu = sum(1 for x in exceedances if x > u)  # Numero di exceedances sopra u
n = len(exceedances)  # Numero totale di osservazioni

# Stima dei parametri della distribuzione GPD
xi = 1.62  # Stima del parametro ξ
beta = 1.1747e6  # Stima del parametro β

# Calcolo della tail estimator (Equazione 17.6)
def tail_estimator(z, u, nu, n, xi, beta):
    return 1 - genpareto.cdf(z, xi, scale=beta, loc=u) * (nu / n)

# Range di valori per il grafico della coda
z_values = np.linspace(1, 5, 100)

# Calcolo della tail estimator per i valori di z
tail_values = [tail_estimator(z, u, nu, n, xi, beta) for z in z_values]

# Grafico della tail estimator
plt.figure(figsize=(10, 6))
plt.plot(z_values, tail_values, label='Tail Estimator (G¯(z))', color='red')
plt.title('Tail Estimator of Exceedances Distribution')
plt.xlabel('z')
plt.ylabel('G¯(z)')
plt.grid(True)
plt.legend()
plt.show()

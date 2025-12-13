import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione di trasformazione phi
def phi(Y, L, H):
    return L - H * np.log((H - Y) / (H - L))

# Dati di esempio (mortalità media delle pandemie)
avg_estimates = [7.5, 10.0, 5.0, 20.0, 15.0]  # Esempio di stime medie di mortalità (in milioni)

# Parametri per la trasformazione
L = 0  # Limite inferiore (assumendo L = 0)
H = 7.7e9  # Limite superiore (popolazione mondiale attuale)

# Applica la trasformazione ai dati per ottenere i valori Z (distribuzione duale)
Z_values = [phi(avg, L, H) for avg in avg_estimates]

# Grafico dei dati originali e dei dati trasformati (distribuzione duale)
plt.figure(figsize=(10, 6))
plt.scatter(avg_estimates, np.zeros_like(avg_estimates), label='Original Data (Y)', color='blue')
plt.scatter(Z_values, np.ones_like(Z_values), label='Dual Distribution (Z)', color='red')
plt.axhline(y=0, color='black', linestyle='--', linewidth=0.5)  # Linea orizzontale per i dati Y
plt.axhline(y=1, color='black', linestyle='--', linewidth=0.5)  # Linea orizzontale per i dati Z
plt.yticks([0, 1], ['Y', 'Z'])  # Etichette per i dati Y e Z sull'asse y
plt.title('Dual Distribution Transformation')
plt.xlabel('Average Mortality (millions)')
plt.legend()
plt.show()


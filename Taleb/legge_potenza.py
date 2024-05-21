import numpy as np
import matplotlib.pyplot as plt

# Definizione dei parametri della legge di potenza
xmin = 1  # Valore minimo
alpha = 2  # Esponente della legge di potenza

# Generazione di dati casuali secondo una legge di potenza
data = np.random.pareto(alpha, 1000) + xmin

# Creazione di un istogramma per visualizzare i dati
plt.hist(data, bins=30, density=True, alpha=0.5, color='b')

# Calcolo della funzione di sopravvivenza
x = np.linspace(min(data), max(data), 100)
survival_function = ((xmin / x) ** alpha)

# Visualizzazione della funzione di sopravvivenza
plt.plot(x, survival_function, 'r-', linewidth=2)
plt.xlabel('Valore')
plt.ylabel('Probabilità di sopravvivenza')
plt.title('Legge di potenza')
plt.show()


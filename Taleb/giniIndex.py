'''
 quando tiriamo il dado molte volte, il Gini index tende a comportarsi in un modo particolare
'''
import numpy as np
import matplotlib.pyplot as plt

# Funzione per calcolare il Gini index
def gini_index(data):
    n = len(data)
    data.sort()
    coef = 2 / n
    indexes = np.arange(1, n + 1)
    weighted_sum = (indexes * data).sum()
    total = data.sum()
    return coef * weighted_sum / total - (n + 1) / n

# Numero di lanci del dado, cresce esponenzialmente con n
ns = np.arange(1, 8)
num_rolls = 10 ** ns

# Simulazione del lancio del dado e calcolo del Gini index
gini_values = []
for n in num_rolls:
    # Simula il lancio del dado un numero n di volte
    dice_rolls = np.random.randint(1, 7, size=n)
    # Calcola il Gini index basato sui risultati dei lanci
    gini_values.append(gini_index(dice_rolls))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(num_rolls, gini_values, marker='o')
plt.xscale('log')
plt.xlabel('Numero di lanci del dado (n)')
plt.ylabel('Gini Index')
plt.title('Convergenza del Gini Index al crescere del numero di lanci del dado')
plt.grid(True)
plt.show()

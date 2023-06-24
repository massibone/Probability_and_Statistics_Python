'''
Ecco un diagramma a barre che rappresenta la frequenza di uscita delle sei facce di un dado su 40 lanci. 
Le linee tratteggiate rosse, verdi e blu rappresentano rispettivamente la media campionaria, la mediana campionaria e la moda campionaria.
'''

import matplotlib.pyplot as plt
import numpy as np

# Frequenza di uscita delle sei facce di un dado
frequencies = [8, 7, 6, 9, 5, 5]

# Calcolo la media campionaria
mean = np.mean(frequencies)

# Calcolo la mediana campionaria
median = np.median(frequencies)

# Calcolo la moda campionaria
mode = np.argmax(frequencies) + 1

# Etichette delle facce del dado
labels = ['1', '2', '3', '4', '5', '6']

# Creazione del diagramma a barre
fig, ax = plt.subplots()
ax.bar(labels, frequencies)

# Aggiunta delle linee per la media, mediana e moda
ax.axhline(mean, color='r', linestyle='--', label='Media')
ax.axhline(median, color='g', linestyle='--', label='Mediana')
ax.axhline(frequencies[mode-1], color='b', linestyle='--', label='Moda')

# Etichette degli assi
ax.set_xlabel('Faccia del dado')
ax.set_ylabel('Frequenza di uscita')

# Titolo del diagramma
ax.set_title('Frequenza di uscita delle facce di un dado')

# Aggiunta della legenda
ax.legend()

# Mostra il diagramma
plt.show()

#sempre per i dadi

import matplotlib.pyplot as plt
import numpy as np

# Frequenza di uscita delle sei facce di un dado
frequencies = [8, 7, 6, 9, 5, 5]

# Calcolo la media campionaria
mean = np.mean(frequencies)

# Calcolo la varianza campionaria
variance = np.var(frequencies, ddof=1)

# Etichette delle facce del dado
labels = ['1', '2', '3', '4', '5', '6']

# Creazione del diagramma a barre
fig, ax = plt.subplots()
ax.bar(labels, frequencies)

# Aggiunta della linea per la media
ax.axhline(mean, color='r', linestyle='--', label='Media')

# Etichette degli assi
ax.set_xlabel('Faccia del dado')
ax.set_ylabel('Frequenza di uscita')

# Titolo del diagramma
ax.set_title('Frequenza di uscita delle facce di un dado')

# Aggiunta della legenda
ax.legend()

# Mostra il diagramma
plt.show()

# Stampa della varianza campionaria
print("Varianza campionaria:", variance)
#la varianza campionaria viene calcolata utilizzando la funzione np.var() 
con il parametro ddof impostato su 1 per indicare che si tratta di una varianza campionaria anziché di una varianza popolazione.

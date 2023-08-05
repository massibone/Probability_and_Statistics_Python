import numpy as np
import matplotlib.pyplot as plt

# Dati di esempio
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 6, 7])

# Calcolo la varianza
varianza_x = np.var(x)
varianza_y = np.var(y)
# Calcolo la covarianza
covarianza = np.cov(x, y)[0, 1]

# Creazione del grafico
fig, ax = plt.subplots()
ax.scatter(x, y, color='b', label='Dati')
# Aggiunta di etichette
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Aggiunta della legenda
ax.legend()

# Aggiunta del titolo
ax.set_title('Varianza e Covarianza')

# Aggiunta delle informazioni sulla varianza e la covarianza
ax.text(1, 7, f'Varianza X: {varianza_x:.2f}', fontsize=8)
ax.text(1, 6.5, f'Varianza Y: {varianza_y:.2f}', fontsize=8)
ax.text(1, 6, f'Covarianza: {covarianza:.2f}', fontsize=8)

# Mostra il grafico
plt.show()

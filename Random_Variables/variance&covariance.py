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

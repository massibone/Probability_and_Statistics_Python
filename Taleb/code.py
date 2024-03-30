
'''
due insiemi di dati casuali in uno spazio tridimensionale, uno con code sottili e l'altro con code spesse. Successivamente, visualizza i dati generati in due grafici tridimensionali separati per mostrare la differenza nella distribuzione dei dati intorno al centro tra code sottili e spesse
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generazione di dati casuali con code sottili e spesse
np.random.seed(42)
mean = [0, 0, 0]
cov_thin = np.eye(3) * 0.5  # Covarianza per code sottili
cov_thick = np.eye(3) * 2.0  # Covarianza per code spesse

data_thin = np.random.multivariate_normal(mean, cov_thin, 1000)
data_thick = np.random.multivariate_normal(mean, cov_thick, 1000)

# Creazione del grafico tridimensionale
fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(data_thin[:, 0], data_thin[:, 1], data_thin[:, 2], c='b', alpha=0.5)
ax1.set_title('Code Sottili')

ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(data_thick[:, 0], data_thick[:, 1], data_thick[:, 2], c='r', alpha=0.5)
ax2.set_title('Code Spesse')

plt.show()

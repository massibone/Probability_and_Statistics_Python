import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import genpareto

# Genera dati da una distribuzione di coda grassa (Pareto)
np.random.seed(0)
data = genpareto.rvs(c=0.5, loc=0, scale=1, size=1000)

# Calcola i valori massimi estratti
max_values = np.maximum.accumulate(data)

# Adatta una distribuzione di Pareto ai valori massimi
params = genpareto.fit(max_values, floc=0)

# Crea una griglia di valori per il plot della distribuzione di Pareto
x = np.linspace(0, np.max(max_values), 100)
pdf_fitted = genpareto.pdf(x, *params)

# Plotta un istogramma dei valori massimi e la distribuzione di Pareto adattata
plt.figure(figsize=(10, 6))
plt.hist(max_values, bins=30, density=True, alpha=0.7, label='Histogram of Max Values')
plt.plot(x, pdf_fitted, 'r-', lw=2, label='Fitted Pareto Distribution')
plt.title('Extreme Value Analysis with Pareto Distribution')
plt.xlabel('Max Values')
plt.ylabel('Density')
plt.legend()
plt.show()

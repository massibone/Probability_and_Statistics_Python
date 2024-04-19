'''
EVT per adattare una distribuzione di coda grassa (Pareto) ai dati simulati e plottare i risultati. 
'''


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import genpareto

# Simulazione e Adattamento della Distribuzione con Extreme Value Theory (EVT)

# Passo 1: Generazione dei dati da una distribuzione di coda grassa (Pareto)
np.random.seed(0)  # Impostiamo il seed per la riproducibilità
data = genpareto.rvs(c=0.5, loc=0, scale=1, size=1000)  # Genera dati da una distribuzione di Pareto

# Passo 2: Applicazione dell'Extreme Value Theory (EVT) per adattare la distribuzione dei valori massimi
max_values = []
sample_size = 100  # Dimensione del campione per selezionare i massimi
num_samples = 1000  # Numero di campioni per calcolare i valori massimi

for _ in range(num_samples):
    sample = np.random.choice(data, size=sample_size, replace=True)  # Seleziona casualmente un campione
    max_value = np.max(sample)  # Trova il valore massimo nel campione
    max_values.append(max_value)  # Aggiungi il valore massimo alla lista dei valori massimi

# Passo 3: Plottaggio dei risultati
plt.figure(figsize=(10, 6))
plt.hist(max_values, bins=30, density=True, alpha=0.5, color='b', label='Max Values')  # Istogramma dei valori massimi

# Adattamento della distribuzione di Pareto utilizzando i valori massimi
params = genpareto.fit(max_values)  # Adatta una distribuzione di Pareto ai valori massimi
x = np.linspace(np.min(max_values), np.max(max_values), 100)  # Crea un array di valori per il plot della PDF
pdf_fitted = genpareto.pdf(x, *params)  # Calcola la PDF della distribuzione di Pareto adattata
plt.plot(x, pdf_fitted, 'r-', lw=2, label='Fitted Pareto Distribution')  # Plotta la PDF adattata

# Personalizzazione del grafico
plt.title('Extreme Value Theory (EVT) - Fitted Pareto Distribution')
plt.xlabel('Max Values')
plt.ylabel('Density')
plt.legend()
plt.grid(True)

# Mostra il grafico
plt.show()

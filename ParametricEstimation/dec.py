import numpy as np
import matplotlib.pyplot as plt

# Parametro della distribuzione esponenziale (tasso di decadimento)
tasso_decadimento = 0.5  # Un valore a caso per l'esempio
# Genera 1000 campioni dalla distribuzione esponenziale
num_campioni = 1000
tempi_attesa = np.random.exponential(scale=1/tasso_decadimento, size=num_campioni)

# Plot dell'istogramma dei tempi di attesa
plt.hist(tempi_attesa, bins=30, density=True, alpha=0.7, color='b')

# Calcola la funzione di densità di probabilità della distribuzione esponenziale
x = np.linspace(0, max(tempi_attesa), 100)
pdf = tasso_decadimento * np.exp(-tasso_decadimento * x)
plt.plot(x, pdf, 'r-', lw=2, label='PDF')

plt.xlabel('Tempo di attesa')
plt.ylabel('Densità di probabilità')
plt.title('Distribuzione Esponenziale (Tempi di Attesa)')
plt.legend()

plt.show()

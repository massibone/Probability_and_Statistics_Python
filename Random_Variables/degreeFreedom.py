'''
I gradi di libertà di una variabile aleatoria o di una statistica in genere esprimono il numero minimo di dati sufficienti a valutare la quantità d'informazione contenuta nella statistica. Infatti, quando un dato non è indipendente, l'informazione che esso fornisce è già contenuta implicitamente negli altr

'''


import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

# Gradi di libertà per la distribuzione t di Student
degrees_of_freedom = [1, 3, 10, 30]

# Generazione dei valori possibili per la variabile casuale
x = np.linspace(-5, 5, 1000)

# Creazione del grafico
for df in degrees_of_freedom:
    pdf = t.pdf(x, df)
    plt.plot(x, pdf, label=f'Gradi di Libertà = {df}')

plt.xlabel('Valore')
plt.ylabel('Densità di Probabilità')
plt.title('Densità di Probabilità per Distribuzione t di Student')
plt.legend()
plt.grid(True)

# Visualizzazione del grafico
plt.show()


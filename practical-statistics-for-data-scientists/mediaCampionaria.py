'''
Immagina di avere una grande collezione di conchiglie di mare. 
Ogni volta che prendi un piccolo gruppo di conchiglie e ne calcoli la media delle dimensioni, stai essenzialmente facendo quello che il teorema del limite centrale descrive. 
Anche se i tuoi piccoli gruppi di conchiglie potrebbero variare, se prendi abbastanza gruppi e calcoli le loro medie, alla fine assomiglieranno a una forma a campana come una montagna rotonda. 
È come se ogni gruppo di conchiglie contribuisse un pezzo alla forma della montagna.
'''
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generazione di un esempio di distribuzione non normale
data = np.random.exponential(scale=2, size=1000)

# Calcolo della media di 1000 campioni di dimensione 30
sample_means = [np.mean(np.random.choice(data, size=30)) for _ in range(1000)]

# Creazione del grafico
sns.histplot(sample_means, kde=True)
plt.xlabel('Media dei campioni')
plt.ylabel('Conteggio')
plt.title('Distribuzione delle medie campionarie')
plt.show()

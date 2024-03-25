'''
il tasso di convergenza di una distribuzione Student T alla zona gaussiana. 
Si evidenzia che la convergenza dell'indice κ a 0 sotto sommatoria è di 1/log(n). 
Viene menzionata la forma semi-chiusa per la densità di una distribuzione Student cubica sommata n volte. Inoltre, 
si parla dell'approccio di Bouchaud e Potters che separa la "zona gaussiana" dalla "zona Power Law" nelle code della distribuzione. 
Si sottolinea che il passaggio tra le due zone avviene a una velocità molto lenta. 
Infine, si menziona l'interesse per la convergenza della Pareto a una distribuzione Levy-Stable, che finora è stata ottenuta solo numericamente.
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import levy_stable

# Genera 100 dati da una distribuzione di Pareto
alpha_pareto = 3
samples_pareto = np.random.pareto(alpha_pareto, 100)

# Genera 100 dati da una distribuzione stabile
alpha_stable = 1.7
samples_stable = levy_stable.rvs(alpha_stable, size=100)

# Crea un grafico a istogramma per confrontare le due distribuzioni
plt.figure(figsize=(10, 5))

plt.hist(samples_pareto, bins=20, color='skyblue', edgecolor='black', alpha=0.7, label='Pareto')
plt.hist(samples_stable, bins=20, color='salmon', edgecolor='black', alpha=0.7, label='Stabile')
plt.legend()

plt.title('Confronto tra Distribuzione di Pareto e Stabile')
plt.xlabel('Valore')
plt.ylabel('Frequenza')

plt.show()

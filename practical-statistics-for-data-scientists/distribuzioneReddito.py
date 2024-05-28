'''
Nel campo della statistica, è importante distinguere tra la media di un campione (indicata con x-bar) e la media di una popolazione (indicata con μ). 
Questa distinzione è cruciale perché le informazioni sui campioni sono osservate direttamente, 
mentre le informazioni sulle grandi popolazioni spesso vengono dedotte da campioni più piccoli. 
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creazione di un DataFrame per i dati di esempio
loans_income = pd.Series([20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000])
# campione di 1000 prestiti
sample_data = pd.DataFrame({'income': loans_income.sample(1000), 'type': 'Data'})
# campione di medie di 5 valori
sample_mean_05 = pd.DataFrame({'income': [loans_income.sample(5).mean() for _ in range(1000)], 'type': 'Media di 5'})
# campione di medie di 20 valori
sample_mean_20 = pd.DataFrame({'income': [loans_income.sample(20).mean() for _ in range(1000)], 'type': 'Media di 20'})
# Unione dei DataFrame
results = pd.concat([sample_data, sample_mean_05, sample_mean_20])

# Creazione dei grafici usando FacetGrid
g = sns.FacetGrid(results, col='type', col_wrap=1, height=4, aspect=2)
g.map(plt.hist, 'income', range=[0, 200000], bins=40)
g.set_axis_labels('Reddito', 'Conteggio')
g.set_titles('{col_name}')
plt.show()

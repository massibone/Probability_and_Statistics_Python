import numpy as np

# Generiamo un set di dati di esempio rappresentante il numero di caramelle di diversi tipi nel mucchio
np.random.seed(0)
caramelle = np.random.randint(1, 100, size=100)  # Genera 100 caramelle con valori casuali da 1 a 100

# Stampiamo i dati di esempio
print("Dati delle caramelle:")
print(caramelle)
from scipy.stats import genpareto

# Applichiamo la teoria dei valori estremi per analizzare la coda della distribuzione
# Troviamo una soglia (threshold) oltre la quale consideriamo i valori come estremi
threshold = np.percentile(caramelle, 95)  # Soglia del 95-esimo percentile

# Selezioniamo solo i valori delle caramelle che superano la soglia
caramelle_estreme = caramelle[caramelle > threshold]

# Fittiamo una distribuzione di Pareto Generalizzata (GPD) ai valori estremi
loc, scale = genpareto.fit(caramelle_estreme)

# Stampa dei parametri stimati della distribuzione di Pareto Generalizzata (GPD)
print("\nParametri della distribuzione GPD:")
print(f"Location (loc): {loc}")
print(f"Scale (scale): {scale}")

# Calcoliamo il numero totale di caramelle stimato utilizzando la distribuzione GPD
num_caramelle_totale = genpareto.cdf(max(caramelle), loc=loc, scale=scale)
num_caramelle_totale_stimato = int(len(caramelle) / (1 - num_caramelle_totale))

# Stampa del numero totale di caramelle stimato
print("\nNumero totale di caramelle stimato utilizzando la distribuzione GPD:")
print(num_caramelle_totale_stimato)
# Calcoliamo il numero stimato di tipi di caramelle nel mucchio
# (utilizzando la distribuzione GPD e considerando la probabilità di superamento della soglia)
num_tipi_caramelle_stimato = genpareto.sf(threshold, loc=loc, scale=scale) * num_caramelle_totale_stimato

# Stampa del numero stimato di tipi di caramelle nel mucchio
print("\nNumero stimato di tipi di caramelle nel mucchio:")
print(int(num_tipi_caramelle_stimato))


'''
Nel primo passo, abbiamo generato un insieme di dati simulati rappresentanti il numero di caramelle di diversi tipi nel mucchio.
Nel secondo passo, abbiamo applicato la teoria dei valori estremi per analizzare la coda della distribuzione dei dati e stimare il numero totale di caramelle nel mucchio utilizzando una distribuzione di Pareto Generalizzata (GPD).
Nel terzo passo, abbiamo utilizzato le informazioni della distribuzione GPD per stimare il numero totale di tipi di caramelle nel mucchio.
In questo esempio, la teoria dei valori estremi ci ha permesso di estrarre informazioni utili sui dati delle caramelle, inclusa una stima del numero totale di caramelle nel mucchio e del numero totale di tipi di caramelle presenti. Questo tipo di analisi può essere estremamente utile per comprendere meglio la distribuzione e la varietà dei dati disponibili.
'''
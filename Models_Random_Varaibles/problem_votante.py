'''
Se un votante scelto a caso è favorevole ad una certa riforma con probbabilità 0.7,qual'è la probabilità che su 10 votanti esattamente 7 siano favorevoli?

ogni votante ha una probabilità di successo p = 0.7 di essere favorevole alla riforma. Per calcolare la probabilità che esattamente 7 votanti su 10 siano favorevoli, possiamo utilizzare la formula della funzione di massa di probabilità (PMF) della distribuzione binomiale.

La formula della PMF della distribuzione binomiale è:

P(X = k) = C(n, k) * p^k * (1-p)^(n-k)
'''
from scipy.stats import binom

p = 0.7  # Probabilità di successo
n = 10   # Numero totale di votanti
k = 7    # Numero di votanti favorevoli desiderato

# Calcolo della probabilità utilizzando la distribuzione binomiale
probability = binom.pmf(k, n, p)

print("La probabilità che su 10 votanti esattamente 7 siano favorevoli è:", probability)
#La probabilità che su 10 votanti esattamente 7 siano favorevoli è: 0.26682793200000005

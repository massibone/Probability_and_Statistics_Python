'''
Immagina di avere diversi gruppi di piante in un campo e stai cercando di capire se un certo fertilizzante fa crescere le piante meglio di un altro. La distribuzione F è come una misura che ci dice se le differenze tra i gruppi di piante sono grandi rispetto alle differenze che ci aspetteremmo solo per caso. Se la differenza è grande, la distribuzione F ci darà un valore alto.
'''
import numpy as np
from scipy.stats import poisson

# Generare 100 numeri casuali da una distribuzione di Poisson con lambda = 2
random_numbers = poisson.rvs(2, size=100)

print("Numeri casuali generati:", random_numbers)

'''
Questo codice genererà 100 numeri casuali da una distribuzione di Poisson con un valore medio di 2. Ad esempio, se in media arrivano due chiamate al minuto, questo codice simulerà 100 minuti restituendo il numero di chiamate in ciascuno di quei 100 minuti.
'''

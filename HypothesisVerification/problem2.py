'''
Due campioni seguenti provengono da popolazioni di Poisson di media λ1 e λ2. verifica l'ipotesi λ1=λ2
campione1 24 32 29 33 40 28 34 36 
campione2 42 36 41

Per verificare se le medie dei due campioni provengono da popolazioni di Poisson con lo stesso parametro λ (ovvero λ1 = λ2), 
possiamo utilizzare il test di Kolmogorov-Smirnov. Questo test viene utilizzato per confrontare due distribuzioni empiriche e 
determinare se possono essere considerate provenienti dalla stessa distribuzione.

Nel nostro caso, possiamo considerare λ1 e λ2 come le medie dei due campioni. Pertanto, la nostra ipotesi nulla sarà "λ1 = λ2," 
e vogliamo verificare se possiamo rifiutare questa ipotesi.

Il test di Kolmogorov-Smirnov restituirà un valore p (p-value) che rappresenta 
la probabilità che i due campioni provengano da popolazioni con la stessa distribuzione. 
Se il p-value è maggiore del livello di significatività (in questo caso, 0.05), 
non avremo sufficienti evidenze per rifiutare l'ipotesi che λ1 = λ2. Al contrario, 
se il p-value è inferiore al livello di significatività, 
possiamo rifiutare l'ipotesi e concludere che i due campioni provengono da popolazioni con parametri λ diversi.





import numpy as np
from scipy.stats import ks_2samp

# Dati dei campioni
campione1 = np.array([24, 32, 29, 33, 40, 28, 34, 36])
campione2 = np.array([42, 36, 41])

# Calcolo delle medie dei campioni
media_campione1 = np.mean(campione1)
media_campione2 = np.mean(campione2)

# Test di Kolmogorov-Smirnov
statistiche, p_value = ks_2samp(campione1, campione2)

# Livello di significatività
livello_significatività = 0.05

# Stampa dei risultati
print(f"Media campione 1: {media_campione1}")
print(f"Media campione 2: {media_campione2}")
print(f"Test di Kolmogorov-Smirnov: statistiche = {statistiche}, p-value = {p_value}")

if p_value > livello_significatività:
    print("Non ci sono evidenze sufficienti per rifiutare l'ipotesi che λ1 = λ2.")
else:
    print("Possiamo rifiutare l'ipotesi che λ1 = λ2; i due campioni provengono da popolazioni con parametri λ diversi.")

'''
Media campione 1: 32.0
Media campione 2: 39.666666666666664
Test di Kolmogorov-Smirnov: statistiche = 0.75, p-value = 0.1212121212121212     
Non ci sono evidenze sufficienti per rifiutare l'ipotesi che λ1 = λ2.
'''

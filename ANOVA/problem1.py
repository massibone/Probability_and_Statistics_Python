'''Si scelgono 20 persone sovrappeso e ciascuno viene sottoposto a dieta.Dopo 10 settimane le diminuzioni di peso sono state
dieta1  22.2 23.4 24.2 16.1 9.4 12.5 18.6 32.2 8.8 7.6
dieta2 24.2 16.8 14.6 13.7 19.5 17.6 11.2 9.5 30.1 21.5
Verifica al 5% di significatività l'ipotesi che le due diete abbiano uguale effetto.

possiamo utilizzare un test di confronto tra due medie noto come "t-test" per campioni indipendenti. Poiché si tratta di un test bilaterale e la dimensione del campione è piccola, useremo il t-test per campioni indipendenti con un livello di significatività del 5%.

'''
import numpy as np
from scipy.stats import ttest_ind

# Dati delle due diete
dieta1 = np.array([22.2, 23.4, 24.2, 16.1, 9.4, 12.5, 18.6, 32.2, 8.8, 7.6])
dieta2 = np.array([24.2, 16.8, 14.6, 13.7, 19.5, 17.6, 11.2, 9.5, 30.1, 21.5])

# Test t per campioni indipendenti
t_statistic, p_value = ttest_ind(dieta1, dieta2)

# Stampa i risultati
print("Valore della statistica t:", t_statistic)
print("Valore di p:", p_value)

# Verifica dell'ipotesi
alpha = 0.05
if p_value < alpha:
    print("L'ipotesi di uguale effetto delle due diete può essere rigettata.")
else:
    print("L'ipotesi di uguale effetto delle due diete non può essere rigettata.")
#Valore della statistica t: -0.11481305460610226
#Valore di p: 0.9098643582478192
#L'ipotesi di uguale effetto delle due diete non può essere rigettata.

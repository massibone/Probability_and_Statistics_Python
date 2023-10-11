'''
abbiamo due produttori da scegliere. li sottoponiamo a 8 problemi di calcolo e misura dei tempi necessari ai 2 calcolatori per risolverli
Problema  1      2     3     4     5    6    7     8
sistemaA  15   32   17   26   42 29 12   38
sistemaB  22  29   1     23    46 25  19  47
Determina il p-dei-dati del test e l'ipotesi nulla che nn vi siano differenze.
Per verificare se ci sono differenze significative tra i due produttori, possiamo utilizzare un test statistico chiamato test t per campioni indipendenti. In questo caso, il test t ci aiuterà a confrontare i tempi necessari per risolvere i problemi nei due sistemi.

'''
import numpy as np
from scipy.stats import ttest_ind

# Tempi necessari ai due produttori per risolvere i problemi
sistemaA = np.array([15, 32, 17, 26, 42, 29, 12, 38])
sistemaB = np.array([22, 29, 1, 23, 46, 25, 19, 47])

# Test t per campioni indipendenti
t_statistic, p_value = ttest_ind(sistemaA, sistemaB)

# Stampa i risultati
print("Valore della statistica t:", t_statistic)
print("Valore di p:", p_value)

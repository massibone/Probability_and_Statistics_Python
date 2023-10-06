# regressione attraverso l'origine

import numpy as np
import statsmodels.api as sm

# Dati forniti
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2, 4, 6, 8, 10])

# Esecuzione della regressione lineare attraverso l'origine
model = sm.OLS(y_data, x_data).fit()

# Ottenere il coefficiente di regressione
slope = model.params[0]

# Stampa del risultato
print(f"Coefficiente di regressione (pendenza): {slope:.2f}")

#RISULTATO Coefficiente di regressione (pendenza): 2.00

'''
In questo esempio, poiché abbiamo eseguito la regressione attraverso l'origine, il modello ottenuto è una retta senza il termine costante. Il coefficiente di regressione (pendenza) sarà semplicemente la relazione tra le variabili "x" e "y" senza alcun termine aggiuntivo.

Nell'esempio sopra, il coefficiente di regressione (pendenza) sarà 2. Questo indica che la relazione tra le variabili "x" e "y" è lineare e che il valore di "y" è sempre il doppio del valore di "x" (in quanto la retta passa attraverso l'origine).
'''

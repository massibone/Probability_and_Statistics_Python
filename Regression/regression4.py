'''
abella numero fusti trasportati in un container risultati danneggiati rispetto alla velocità di consegna
velocità              3 3 3 5 5 5 6 7 7 8
danneggiati    54 62 65 94 122 84 142 139 184 254
a)analizza dati con modello regressione lineare
b) disegna grafico dei residui standardizzati
c) da risultato di b) risulta qualche difetto nel modello?
d) se c) positiva,individua un modello migliore e stima i parametri corrispondenti

Dopo aver eseguito il codice, vedrai i risultati della regressione lineare, inclusi i coefficienti di regressione (pendenza e termine costante) e i p-values associati. Il grafico dei residui standardizzati mostrerà la distribuzione dei residui standardizzati intorno alla linea zero orizzontale.

Osservando il grafico dei residui standardizzati, esamina se i punti sono distribuiti casualmente intorno allo zero o se mostrano una struttura sistematica. Se i punti mostrano una struttura sistematica, potrebbe indicare che il modello di regressione lineare non è adeguato per spiegare la relazione tra le variabili.

Se il modello mostra dei difetti e i residui non hanno una distribuzione casuale intorno allo zero, potresti considerare un modello di regressione non lineare o includere altre variabili esplicative per migliorare la capacità predittiva del modello. Potresti anche esaminare se la relazione tra le variabili potrebbe essere meglio rappresentata da un modello polinomiale o da altre forme funzionali più complesse. In questo caso, dovresti valutare diversi modelli e scegliere quello che meglio si adatta ai dati.







'''


import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Dati forniti
velocita = np.array([3, 3, 3, 5, 5, 5, 6, 7, 7, 8])
danneggiati = np.array([54, 62, 65, 94, 122, 84, 142, 139, 184, 254])

# Esecuzione della regressione lineare
X = sm.add_constant(velocita)  # Aggiunta di una colonna di 1 per il termine costante
model = sm.OLS(danneggiati, X).fit()

# Ottenere i coefficienti di regressione
slope, intercept = model.params

# a) Risultato della regressione lineare
print("Risultati della regressione lineare:")
print(model.summary())

# b) Calcolo dei residui standardizzati
standardized_residuals = model.get_influence().resid_studentized_internal

# c) Grafico dei residui standardizzati
plt.scatter(velocita, standardized_residuals, color='b')
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Velocità di consegna')
plt.ylabel('Residui standardizzati')
plt.title('Grafico dei residui standardizzati')
plt.grid(True)
plt.show()

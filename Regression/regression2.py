import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Dati forniti
stature = np.array([64, 65, 66, 67, 69, 70, 72, 72, 74, 74, 75, 76])
incomes = np.array([91, 94, 88, 103, 77, 96, 105, 88, 122, 102, 90, 114])

# Aggiunta di una colonna di 1 per il calcolo del termine costante nell'equazione di regressione
X = sm.add_constant(stature)

# Esecuzione della regressione lineare
model = sm.OLS(incomes, X).fit()

# Ottenere i coefficienti della regressione e i p-values associati
coefficients = model.params
p_values = model.pvalues

# Visualizzazione dei risultati
print("Risultati della regressione:")
print(model.summary())

# Grafico di dispersione con retta di regressione
plt.scatter(stature, incomes, color='b', label='Dati')
plt.plot(stature, coefficients[0] + coefficients[1] * stature, color='r', label='Retta di regressione')
plt.xlabel('Statura (pollici)')
plt.ylabel('Reddito (migliaia di euro)')
plt.title('Diagramma di dispersione con retta di regressione')
plt.legend()
plt.grid(True)
plt.show()

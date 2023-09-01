'''
Per calcolare il tempo di vita medio di una variabile aleatoria X con la funzione di densità data, possiamo calcolare l'aspettativa matematica di X. L'aspettativa matematica (o valore atteso) di una variabile aleatoria X con densità di probabilità f(x) è definita come:

E[X] = ∫(x * f(x)) dx

Nel caso specifico della funzione di densità data f(x) = a^2x * e^(-ax), con x >= 0, possiamo calcolare l'aspettativa matematica come:

E[X] = ∫(x * a^2x * e^(-ax)) dx


'''

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definizione della variabile simbolica x e dei parametri della funzione di densità
x, a = sp.symbols('x a')
density_func = a**2 * x * sp.exp(-a*x)

# Calcolo dell'aspettativa matematica
mean_value = sp.integrate(x * density_func, (x, 0, sp.oo))

# Conversione dell'espressione simbolica in una funzione numpy
mean_value_func = sp.lambdify(a, mean_value)

# Range di valori per il parametro a
a_values = np.linspace(0.01, 5, 100)

# Calcolo del tempo di vita medio per ogni valore di a
mean_values = [mean_value_func(a_val) for a_val in a_values]

# Creazione del grafico
plt.plot(a_values, mean_values)
plt.xlabel('a')
plt.ylabel('Tempo di vita medio')
plt.title('Tempo di vita medio in funzione di a')
plt.grid(True)
plt.show()

import numpy as np

# Insiemi di dati A e B
data_A = [3, 4, 6, 7, 10]
data_B = [-20, 5, 15, 24]

# Calcolo della varianza campionaria per A
variance_A = np.var(data_A, ddof=1)

# Calcolo della varianza campionaria per B
variance_B = np.var(data_B, ddof=1)

# Stampa della varianza campionaria per A e B
print("Varianza campionaria di A:", variance_A)
print("Varianza campionaria di B:", variance_B)

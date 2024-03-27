'''
In questo codice, vengono definiti i cumulanti di ordine 1, 2 e 3 per la variabile casuale X1. Successivamente, vengono calcolati i cumulanti corrispondenti alla somma delle n copie identiche di X1 utilizzando la relazione K_ni = n * K_i(X1).
'''
import numpy as np

# Definizione dei cumulanti per la variabile casuale X1
K_1_X1 = 2  # Esempio di cumulante di ordine 1 per X1
K_2_X1 = 5  # Esempio di cumulante di ordine 2 per X1
K_3_X1 = 10  # Esempio di cumulante di ordine 3 per X1

# Numero di copie identiche della variabile casuale Xi
n = 4

# Calcolo dei cumulanti per la somma delle n copie identiche
K_n1 = n * K_1_X1
K_n2 = n * K_2_X1
K_n3 = n * K_3_X1

print(f"Cumulanti per la somma delle {n} copie identiche:")
print(f"K_{n}1: {K_n1}")
print(f"K_{n}2: {K_n2}")
print(f"K_{n}3: {K_n3}")
-varianzeElevate.py
'''
per varianze elevate, il tasso di convergenza κ1,n si avvicina a 1
'''
import numpy as np

# Definizione delle costanti e parametri
n = 5
sigma = 10

# Calcolo del tasso di convergenza κ1,n per σ → ∞
M_1 = 2  # Deviazione media assoluta per n=1
M_n = n  # Deviazione media assoluta per n copie identiche

kappa_1_n = M_n / M_1

print(f"Tasso di convergenza κ1,n per σ → ∞: {kappa_1_n}")

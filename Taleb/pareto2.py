'''
Immagina di avere una scatola di giocattoli con vari tipi di pupazzi e oggetti divertenti. 
Ogni tipo di giocattolo rappresenta una "variabile" diversa, 
come i punteggi dei tuoi giochi preferiti.

Ora, se prendi più giocattoli dello stesso tipo e li sommi insieme, 
ottieni un nuovo giocattolo che è la somma di tutti quelli precedenti! 
Questo nuovo giocattolo ha delle caratteristiche diverse, come il colore o la grandezza.

Nella matematica delle distribuzioni, facciamo qualcosa di simile. 
Prendiamo più "variabili" (o giocattoli) che seguono una certa legge di distribuzione, 
come la distribuzione di Pareto, e le sommiamo insieme. 
Alla fine, otteniamo una nuova distribuzione 
che ha caratteristiche diverse rispetto alle distribuzioni originali.
'''

import numpy as np
import matplotlib.pyplot as plt

# Creiamo una distribuzione di Pareto
def pareto_distribution(alpha, xmin, size):
    return xmin * (1 - np.random.uniform(size=size)) ** (-1 / alpha)

# Definiamo il numero di variabili da sommare
n_variables = 1000

# Parametri della distribuzione di Pareto
alpha = 1.5  # Esponente della coda lunga
xmin = 1.0   # Valore minimo della distribuzione di Pareto

# Generiamo n_variables variabili seguendo la distribuzione di Pareto
variables = pareto_distribution(alpha, xmin, n_variables)

# Calcoliamo la somma normalizzata delle variabili
normalized_sum = np.sum(variables) / n_variables

# Plot della distribuzione delle variabili originali e della somma normalizzata
plt.figure(figsize=(10, 6))

# Istogramma delle variabili originali
plt.hist(variables, bins=50, density=True, alpha=0.7, label='Variabili di Pareto')

# Linea verticale per la somma normalizzata
plt.axvline(normalized_sum, color='r', linestyle='--', linewidth=2, label='Somma normalizzata')

plt.title('Somma di variabili di Pareto')
plt.xlabel('Valore')
plt.ylabel('Densità')
plt.legend()
plt.grid(True)
plt.show()

# Stampiamo il risultato della somma normalizzata
print(f"La somma normalizzata delle variabili di Pareto è: {normalized_sum:.2f}")

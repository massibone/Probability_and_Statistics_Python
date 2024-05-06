import math

# Funzione per calcolare l'approssimazione dell'aspettativa E(X) per una distribuzione power law
def calcola_aspettativa_alpha(alpha):
    # Costante k
    k = 1.0  # Possiamo scegliere qualsiasi valore positivo per k
    
    # Calcolo di nu(alpha) approssimato
    nu_alpha = alpha * (1 + math.log(4)) / math.pi
    
    # Calcolo approssimativo di E(X)
    aspettativa = k / (nu_alpha * (alpha - 1))
    
    return aspettativa

import math

# Funzione per calcolare l'approssimazione dell'aspettativa E(X) per una distribuzione power law
def calcola_aspettativa_alpha(alpha):
    # Costante k
    k = 1.0  # Possiamo scegliere qualsiasi valore positivo per k
    
    # Calcolo di nu(alpha) approssimato
    nu_alpha = alpha * (1 + math.log(4)) / math.pi
    
    # Calcolo approssimativo di E(X)
    aspettativa = k / (nu_alpha * (alpha - 1))
    
    return aspettativa

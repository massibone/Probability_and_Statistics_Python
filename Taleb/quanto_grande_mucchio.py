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

# Esempio di utilizzo della funzione per alpha = 2
alpha = 2
aspettativa = calcola_aspettativa_alpha(alpha)
print(f"Approssimazione dell'aspettativa E(X) per alpha = {alpha}: {aspettativa}")
'''
Quando calcoliamo l'approssimazione dell'aspettativa 

E(X) per una distribuzione power law con 
α=2, otteniamo il valore approssimativo di 
0.6582575697231753
E(X)=0.6582575697231753.

Immagina che 
α rappresenti la forma del mucchio di giocattoli. Una distribuzione con 

α=2 ha una forma particolare: la coda della distribuzione (la parte estesa verso valori più alti) scende più rapidamente rispetto ad altre distribuzioni. Questo significa che nel mucchio di giocattoli, ci sono più piccoli mucchietti concentrati verso l'inizio, e pochi giocattoli che si estendono molto lontano.

Il valore di 0.6582575697231753
E(X)=0.6582575697231753 rappresenta una stima approssimativa della taglia media di un giocattolo nel mucchio. Quindi, se prendessimo un giocattolo a caso da questo mucchio, ci aspetteremmo che sia di dimensioni intorno a questo numero.


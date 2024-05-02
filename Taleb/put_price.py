'''
Immagina che il prezzo iniziale sia 100 e scende a 90. La differenza è 10, e ci interessa solo questa differenza.

Per fare calcoli su quanto scenderà il prezzo, usiamo alcuni numeri speciali chiamati "rate of return" e "Pareto distribution". 
Sono come regole che ci aiutano a capire quanto potrebbe scendere il prezzo. 
Usando queste regole, possiamo calcolare quanto potrebbe costare scommettere su un certo prezzo basso.
'''
def calculate_put_price(K1, K2, S0, alpha):
    # Calcola il prezzo dell'opzione put utilizzando la formula data
    P = ((K2 - S0) / ((1 - alpha) * S0)) ** (1 - alpha) - ((K1 - S0) / ((1 - alpha) * S0)) ** (1 - alpha)
    P *= ((alpha - 1) * K2 + S0) / ((alpha - 1) * K1 + S0)
    return P

# Parametri di esempio
K1 = 90  # Prezzo di esercizio inferiore
K2 = 80  # Prezzo di esercizio superiore
S0 = 100  # Prezzo iniziale
alpha = 0.5  # Parametro alpha per la distribuzione di Pareto

# Calcola il prezzo dell'opzione put
put_price = calculate_put_price(K1, K2, S0, alpha)
print("Il prezzo dell'opzione put è:", put_price)

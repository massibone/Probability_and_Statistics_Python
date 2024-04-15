import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione di trasformazione logaritmica
def log_transformation(data, L, H):
    # Applicazione della trasformazione logaritmica
    transformed_data = L - H * np.log((H - data) / (H - L))
    return transformed_data

# Generazione di dati casuali con coda pesante
np.random.seed(0)
data = np.random.exponential(scale=10, size=1000)  # Dati con distribuzione esponenziale (coda pesante)

# Parametri della trasformazione logaritmica
L = 0.1  # Limite inferiore
H = 1000  # Limite superiore (assumiamo un valore molto grande)

# Applicazione della trasformazione logaritmica ai dati
transformed_data = log_transformation(data, L, H)

# Plot dei dati originali e dei dati trasformati
plt.figure(figsize=(10, 6))

# Dati originali
plt.subplot(2, 1, 1)
plt.hist(data, bins=50, color='skyblue', edgecolor='black')
plt.title('Dati Originali')
plt.xlabel('Valore')
plt.ylabel('Frequenza')

# Dati trasformati
plt.subplot(2, 1, 2)
plt.hist(transformed_data, bins=50, color='salmon', edgecolor='black')
plt.title('Dati Trasformati (Trasformazione Logaritmica)')
plt.xlabel('Valore Trasformato')
plt.ylabel('Frequenza')

plt.tight_layout()
plt.show()
'''
Immaginiamo di avere due modi di guardare un mucchio di caramelle: da lontano e da vicino. La trasformazione logaritmica qui serve a illustrare come cambia la nostra percezione della distribuzione delle caramelle quando ci avviciniamo al limite superiore del mucchio, che potrebbe essere molto grande.

Grafico dei dati originali (Dati "da lontano"):

Questo grafico rappresenta la distribuzione delle caramelle quando le guardiamo da lontano, senza vedere il limite superiore del mucchio (H).
Le caramelle sono distribuite in base a una certa distribuzione, che possiamo assumere come una distribuzione uniforme o normale, rappresentata dall'istogramma.
L'asse delle ascisse (x) mostra i diversi tipi di caramelle o i loro valori.
L'asse delle ordinate (y) mostra quante caramelle di quel tipo sono presenti nel mucchio.
Grafico dei dati trasformati (Dati "da vicino"):

Questo grafico rappresenta la distribuzione delle caramelle quando ci avviciniamo al limite superiore del mucchio (H), utilizzando la trasformazione logaritmica.
La trasformazione logaritmica modifica la distribuzione originale delle caramelle in modo da farci vedere più chiaramente la coda estrema delle caramelle vicino al limite superiore.
L'asse delle ascisse (x) mostra i valori trasformati delle caramelle, che sono risultato della trasformazione logaritmica.
L'asse delle ordinate (y) mostra quante caramelle trasformate sono presenti in ciascun intervallo di valori trasformati.
'''
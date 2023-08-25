import matplotlib.pyplot as plt
import numpy as np

def expected_games_played(p):
    return 1/p

# Range di valori per P
p_values = np.linspace(0.01, 0.99, 100)

# Calcolo del numero medio di partite disputate per ogni valore di P
expected_values = [expected_games_played(p) for p in p_values]

# Creazione del grafico
plt.plot(p_values, expected_values)
plt.xlabel('P')
plt.ylabel('Numero medio di partite disputate')
plt.title('Numero medio di partite disputate in funzione di P')
plt.grid(True)
plt.show()

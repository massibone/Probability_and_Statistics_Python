'''
Effetto dell’aumento di ( p ): La figura illustra come l’aumento del valore di ( p ), che rappresenta l’ordine del momento, influisce sulla forma delle iso-norme.
Iso-norme: Le iso-norme sono curve che rappresentano i punti nello spazio delle variabili aleatorie che hanno la stessa norma, o lo stesso livello di “rischio” o “variabilità” in un certo senso statistico.
Questa sezione sembra discutere l’importanza di considerare diverse misure di rischio e come la scelta della norma può influenzare l’analisi statistica, specialmente quando si tratta di distribuzioni con code pesanti o “fat tails”.
'''
import numpy as np
import matplotlib.pyplot as plt

# Genera un campione di dati bidimensionali
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)

# Calcola le iso-norme per diversi valori di p
p_values = [0.5, 1, 2, 4]
for p in p_values:
    Z = (np.abs(X)**p + np.abs(Y)**p)**(1/p)
    plt.contour(X, Y, Z, levels=10, cmap='viridis')

plt.title('Confronto delle iso-norme per diversi valori di p')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(label='Norma')
plt.show()
'''
 la forma delle iso-norme cambia da circolare (norma euclidea) a una forma più squadrata man mano che ( p ) aumenta.
'''

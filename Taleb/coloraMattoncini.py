import numpy as np
import matplotlib.pyplot as plt

# Definiamo una funzione per simulare il processo di colorazione dei mattoncini
def simula_colorazione(num_mattoncini):
    mattoncini = np.random.randint(2, size=num_mattoncini)  # 0 rappresenta un mattoncino non rosso, 1 rappresenta un mattoncino rosso
    return mattoncini

# Definiamo il numero di mattoncini nel nostro esperimento
num_mattoncini = 1000

# Simuliamo il processo di colorazione dei mattoncini
mattoncini_colorati = simula_colorazione(num_mattoncini)

# Calcoliamo la frazione di mattoncini rossi
frazione_rossi = np.mean(mattoncini_colorati)

# Visualizziamo la frazione di mattoncini rossi rispetto al totale
print("Frazione di mattoncini rossi:", frazione_rossi)

# Visualizziamo un grafico della distribuzione dei mattoncini colorati
plt.hist(mattoncini_colorati, bins=[-0.5,0.5,1.5], color=['red'], edgecolor='black') # type: ignore
plt.xlabel('Colore del mattoncino')
plt.ylabel('Numero di mattoncini')
plt.title('Distribuzione dei mattoncini colorati')
plt.xticks([0, 1], ['Non rosso', 'Rosso'])
plt.show()

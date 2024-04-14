'''
Immagina di avere una grande ciotola di caramelle, ma molte di queste caramelle sono raccolte in pochi posti anziché essere distribuite uniformemente in tutta la ciotola. Questo è un esempio di concentrazione.
La concentrazione può sembrare alta se guardiamo l'intera ciotola, ma se guardiamo solo piccole parti della ciotola, potremmo vedere una concentrazione più bassa. Questo è come guardare una foto da lontano e vedere molte caramelle insieme, ma se ti avvicini e guardi da vicino, vedrai che le caramelle sono sparse in modo diverso.
'''

import matplotlib.pyplot as plt
import numpy as np

# Genera le coordinate (x, y) delle caramelle
np.random.seed(0)
num_caramelle = 100
x = np.random.rand(num_caramelle) * 10  # Coordinate x casuali
y = np.random.rand(num_caramelle) * 10  # Coordinate y casuali

# Definisci due subplot per visualizzare da lontano e da vicino
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot da lontano
ax1.scatter(x, y, color='skyblue')
ax1.set_title("Vista da lontano")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")

# Plot da vicino (zoom)
ax2.scatter(x, y, color='skyblue')
ax2.set_title("Vista da vicino (zoom)")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_xlim(2, 4)  # Imposta i limiti dell'asse x per il zoom
ax2.set_ylim(2, 4)  # Imposta i limiti dell'asse y per il zoom

'''
questi dati che rappresentano i tempi di vita (ore) di un campione di 40 transistor:
112 121 126 108 141 104 136 134 121 111
143 116 108 122 127 125 165 145 187 140
134 120 131 112 111 110 154 150 147 132 131 
132 119 110 124 121 153 154 184 130 136 154
a) determina media mediana e moda campionaria
b)traccia un grafico delle frequenze cumulative relative per questi dati
'''



import numpy as np
import matplotlib.pyplot as plt

# Dati sui tempi di vita dei transistor (ore)
tempi_vita = [112, 121, 126, 108, 141, 104, 136, 134, 121, 111, 143, 116, 108, 122, 127, 125, 165, 145, 187, 140,
              134, 120, 131, 112, 111, 110, 154, 150, 147, 132, 131, 132, 119, 110, 124, 121, 153, 154, 184, 130, 136, 154]

# Calcolo della media campionaria
media = np.mean(tempi_vita)

# Calcolo della mediana campionaria
mediana = np.median(tempi_vita)

# Calcolo della moda campionaria
moda = np.argmax(np.bincount(tempi_vita))

# Calcolo delle frequenze cumulative relative
tempi_vita_sorted = np.sort(tempi_vita)
frequenze_cumulative = np.arange(
    1, len(tempi_vita_sorted) + 1) / len(tempi_vita_sorted)

# Stampa delle statistiche campionarie
print("Statistiche Campionarie:")
print("Media Campionaria: {:.2f}".format(media))
print("Mediana Campionaria: {:.2f}".format(mediana))
print("Moda Campionaria: {}".format(moda))
print()

# Tracciamento del grafico delle frequenze cumulative relative
plt.plot(tempi_vita_sorted, frequenze_cumulative, marker='o')
plt.xlabel('Tempi di Vita')
plt.ylabel('Frequenze Cumulative Relative')
plt.title(
    'Grafico delle Frequenze Cumulative Relative dei Tempi di Vita dei Transistor')
plt.grid(True)
plt.show()

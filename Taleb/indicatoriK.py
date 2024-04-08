'''
Immagina di avere una scatola piena di soldi, e ogni volta che metti più soldi dentro, la scatola diventa più grande. 
Ora, c'è una cosa speciale che stiamo guardando, chiamata "κbq", che ci dice quanto sia grande una scatola speciale che usiamo per misurare quanta ricchezza c'è in giro.
Quello che abbiamo notato è che se la nostra scatola speciale diventa più grande, c'è più probabilità che metteremo più soldi dentro. 
È come se più soldi ci sono, più la nostra scatola speciale diventa grande.

Questo è importante perché ci aiuta a capire quanto è grande la differenza tra le persone ricche e quelle meno ricche. 
Questa cosa succede anche in altre situazioni, come durante le guerre o le pandemie, o quando guardiamo le dimensioni delle aziende.

'''
import numpy as np
import matplotlib.pyplot as plt

# Generiamo dati casuali per simulare la ricchezza, le guerre/pandemie e le dimensioni delle aziende
n = 1000  # Numero di dati
ricchezza = np.random.normal(50000, 10000, n)  # Genera dati casuali per la ricchezza
guerre_pandemie = np.random.uniform(0, 1, n)  # Genera dati casuali per le guerre/pandemie
dimensioni_aziende = np.random.randint(1, 1000, n)  # Genera dati casuali per le dimensioni delle aziende

# Calcoliamo l'indicatore kappa per ciascuna categoria
kappa_ricchezza = np.mean(ricchezza) / np.max(ricchezza)
kappa_guerre_pandemie = np.mean(guerre_pandemie) / np.max(guerre_pandemie)
kappa_dimensioni_aziende = np.mean(dimensioni_aziende) / np.max(dimensioni_aziende)

# Visualizziamo i risultati
categories = ['Ricchezza', 'Guerre/Pandemie', 'Dimensioni Aziende']
kappas = [kappa_ricchezza, kappa_guerre_pandemie, kappa_dimensioni_aziende]

plt.bar(categories, kappas, color=['blue', 'red', 'green'])
plt.title('Effetto dell\'aumento su kappa')
plt.xlabel('Categoria')
plt.ylabel('Kappa')
plt.show()

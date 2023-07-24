'''
costruire: 
a)tabella frequenze, 
b) grafico a linee delle frequenze, 
C) grafico frequenze cumulative relative 
d)media campionaria 
e)mediana campionaria 
f)moda campionaria 
g) deviazione standard campionaria?
'''
# view safetyBoard.csv
import numpy as np
import matplotlib.pyplot as plt

# Dati sulla frequenza degli incidenti aerei
anni = ['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
        '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995']
voli = [5.2, 5, 5.4, 5.8, 6.4, 6.3, 6.4, 6.6,
        6.7, 7.1, 7.2, 7.5, 8.1, 8.2, 8.3, 8.4]
incidenti_mortali = [0, 4, 4, 4, 1, 4, 2, 4, 3, 11, 6, 4, 4, 1, 4, 2]
vittime = [0, 4, 233, 5, 4, 197, 5, 231, 285, 178, 39, 62, 33, 1, 239, 166]

# Costruzione della tabella di frequenze
tabella_frequenze = {
    'Anno': anni,
    'Voli': voli,
    'Incidenti mortali': incidenti_mortali,
    'Vittime': vittime
}

# Calcolo delle frequenze
frequenze = {
    'Anno': anni,
    'Voli': [voli.count(volo) for volo in voli],
    'Incidenti mortali': [incidenti_mortali.count(incidente) for incidente in incidenti_mortali],
    'Vittime': [vittime.count(vittima) for vittima in vittime]
}

# Calcolo delle frequenze cumulative relative
frequenze_cumulative = {
    'Anno': anni,
    'Voli': np.cumsum(frequenze['Voli']) / len(anni),
    'Incidenti mortali': np.cumsum(frequenze['Incidenti mortali']) / len(anni),
    'Vittime': np.cumsum(frequenze['Vittime']) / len(anni)
}

# Calcolo della media campionaria
media = np.mean(voli)

# Calcolo della mediana campionaria
mediana = np.median(voli)

# Calcolo della moda campionaria
moda = np.argmax(np.bincount(voli))

# Calcolo della deviazione standard campionaria
deviazione_standard = np.std(voli)

# Stampa della tabella di frequenze
print("Tabella di Frequenze:")
for key, values in tabella_frequenze.items():
    print("{:<17} {}".format(key, '\t'.join(map(str, values))))
print()

# Grafico a linee delle frequenze
plt.plot(anni, frequenze['Voli'], marker='o')
plt.xlabel('Anno')
plt.ylabel('Frequenza')
plt.title('Grafico a Linee delle Frequenze dei Voli')
plt.grid(True)
plt.show()

# Grafico delle frequenze cumulative relative
plt.plot(anni, frequenze_cumulative['Voli'], marker='o')
plt.xlabel('Anno')
plt.ylabel('Frequenza Cumulativa Relativa')
plt.title('Grafico delle Frequenze Cumulative Relative dei Voli')
plt.grid(True)
plt.show()

# Stampa delle statistiche campionarie
print("Statistiche Campionarie:")
print("Media Campionaria: {:.2f}".format(media))
print("Mediana Campionaria: {:.2f}".format(mediana))
print("Moda Campionaria: {:.2f}".format(moda))
print("Deviazione Standard Campionaria: {:.2f}".format(deviazione_standard))


import matplotlib.pyplot as plt

# Dati di esempio (percentuali di caramelle per tipo)
tipi_caramelle = ['Cioccolato', 'Caramelle gommose', 'Liquirizia']
percentuali = [30, 50, 20]  # Queste sono solo percentuali di esempio

# Intervallo teorico di caramelle totali
caramelle_min = 1000
caramelle_max = 10000

# Calcola stime approssimative di caramelle per tipo
stima_caramelle = []
for percentuale in percentuali:
    caramelle_stimate = percentuale / 100 * (caramelle_max - caramelle_min)
    stima_caramelle.append(caramelle_stimate)

# Stampa le stime
for tipo, stima in zip(tipi_caramelle, stima_caramelle):
    print(f"Stima di {tipo}: {int(stima)} caramelle")

# Visualizza il grafico a torta
plt.figure(figsize=(8, 8))
plt.pie(percentuali, labels=tipi_caramelle, autopct='%1.1f%%', startangle=140)
plt.title("Proporzioni di caramelle per tipo")
plt.axis('equal')  # Per fare in modo che il grafico sia circolare
plt.show()

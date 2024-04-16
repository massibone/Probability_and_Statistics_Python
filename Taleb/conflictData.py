'''
creiamo un DataFrame pandas con dati ipotetici sui conflitti e sul numero di vittime nel corso del tempo (ogni 10 anni a partire dal 1950). Successivamente, utilizziamo Matplotlib per tracciare un grafico che mostri l'andamento storico dei conflitti e delle relative vittime nel tempo.

Il grafico risultante illustra in modo semplice come il numero di vittime da conflitti sia aumentato nel corso degli anni, evidenziando l'effetto dei conflitti di maggiore portata sulla statistica storica. Se si desidera esaminare più approfonditamente il survivorship bias, potrebbe essere necessario considerare anche altri fattori come la durata dei conflitti, l'accesso alle informazioni storiche e la rappresentatività dei dati nel corso del tempo.
'''

import pandas as pd
import matplotlib.pyplot as plt

# Dati di esempio: elenco di conflitti con le relative vittime nel corso del tempo
conflicts_data = {
    'Year': [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020],
    'Fatalities': [10000, 20000, 50000, 100000, 150000, 300000, 500000, 1000000]
}

# Creazione di un DataFrame pandas dai dati
df = pd.DataFrame(conflicts_data)

# Plot dei dati storici dei conflitti e delle vittime nel corso del tempo
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Fatalities'], marker='o', linestyle='-', color='b')
plt.title('Conflitti e Vittime nel Tempo', fontsize=14)
plt.xlabel('Anno', fontsize=12)
plt.ylabel('Numero di Vittime', fontsize=12)
plt.grid(True)
plt.xticks(df['Year'], rotation=45)
plt.show()

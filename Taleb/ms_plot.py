import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Definiamo i dati della tabella come un dizionario
data = {
    'Asset': ['Australian Dollar/USD', 'Australia TB 10y', 'Australia TB 3y', 'BeanOil', 'Bonds 30Y', 'Bovespa', 'British Pound/USD', 'CAC40', 'Canadian Dollar', 'Cocoa NY', 'Coffee NY', 'Copper', 'Corn', 'Crude Oil', 'CT', 'DAX', 'Euro Bund', 'Euro Currency/DEM previously', 'Eurodollar Depo 1M', 'Eurodollar Depo 3M', 'FTSE', 'Gold', 'Heating Oil', 'Hogs', 'Jakarta Stock Index', 'Japanese Gov Bonds', 'Live Cattle', 'Nasdaq Index', 'Natural Gas', 'Nikkei', 'Notes 5Y', 'Russia RTSI', 'Short Sterling', 'Silver', 'Smallcap', 'SoyBeans', 'SoyMeal', 'Sp500', 'Sugar #11', 'SwissFranc', 'TY10Y Notes', 'Wheat', 'Yen/USD'],
    'K(1)': [6.3, 7.5, 7.5, 5.5, 5.6, 24.9, 6.9, 6.5, 7.4, 4.9, 10.7, 6.4, 9.4, 29.0, 7.8, 8.0, 4.9, 5.5, 41.5, 21.1, 15.2, 11.9, 20.0, 4.5, 40.5, 17.2, 4.2, 11.4, 6.0, 52.6, 5.1, 13.3, 851.8, 160.3, 6.1, 7.1, 8.9, 38.2, 9.4, 5.1, 5.9, 5.6, 9.7],
    'K(10)': [3.8, 6.2, 5.4, 7.0, 4.7, 5.0, 7.4, 4.7, 4.1, 4.0, 5.2, 5.5, 8.0, 4.7, 4.8, 6.5, 3.2, 3.8, 28.0, 8.1, 27.4, 14.5, 4.1, 4.6, 6.2, 16.9, 4.9, 9.3, 3.9, 4.0, 3.2, 6.0, 93.0, 22.6, 5.7, 8.8, 9.8, 7.7, 6.4, 3.8, 5.5, 6.0, 6.1],
    'K(66)': [2.9, 3.5, 4.2, 4.9, 3.9, 2.3, 5.3, 3.6, 3.9, 5.2, 5.3, 4.5, 5.0, 5.1, 3.7, 3.7, 3.3, 2.8, 6.0, 7.0, 6.5, 16.6, 4.4, 4.8, 4.2, 4.3, 5.6, 5.0, 3.8, 2.9, 2.5, 7.3, 3.0, 10.2, 6.8, 6.7, 5.1, 3.8, 2.6, 4.9, 4.9, 2.5],
    'Max_Quartic': [0.12, 0.08, 0.06, 0.11, 0.02, 0.27, 0.05, 0.05, 0.06, 0.04, 0.13, 0.05, 0.18, 0.79, 0.25, 0.20, 0.06, 0.06, 0.31, 0.25, 0.54, 0.04, 0.74, 0.05, 0.19, 0.48, 0.04, 0.13, 0.06, 0.72, 0.06, 0.13, 0.75, 0.94, 0.06, 0.17, 0.09, 0.79, 0.30, 0.05, 0.10, 0.02, 0.27],
    'Years': [22, 25, 21, 47, 32, 16, 38, 20, 38, 47, 37, 48, 49, 26, 48, 18, 18, 38, 19, 28, 25, 35, 31, 43, 16, 24, 44, 21, 19, 23, 21, 17, 17, 46, 17, 47, 48, 56, 48, 38, 27, 49, 38]
}

# Creiamo il DataFrame
df = pd.DataFrame(data)

# Stampiamo il DataFrame
print(df)

# Calcoliamo le statistiche di base
statistics = df.describe()

# Stampiamo le statistiche di base
print(statistics)

# Calcoliamo la media della curtosi per le finestre temporali di 1, 10 e 66 giorni
mean_kurtosis = df.mean(axis=0)

# Stampiamo la media della curtosi
print("\nMedia della curtosi per le finestre temporali di 1, 10 e 66 giorni:")
print(mean_kurtosis)
# Assumiamo che ci sia una colonna 'Year' che rappresenti gli anni dal 1958 al 2018
df['Year'] = np.arange(1958, 2019)

# Supponiamo che ci sia una colonna 'SP500' che rappresenti i valori dell'SP500 per ogni anno


# Plot MS per p = 1, 2, 3, 4
plt.figure(figsize=(10, 6))
for p in range(1, 5):
    plt.plot(df['Year'], df[f'M{p}'], label=f'M{p}')

plt.title('MS Plot per SP500 (1958-2018)')
plt.xlabel('Anno')

plt.legend()
plt.grid(True)
plt.show()
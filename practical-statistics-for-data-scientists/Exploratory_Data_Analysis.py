import pandas as pd
import numpy as np
from scipy.stats import trim_mean
from statsmodels import robust
import wquantiles
import matplotlib.pyplot as plt

# Carica il dataset degli stati
STATE_CSV = "state.csv"
state = pd.read_csv(STATE_CSV)

# Calcola la media, la media tagliata e la mediana per la popolazione
print("Media della popolazione:", state['Population'].mean())
print("Media tagliata della popolazione:", trim_mean(state['Population'], 0.1))
print("Mediana della popolazione:", state['Population'].median())

# Calcola la media dell'indice di omicidi
print("Media dell'indice di omicidi:", state['Murder.Rate'].mean())

# Calcola la media ponderata dell'indice di omicidi
weighted_mean = np.average(state['Murder.Rate'], weights=state['Population'])
print("Media ponderata dell'indice di omicidi:", weighted_mean)

# Calcola la mediana ponderata dell'indice di omicidi
weighted_median = wquantiles.median(state['Murder.Rate'], weights=state['Population'])
print("Mediana ponderata dell'indice di omicidi:", weighted_median)

# Calcola la deviazione standard della popolazione
print("Deviazione standard della popolazione:", state['Population'].std())

# Calcola l'intervallo interquartile della popolazione
print("Intervallo interquartile della popolazione:", state['Population'].quantile(0.75) - state['Population'].quantile(0.25))

# Calcola la deviazione assoluta dalla mediana della popolazione
mad = robust.scale.mad(state['Population'])
print("Deviazione assoluta dalla mediana della popolazione:", mad)

# Calcola i quantili dell'indice di omicidi
print("Quantili dell'indice di omicidi:", state['Murder.Rate'].quantile([0.05, 0.25, 0.5, 0.75, 0.95]))

# Crea un boxplot della popolazione
ax = (state['Population'] / 1_000_000).plot.box(figsize=(3, 4))
ax.set_ylabel('Popolazione (milioni)')
plt.tight_layout()
plt.show()

# Crea un istogramma della popolazione
ax = (state['Population'] / 1_000_000).plot.hist(figsize=(4, 4))
ax.set_xlabel('Popolazione (milioni)')
plt.tight_layout()
plt.show()

# Crea un grafico a densità dell'indice di omicidi
ax = state['Murder.Rate'].plot.density(figsize=(4, 4))
ax.set_xlabel('Tasso di omicidi (per 100.000)')
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon

# Parametro della distribuzione esponenziale
lambda_ = 0.5

# Generazione dei valori possibili per la variabile casuale
x = np.linspace(0, 10, 1000)

# Calcolo della funzione di densità di probabilità per la distribuzione esponenziale
pdf = expon.pdf(x, scale=1/lambda_)

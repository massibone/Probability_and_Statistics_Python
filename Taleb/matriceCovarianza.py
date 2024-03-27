import numpy as np

# Rendimenti storici dei titoli nel portafoglio
returns_stock1 = np.array([0.02, 0.03, 0.01, -0.02, 0.015])  # Esempio di rendimenti del titolo 1
returns_stock2 = np.array([0.015, 0.025, -0.01, 0.03, -0.005])  # Esempio di rendimenti del titolo 2

# Calcolo della matrice di covarianza
portfolio_returns = np.array([returns_stock1, returns_stock2])
cov_matrix = np.cov(portfolio_returns)

print("Matrice di Covarianza del Portafoglio:")
print(cov_matrix)

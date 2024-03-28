import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

# Definiamo una funzione per calcolare la probabilità P(X > k) per la distribuzione gaussiana
def gaussian_prob(k, variance):
    return 1 - 0.5 * (1 + erf(k / (np.sqrt(2 * variance))))

# Definiamo una funzione per calcolare la probabilità P(X > k) per la distribuzione di Student
def student_prob(k, df):
    return 1 - np.arctan(k / np.sqrt(df)) / np.pi

# Definiamo una funzione per calcolare la probabilità P(X > k) per la distribuzione di Pareto
def pareto_prob(k, alpha):
    return (k * (-alpha))

# Valori di k come nell'esempio della tabella
k_values = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

# Calcoliamo le probabilità per ogni distribuzione
gaussian_probs = gaussian_prob(k_values, variance=1)
student_probs = student_prob(k_values, df=3)
pareto_probs = pareto_prob(k_values, alpha=2)

# Creiamo un grafico per visualizzare i risultati
plt.figure(figsize=(10, 6))

plt.plot(k_values, gaussian_probs, label='Gaussiana', marker='o')
plt.plot(k_values, student_probs, label='Student (3)', marker='s')
plt.plot(k_values, pareto_probs, label='Pareto (2)', marker='^')

plt.yscale('log')  # Scala logaritmica per visualizzare meglio le differenze
plt.xlabel('k')
plt.ylabel('P(X > k)')
plt.title('Scalabilità: Confronto tra Funzioni a Variazione Regolare e Altre Distribuzioni')
plt.legend()
plt.grid(True)
plt.show()

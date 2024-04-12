import numpy as np
import matplotlib.pyplot as plt

# Funzione per calcolare il Gini index
def gini_index(data):
    n = len(data)
    data = np.sort(data)
    coef = 2 / n
    indexes = np.arange(1, n + 1)
    weighted_sum = (indexes * data).sum()
    total = data.sum()
    return coef * weighted_sum / total - (n + 1) / n

# Numero di persone nel gruppo
num_people = 1000

# Simulazione della distribuzione del denaro tra le persone (distribuzione normale)
mean_money = 1000  # Media del denaro
std_money = 500  # Deviazione standard del denaro
money_distribution = np.random.normal(mean_money, std_money, num_people)

# Calcolo del Gini index per la distribuzione del denaro
gini_value = gini_index(money_distribution)

# Plot della distribuzione del denaro
plt.figure(figsize=(10, 6))
plt.hist(money_distribution, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Somma di denaro')
plt.ylabel('Numero di persone')
plt.title('Distribuzione del denaro tra le persone')
plt.grid(True)
plt.show()

# Output del Gini index
print(f"Gini Index per la distribuzione del denaro: {gini_value}")

'''
Se molte persone nel gruppo hanno somme di denaro intorno a 1000 (la media), allora il Gini index potrebbe essere più basso, indicando una distribuzione più equa del denaro. Tuttavia, se ci sono differenze significative nelle somme di denaro tra le persone, il Gini index sarà più alto, indicando una distribuzione più diseguale del denaro.

In generale, all'aumentare del numero di persone nel gruppo, diventa più importante considerare la distribuzione del denaro tra di loro e come questa distribuzione influenzi l'equità complessiva della situazione finanziaria. Il Gini index fornisce uno strumento utile per quantificare questa equità o diseguaglianza nella distribuzione del denaro.
'''
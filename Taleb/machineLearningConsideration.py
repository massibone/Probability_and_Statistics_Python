import numpy as np
import matplotlib.pyplot as plt

# Funzione sigmoide
def sigmoid(x, k, b):
  return (1 / (1 + np.exp(-k * (x - b))))

# Funzione ReLu
def relu(x):
  return np.maximum(0, x)

# Funzione di payoff di un'opzione call
def call_payoff(x, K):
  return np.maximum(x - K, 0)

# Funzione per sommare opzioni call con strike price e pesi diversi
def option_sum(x, strikes, weights):
  payoff = 0
  for K, w in zip(strikes, weights):
    payoff += w * call_payoff(x, K)
  return payoff

# Parametri
x = np.linspace(-5, 5, 100)
K = np.array([0, 1, 2])
w = np.array([0.5, 0.3, 0.2])

# Grafico
plt.plot(x, sigmoid(x, 1, 0), label="Sigmoide")
plt.plot(x, relu(x), label="ReLu")
plt.plot(x, option_sum(x, K, w), label="Somma di opzioni call")
plt.legend()
plt.show()

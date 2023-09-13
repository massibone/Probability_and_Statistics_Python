import random
import statistics

def calculate_mean_and_variance(data):
    mean = statistics.mean(data)
    variance = statistics.variance(data)
    return mean, variance

# Probabilità 1-p e p+1
p = 0.3
n = 10

# Generazione dei dati con probabilità 1-p e p+1
data = [random.choice([1-p, p+1]) for _ in range(n)]

# Calcolo della media e della varianza
mean, variance = calculate_mean_and_variance(data)

# Stampa dei risultati
print("Dati:", data)
print("Media:", mean)
print("Varianza:", variance)

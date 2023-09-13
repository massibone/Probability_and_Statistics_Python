import statistics

def calculate_mean_and_variance(data):
    mean = statistics.mean(data)
    variance = statistics.variance(data)
    return mean, variance

# Valori 1, 2, 3, 4 con pari probabilità
values = [1, 2, 3, 4]

# Calcolo della media e della varianza
mean, variance = calculate_mean_and_variance(values)

# Stampa dei risultati
print("Valori:", values)
print("Media:", mean)
print("Varianza:", variance)

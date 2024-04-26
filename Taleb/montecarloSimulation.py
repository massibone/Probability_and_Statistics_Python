'''
simula il processo di generazione di valori casuali uniformemente distribuiti tra un limite inferiore e uno superiore per un evento specifico. 
'''


import random
import statistics

# Definizione di una funzione per eseguire il procedimento Monte Carlo
def monte_carlo_simulation(lower_bound, upper_bound, num_replications):
    estimates = []
    for _ in range(num_replications):
        # Genera un valore casuale uniforme tra lower_bound e upper_bound
        random_value = random.uniform(lower_bound, upper_bound)
        estimates.append(random_value)
    
    return estimates
# Dati di esempio: limiti inferiori e superiori per un evento
lower_bound = 200000
upper_bound = 300000
num_replications = 10000  # Numero di repliche Monte Carlo da eseguire

# Esegui la simulazione Monte Carlo
estimated_values = monte_carlo_simulation(lower_bound, upper_bound, num_replications)

# Calcola la media delle stime ottenute
mean_estimate = statistics.mean(estimated_values)

# Stampare i risultati
print(f"Limiti inferiori: {lower_bound}")
print(f"Limiti superiori: {upper_bound}")
print(f"Numero di repliche Monte Carlo: {num_replications}")
print(f"Media delle stime ottenute: {mean_estimate}")

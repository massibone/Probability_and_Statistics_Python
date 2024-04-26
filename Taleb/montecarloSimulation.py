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

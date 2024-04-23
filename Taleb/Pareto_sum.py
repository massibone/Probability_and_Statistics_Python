'''
Ogni volta che prendi un gruppo di giocattoli e ne calcoli la media, 
scopri che questa media si avvicina sempre a un certo numero, indipendentemente da quanti giocattoli prendi.
In matematica, questo concetto è simile a prendere un tipo speciale di distribuzione di numeri (distribuzione di Pareto) e sommare molti numeri da questa distribuzione insieme.
Anche se aggiungi più e più numeri, la media di questi numeri si avvicina sempre a un certo valore.
Questo valore dipende da quanto grandi o piccoli sono i numeri nella distribuzione.
'''
import numpy as np

def pareto_sum_mean(alpha, num_samples, num_trials):
    lambda_value = 1.0  # Valore di lambda per la distribuzione di Pareto
    means = []

    for _ in range(num_trials):
        # Genera num_samples numeri casuali da una distribuzione di Pareto
        samples = np.random.pareto(alpha, size=num_samples)

        # Calcola la media dei numeri generati
        mean_value = np.mean(samples)

        # Aggiungi la media alla lista delle medie calcolate
        means.append(mean_value)

    # Calcola la media delle medie ottenute nei vari tentativi
    final_mean = np.mean(means)

    return final_mean

# Parametri
alpha_value = 1.5  # Valore di alpha (1 < alpha < 2)
num_samples_per_trial = 1000  # Numero di numeri da generare da ogni distribuzione di Pareto
num_trials = 1000  # Numero di prove da eseguire

# Calcola la media finale delle somme
final_mean_result = pareto_sum_mean(alpha_value, num_samples_per_trial, num_trials)
print("Media finale delle somme di numeri da distribuzione di Pareto con alpha =", alpha_value, ":", final_mean_result)
'''
Se α è più vicino a 1, significa che ci sono più numeri con valori elevati nella distribuzione, e di conseguenza la media finale delle somme sarà diversa rispetto a quando 
α è più vicino a 2.
'''

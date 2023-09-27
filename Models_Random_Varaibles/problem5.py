'''
l 12% della popolazione mondiale è mancina.,trova la probabilità che in un campione aleatorio di 100 persone vi siano persone mancine il numero e che vi sia un numero di mancini tra 10 e 12.
La distribuzione binomiale viene utilizzata per modellare eventi binari (successo/fallimento) ripetuti in modo indipendente.

Nel tuo caso, la probabilità di successo (essere mancini) è del 12% o 0.12
'''

from scipy.stats import binom

def calculate_probability(sample_size, p, lower_bound, upper_bound):
    probability = 0
    for i in range(lower_bound, upper_bound + 1):
        probability += binom.pmf(i, sample_size, p)
    return probability

sample_size = 100
p = 0.12
lower_bound = 10
upper_bound = 12

probability = calculate_probability(sample_size, p, lower_bound, upper_bound)
print(f"Probabilità: {probability}")

# probabilità del 35%

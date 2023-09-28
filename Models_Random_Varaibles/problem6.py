'''
a media e la deviazione standard dei punteggi della prova di matematica di tutte le scuole superiori di Milano sono stati 517 e 120.
Trova la probabilità che un campione di 144 studenti abbia un punteggio che superi: a)507 b) 517c)537 d)550
'''

from scipy.stats import norm

def calculate_probability(mean, std_dev, value):
    z_score = (value - mean) / std_dev
    probability = 1 - norm.cdf(z_score)
    return probability

mean = 517
std_dev = 120

value_a = 507
value_b = 517
value_c = 537
value_d = 550

probability_a = calculate_probability(mean, std_dev, value_a)
probability_b = calculate_probability(mean, std_dev, value_b)
probability_c = calculate_probability(mean, std_dev, value_c)
probability_d = calculate_probability(mean, std_dev, value_d)

print(f"Probabilità a) {probability_a}")
print(f"Probabilità b) {probability_b}")
print(f"Probabilità c) {probability_c}")
print(f"Probabilità d) {probability_d}")

'''
SOLUZIONI
Probabilità a) 0.5332067518526222
Probabilità b) 0.5
Probabilità c) 0.43381616738909634
Probabilità d) 0.39165811915360516
'''

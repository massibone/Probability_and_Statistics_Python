'''
i punteggi dei test del Q.I. medio degli studenti dell'università di un campione di 18 studenti è:
130 122 119 142 136 127 120 152 141
132 127 118 150 141 133 137 129 142
costruisci gli intervalli di confidenzas al 95% e al 80% 
a)quello bilaterale b) quello unilaterale sinistro c)quello unilaterale destro
''''

import numpy as np
from scipy.stats import t

data = [130, 122, 119, 142, 136, 127, 120, 152, 141,
        132, 127, 118, 150, 141, 133, 137, 129, 142]

sample_mean = np.mean(data)  # Calcolo del valore medio del campione
sample_std_dev = np.std(data, ddof=1)  # Calcolo della deviazione standard campionaria
sample_size = len(data)  # Dimensione del campione

confidence_level_a = 0.95  # Livello di confidenza bilaterale
confidence_level_b = 0.80  # Livello di confidenza unilaterale sinistro
confidence_level_c = 0.80  # Livello di confidenza unilaterale destro

degrees_of_freedom = sample_size - 1  # Gradi di libertà per la distribuzione t

# Calcolo degli intervalli di confidenza bilaterali
lower_bound_a = sample_mean - t.ppf(1 - (1 - confidence_level_a) / 2, degrees_of_freedom) * sample_std_dev / np.sqrt(sample_size)
upper_bound_a = sample_mean + t.ppf(1 - (1 - confidence_level_a) / 2, degrees_of_freedom) * sample_std_dev / np.sqrt(sample_size)

# Calcolo dell'intervallo di confidenza unilaterale sinistro
lower_bound_b = sample_mean - t.ppf(1 - confidence_level_b, degrees_of_freedom) * sample_std_dev / np.sqrt(sample_size)
upper_bound_b = float("inf")  # L'intervallo unilaterale sinistro non ha un limite superiore

# Calcolo dell'intervallo di confidenza unilaterale destro
lower_bound_c = float("-inf")  # L'intervallo unilaterale destro non ha un limite inferiore
upper_bound_c = sample_mean + t.ppf(1 - confidence_level_c, degrees_of_freedom) * sample_std_dev / np.sqrt(sample_size)

print(f"Intervallo di confidenza bilaterale al {confidence_level_a * 100}%: [{lower_bound_a}, {upper_bound_a}]")
print(f"Intervallo di confidenza unilaterale sinistro al {confidence_level_b * 100}%: [{lower_bound_b}, {upper_bound_b}]")
print(f"Intervallo di confidenza unilaterale destro al {confidence_level_c * 100}%: [{lower_bound_c}, {upper_bound_c}]")

'''
RISULTATI
Intervallo di confidenza bilaterale al 95.0%: [128.1435316088795, 138.30091283556496]
Intervallo di confidenza unilaterale sinistro al 80.0%: [135.30028396777524, inf]Intervallo di confidenza unilaterale destro al 80.0%: [-inf, 131.1441604766692]  
'''

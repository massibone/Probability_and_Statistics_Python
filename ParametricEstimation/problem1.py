'''
Si analizza un campione di 20 sigarette per vedere contenuto nicotina e il valore medio è di 1.2mg.calcola un intervallo di confidenza  bilaterale al 99% per il contenuto medio di nicotina di quel tipo di sigarette sapendo che la deviazione standard è 0.2mg.

L'intervallo di confidenza può essere calcolato utilizzando la formula:

Intervallo di confidenza = valore medio ± (t * errore standard)

Dove t è il valore critico corrispondente al livello di confidenza desiderato, errore standard è la deviazione standard campionaria divisa per la radice quadrata della dimensione del campione.

Per un intervallo di confidenza bilaterale al 99%, il livello di confidenza è del 99% / 2 = 0.995. Utilizzando una tabella o una funzione di distribuzione t, troviamo che il valore critico corrispondente a un livello di confidenza di 0.995 con 19 gradi di libertà (20 - 1) è di circa 2.861.
'''

import math

sample_mean = 1.2  # Valore medio del campione
sample_std_dev = 0.2  # Deviazione standard del campione
sample_size = 20  # Dimensione del campione

confidence_level = 0.99  # Livello di confidenza bilaterale

critical_value = 2.861  # Valore critico t corrispondente al livello di confidenza

standard_error = sample_std_dev / math.sqrt(sample_size)  # Errore standard

lower_bound = sample_mean - (critical_value * standard_error)
upper_bound = sample_mean + (critical_value * standard_error)

print(f"Intervallo di confidenza al {confidence_level * 100}%: [{lower_bound}, {upper_bound}]")
#Intervallo di confidenza al 99.0%: [1.072052190327462, 1.327947809672538]

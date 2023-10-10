'''
verifica che questi tre campioni indipendent provengano tutti dalla stessa polozaione normale.
Test di normalità. Un test comunemente usato per questo scopo è il test di Shapiro-Wilk.
camp1 35 37 29 27 30
camp2 29 38 34 30 32 
camp3 44 52 56
-------
Se il valore di p ottenuto per ciascun campione è superiore al livello di significatività desiderato (ad esempio, 0.05), possiamo concludere che non abbiamo sufficienti evidenze per rigettare l'ipotesi nulla e accettare che i dati provengono da una distribuzione normale comune. Altrimenti, se il valore di p è inferiore al livello di significatività, dovremmo rigettare l'ipotesi nulla e considerare i dati non provenienti da una distribuzione normale comune.
'''
import numpy as np
from scipy.stats import shapiro

# Dati dei tre campioni
camp1 = np.array([35, 37, 29, 27, 30])
camp2 = np.array([29, 38, 34, 30, 32])
camp3 = np.array([44, 52, 56])

# Test di Shapiro-Wilk per i tre campioni
statistic_camp1, p_value_camp1 = shapiro(camp1)
statistic_camp2, p_value_camp2 = shapiro(camp2)
statistic_camp3, p_value_camp3 = shapiro(camp3)

# Stampa i risultati
print("Risultati del test di Shapiro-Wilk per campione 1:")
print("Statistiche del test:", statistic_camp1)
print("Valore di p:", p_value_camp1)
print()

print("Risultati del test di Shapiro-Wilk per campione 2:")
print("Statistiche del test:", statistic_camp2)
print("Valore di p:", p_value_camp2)
print()

print("Risultati del test di Shapiro-Wilk per campione 3:")
print("Statistiche del test:", statistic_camp3)
print("Valore di p:", p_value_camp3)
#risultati
'''
Risultati del test di Shapiro-Wilk per campione 1:
Statistiche del test: 0.9202497005462646
Valore di p: 0.5315518379211426

Risultati del test di Shapiro-Wilk per campione 2:
Statistiche del test: 0.9426465630531311
Valore di p: 0.6847051382064819

Risultati del test di Shapiro-Wilk per campione 3:
Statistiche del test: 0.9642857313156128
Valore di p: 0.6368856430053711
'''

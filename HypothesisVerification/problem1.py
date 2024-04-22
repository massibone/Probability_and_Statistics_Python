'''
si è pescato un campione di 10 pesci del lago A e 8 del lago B , misurandone la concetrazione di PCB.I valori trovati in parti per milione sono :
lago A 11.5 10.8 11.6 9.4 12.4 11.4 12.2 11.0 10.6 10.8
lago B 11.8 12.6 12.2 12.5 11.7 12.1 10.4 12.6
Sapendo che gli errori statistici di varianza sono 0.09 e 0.16 rispettivamente,
si può concludere ad un livello di significatività del 5% che i due laghi sono ugualmente inquinati?
'''

import numpy as np
from scipy.stats import t

# Dati dei campioni
lago_A = np.array([11.5, 10.8, 11.6, 9.4, 12.4, 11.4, 12.2, 11.0, 10.6, 10.8])
lago_B = np.array([11.8, 12.6, 12.2, 12.5, 11.7, 12.1, 10.4, 12.6])

# Dimensioni dei campioni
n_A = len(lago_A)
n_B = len(lago_B)

# Medie dei campioni
media_A = np.mean(lago_A)
media_B = np.mean(lago_B)

# Errori statistici di varianza
errore_varianza_A = 0.09
errore_varianza_B = 0.16

# Calcolo dei pesi per il test t-student
peso_A = n_A / (n_A + n_B)
peso_B = n_B / (n_A + n_B)

# Calcolo della varianza combinata pesata
varianza_combinata_pesata = (peso_A * errore_varianza_A) + (peso_B * errore_varianza_B)

# Calcolo del test t-student
t_stat = (media_A - media_B) / np.sqrt(varianza_combinata_pesata)

# Gradi di libertà
gradi_libertà = n_A + n_B - 2

# Livello di significatività
livello_significatività = 0.05

# Calcolo del valore critico t per il livello di significatività
valore_critico_t = t.ppf(1 - livello_significatività / 2, gradi_libertà)

# Confronto con il valore critico per determinare la significatività
if np.abs(t_stat) > valore_critico_t:
    print("I due laghi hanno concentrazioni di PCB significativamente diverse.")
else:
    print("Non ci sono evidenze sufficienti per concludere che i due laghi abbiano concentrazioni di PCB significativamente diverse.")

#I due laghi hanno concentrazioni di PCB significativamente diverse.

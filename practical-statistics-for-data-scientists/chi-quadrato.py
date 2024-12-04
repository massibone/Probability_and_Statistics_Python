'''
Immagina di avere un gioco in cui devi lanciare un dado e vedere quante volte esce ciascun numero. Ora, diciamo che ti aspetti che ogni numero esca un numero uguale di volte, ma quando lanci il dado, ottieni risultati diversi. Il chi-quadrato è come una misura di quanto i tuoi risultati sono diversi da ciò che ti aspettavi. Se i risultati sono molto diversi, il valore del chi-quadrato sarà alto.
'''
import numpy as np
from scipy.stats import chi2_contingency

# Dati osservati (tabella di conteggio)
observed = np.array([[30, 10], [20, 40]])

# Test del chi-quadrato per l'indipendenza tra righe e colonne
chi2, p, dof, expected = chi2_contingency(observed)

print("Valore del chi-quadrato:", chi2)
print("Gradi di libertà:", dof)
print("Valori attesi:", expected)

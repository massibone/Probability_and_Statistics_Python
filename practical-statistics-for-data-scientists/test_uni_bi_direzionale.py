'''
In un test A/B, quando confronti una nuova opzione (B) con una opzione predefinita (A), 
potresti voler utilizzare un test di ipotesi unidirezionale (one-tail) se ti interessa solo dimostrare che B è migliore di A. 
Questo test considera solo i risultati estremi in una direzione per calcolare il valore p.
Se invece vuoi proteggerti dal rischio di essere ingannato dal caso in entrambe le direzioni 
(A è diverso da B, sia maggiore che minore), utilizzi un test di ipotesi bidirezionale (two-tail). 
Questo test considera i risultati estremi in entrambe le direzioni per calcolare il valore p.

Il test unidirezionale è spesso più adatto per le decisioni A/B, 
ma molti statistici preferiscono il test bidirezionale per evitare discussioni. 
Il software di analisi, come R e scipy in Python, fornisce spesso un test bidirezionale di default.
'''
import numpy as np
from scipy import stats

# Dati campione per due gruppi (A e B)
np.random.seed(42)  # Per riproducibilità
group_A = np.random.normal(100, 10, 30)
group_B = np.random.normal(105, 10, 30)
# Test bidirezionale (two-tail)
t_statistic, p_value_two_tail = stats.ttest_ind(group_A, group_B)
print("Test bidirezionale:")
print(f"Statistiche t: {t_statistic}")
print(f"Valore p (bidirezionale): {p_value_two_tail}")

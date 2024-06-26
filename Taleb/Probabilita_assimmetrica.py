'''
Immagina di lanciare un dado molte volte e ogni volta ottenere un risultato diverso. I risultati potrebbero sembrare strani e volatili, ma il testo cerca di capire come le distribuzioni di questi risultati cambino quando si eseguono gli stessi esperimenti molte volte.
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc, erfcinv

def phi(p, pM):
    if p < 0.5:
        lambda_p = erfcinv(2 * p)
        lambda_pM = erfcinv(1 - 2 * pM)
        return (1 / (2**((n-1)/2))) * (lambda_p * (lambda_pM - 1) * (lambda_p - 1) / 
                                        ((lambda_pM - 2) * np.sqrt(1 - lambda_p) * 
                                         lambda_p * np.sqrt(1 - lambda_pM) * (lambda_pM + 1)))
    else:
        lambda_p = erfcinv(2 * (1 - p))
        lambda_pM = erfcinv(2 * pM - 1)
        return ((1 - lambda_p) ** (1/2) * (1 / (2**((n+1)/2)))) * ((lambda_p - 1) * 
                                         (lambda_pM - 1) * (lambda_p) / 

# Esempio di distribuzione di probabilità asimmetrica
n = 10
pM = 0.5
p_values = np.linspace(0, 1, 100)

pdf_values = [phi(p, pM) for p in p_values]

plt.plot(p_values, pdf_values, label=f'n={n}, pM={pM}')
plt.xlabel('p-value')
plt.ylabel('PDF')
plt.title('Probability Distribution of p-values')
plt.legend()
plt.show()                                     ((-lambda_pM) * np.sqrt(1 - lambda_p) * 
                                         lambda_p * np.sqrt(1 - lambda_pM) * (lambda_pM + 1)))

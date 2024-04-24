'''
Il testo discute della potenza (power) di un test statistico per un dato valore p (valore p) ottenuto da estrazioni casuali da un parametro non osservato θ e una dimensione del campione n. 
Si esplora la fiducia nella potenza come misura affidabile, effettuando un problema inverso per calcolare la distribuzione del valore di β dato il valore p.
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc, erfcinv

def calculate_power(p_values, n):
    # Calcola la potenza (power) del test per diversi valori di p e dimensione del campione n
    powers = []
    for p in p_values:
        beta_c = calculate_beta_c(p, n)
        phi_beta_c = calculate_phi_beta_c(beta_c, n)
        powers.append(phi_beta_c)
    return powers

def calculate_beta_c(p, n):
    # Calcola beta_c dato un valore p e una dimensione del campione n
    gamma1 = erfcinv(2 * p)
    gamma2 = erfcinv(2 * (1 - p))
    gamma3 = erfcinv(2 * p - 1)
    
    return gamma1, gamma2, gamma3

def calculate_phi_beta_c(beta_c, n):
    # Calcola phi(beta_c) per un dato beta_c e una dimensione del campione n
    gamma1, gamma2, gamma3 = beta_c
    
    phi_beta_c_L = np.sqrt(1 - gamma1 * gamma3**(-n/2)) * ((-gamma1**(1/2) * np.sqrt(1 - gamma3**(-1)) * 
                                                           (-(gamma1 - 1) * gamma1**(-2 * np.sqrt(1 - gamma3**(-1))) * 
                                                            (2 * np.sqrt(1 - gamma3**(-1)) - 1 / gamma3))))
    
    phi_beta_c_H = np.sqrt(gamma2 * (1 - gamma2)**(-n/2) * np.beta(1/2, n/2)) * (
                        (1 - 2 * (np.sqrt(-(gamma2 - 1) * gamma2) + gamma2) * np.sqrt(1 - gamma3**(-1)) + 
                        2 * np.sqrt(1 - gamma3**(-1)) + 2 * np.sqrt(-(gamma2 - 1) * gamma2 - 1 / gamma3))) * (n/2)
    
    return phi_beta_c_L if beta_c < 0.5 else phi_beta_c_H

# Esempio di calcolo della potenza del test per diversi valori di p e dimensioni del campione n
p_values = np.linspace(0, 1, 100)
n = 20
powers = calculate_power(p_values, n)

plt.plot(p_values, powers)
plt.xlabel('p-value')
plt.ylabel('Power')
plt.title(f'Power of Test for Sample Size n={n}')
plt.show()

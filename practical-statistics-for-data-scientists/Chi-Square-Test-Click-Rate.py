import pandas as pd
import numpy as np
from scipy import stats
import random
import matplotlib.pyplot as plt

def load_click_data(file_path):
    """Carica e prepara i dati dei click"""
    click_rate = pd.read_csv(file_path)
    return click_rate.pivot(index='Click', columns='Headline', values='Rate')

def chi_square(observed, expected):
    """Calcola la statistica chi-quadrato"""
    pearson_residuals = []
    for row, expect in zip(observed, expected):
        pearson_residuals.append([(observe - expect) ** 2 / expect
                                 for observe in row])
    return np.sum(pearson_residuals)

def permutation_chi_square(clicks, n_permutations=2000):
    """Esegue test di permutazione chi-quadrato"""
    # Prepara i dati
    box = [1] * 34 + [0] * 2966
    expected_clicks = 34 / 3
    expected_noclicks = 1000 - expected_clicks
    expected = [expected_clicks, expected_noclicks]
    
    # Calcola chi-quadrato osservato
    chi2observed = chi_square(clicks.values, expected)
    
    # Funzione per singola permutazione
    def perm_fun(box):
        random.shuffle(box)
        sample_clicks = [sum(box[0:1000]),
                        sum(box[1000:2000]),
                        sum(box[2000:3000])]
        sample_noclicks = [1000 - n for n in sample_clicks]
        return chi_square([sample_clicks, sample_noclicks], expected)
    
    # Esegui permutazioni
    perm_chi2 = [perm_fun(box) for _ in range(n_permutations)]
    
    # Calcola p-value
    p_value = sum(perm_chi2 > chi2observed) / len(perm_chi2)
    return chi2observed, p_value

def run_chi_square_test(clicks):
    """Esegue test chi-quadrato formale"""
    return stats.chi2_contingency(clicks)

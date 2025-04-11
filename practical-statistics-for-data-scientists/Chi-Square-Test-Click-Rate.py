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

def plot_chi_square_distribution():
    """Visualizza distribuzioni chi-quadrato per diversi gradi di libertà"""
    x = [1 + i * (30 - 1) / 99 for i in range(100)]
    chi = pd.DataFrame({
        'x': x,
        'chi_1': stats.chi2.pdf(x, df=1),
        'chi_2': stats.chi2.pdf(x, df=2),
        'chi_5': stats.chi2.pdf(x, df=5),
        'chi_10': stats.chi2.pdf(x, df=10),
        'chi_20': stats.chi2.pdf(x, df=20),
    })
    
    fig, ax = plt.subplots(figsize=(4, 2.5))
    ax.plot(chi.x, chi.chi_1, color='black', linestyle='-', label='1')
    ax.plot(chi.x, chi.chi_2, color='black', linestyle=(0, (1, 1)), label='2')
    ax.plot(chi.x, chi.chi_5, color='black', linestyle=(0, (2, 1)), label='5')
    ax.plot(chi.x, chi.chi_10, color='black', linestyle=(0, (3, 1)), label='10')
    ax.plot(chi.x, chi.chi_20, color='black', linestyle=(0, (4, 1)), label='20')
    ax.legend(title='df')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Esempio di utilizzo
    data_path = 'click_rates.csv'  # Modifica con il tuo percorso
    click_data = load_click_data(data_path)
    
    # Test di permutazione
    chi2_obs, p_val_perm = permutation_chi_square(click_data)
    print(f"Chi-quadrato osservato: {chi2_obs:.4f}")
    print(f"P-value (permutazione): {p_val_perm:.4f}")
    
    # Test chi-quadrato formale
    chi2, p_val, df, expected = run_chi_square_test(click_data)
    print(f"\nChi-quadrato (formale): {chi2:.4f}")
    print(f"P-value (formale): {p_val:.4f}")
    
    # Visualizza distribuzioni chi-quadrato
    plot_chi_square_distribution()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

def load_multiple_sessions(file_path):
    """Carica dati per multiple sessioni"""
    return pd.read_csv(file_path)

def plot_multiple_sessions(data):
    """Crea boxplot per confrontare multiple pagine"""
    ax = data.boxplot(by='Page', column='Time', figsize=(4, 4))
    ax.set_xlabel('Page')
    ax.set_ylabel('Time (in seconds)')
    plt.suptitle('')
    plt.title('')
    plt.tight_layout()
    plt.show()
def permutation_variance_test(df, n_permutations=3000):
    """Esegue test di permutazione sulla varianza"""
    # Calcola varianza osservata
    observed_variance = df.groupby('Page').mean().var()[0]
    
    # Funzione per singola permutazione
    def perm_test(df):
        df = df.copy()
        df['Time'] = np.random.permutation(df['Time'].values)
        return df.groupby('Page').mean().var()[0]
    


    # Esegui permutazioni
    random.seed(1)
    perm_variance = [perm_test(df) for _ in range(n_permutations)]
    
    # Visualizza distribuzione
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.hist(perm_variance, bins=11, rwidth=0.9)
    ax.axvline(x=observed_variance, color='black', lw=2)
    ax.text(60, 200, 'Observed\nvariance', bbox={'facecolor':'white'})
    ax.set_xlabel('Variance')
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    plt.show()
    
    # Calcola p-value
    p_value = np.mean([var > observed_variance for var in perm_variance])
    return observed_variance, p_value

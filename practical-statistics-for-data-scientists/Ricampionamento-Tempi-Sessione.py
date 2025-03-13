import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from pathlib import Path

def load_session_data(file_path):
    """Carica e prepara i dati delle sessioni"""
    session_times = pd.read_csv(file_path)
    session_times.Time = 100 * session_times.Time
    return session_times

def plot_boxplot(data):
    """Crea un boxplot dei tempi di sessione per pagina"""
    ax = data.boxplot(by='Page', column='Time', figsize=(4, 4))
    ax.set_xlabel('')
    ax.set_ylabel('Time (in seconds)')
    plt.suptitle('')
    plt.tight_layout()
    plt.show()


def permutation_test(x, nA, nB):
    """Esegue un singolo test di permutazione"""
    n = nA + nB
    idx_B = set(random.sample(range(n), nB))
    idx_A = set(range(n)) - idx_B
    return x.loc[list(idx_B)].mean() - x.loc[list(idx_A)].mean()

def run_permutation_analysis(data, n_permutations=1000):
    """Esegue l'analisi completa di permutazione"""
    # Calcola le differenze reali
    mean_a = data[data.Page == 'Page A'].Time.mean()
    mean_b = data[data.Page == 'Page B'].Time.mean()
    observed_diff = mean_b - mean_a

    # Esegui test di permutazione
    nA = data[data.Page == 'Page A'].shape[0]
    nB = data[data.Page == 'Page B'].shape[0]
        

    random.seed(1)
    perm_diffs = [permutation_test(data.Time, nA, nB) 
                  for _ in range(n_permutations)]
    
    # Visualizza risultati
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.hist(perm_diffs, bins=11, rwidth=0.9)
    ax.axvline(x=observed_diff, color='black', lw=2)
    ax.text(50, 190, 'Observed\ndifference', bbox={'facecolor':'white'})
    ax.set_xlabel('Session time differences (in seconds)')
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    plt.show()

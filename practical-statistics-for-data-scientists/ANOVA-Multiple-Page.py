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

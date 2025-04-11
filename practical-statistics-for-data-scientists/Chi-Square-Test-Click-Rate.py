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

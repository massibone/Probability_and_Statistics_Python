import numpy as np
import pandas as pd
import scipy.stats as stats

# Generazione di dati di esempio per A/B test
np.random.seed(42)
n = 1000  # Numero di soggetti per gruppo
group_a = np.random.choice([0, 1], size=n, p=[0.95, 0.05])  # Gruppo A: 5% conversione
group_b = np.random.choice([0, 1], size=n, p=[0.90, 0.10])  # Gruppo B: 10% conversione

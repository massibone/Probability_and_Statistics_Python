import numpy as np
import pandas as pd
import scipy.stats as stats

# Generazione di dati di esempio per A/B test
np.random.seed(42)
n = 1000  # Numero di soggetti per gruppo
group_a = np.random.choice([0, 1], size=n, p=[0.95, 0.05])  # Gruppo A: 5% conversione
group_b = np.random.choice([0, 1], size=n, p=[0.90, 0.10])  # Gruppo B: 10% conversione


# Creazione di un DataFrame
data = pd.DataFrame({
    'group': ['A'] * n + ['B'] * n,
    'conversion': np.concatenate([group_a, group_b])
})

# Calcolo delle conversioni per gruppo
conversion_rates = data.groupby('group')['conversion'].mean()
print(conversion_rates)

# Test statistico (test del chi-quadrato) per confrontare le proporzioni
contingency_table = pd.crosstab(data['group'], data['conversion'])
chi2, p_value, _, _ = stats.chi2_contingency(contingency_table)

print(f"Chi2 statistic: {chi2}")
print(f"P-value: {p_value}")

# Interpretazione del risultato
if p_value < 0.05:
    print("C'è una differenza significativa tra i due gruppi.")
else:
    print("Non c'è una differenza significativa tra i due gruppi.")

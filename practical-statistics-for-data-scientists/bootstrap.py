import numpy as np

# Esempio di bootstrapping
def bootstrap(data, num_iterations):
    sample_statistics = []
    n = len(data)
    for _ in range(num_iterations):
        resample = np.random.choice(data, n, replace=True)
        statistic = np.mean(resample)  # Calcola la statistica di interesse (es. media)
        sample_statistics.append(statistic)
    return sample_statistics

# Esempio di confidenza intervallo con bootstrapping
def bootstrap_confidence_interval(data, num_iterations, confidence_level):
    sample_statistics = bootstrap(data, num_iterations)
    alpha = (1 - confidence_level) / 2
    lower_percentile = np.percentile(sample_statistics, alpha * 100)
    upper_percentile = np.percentile(sample_statistics, (1 - alpha) * 100)
    return lower_percentile, upper_percentile

# Esempio di utilizzo
data = np.random.normal(loc=50, scale=10, size=1000)  # Genera dati casuali da una distribuzione normale
confidence_interval = bootstrap_confidence_interval(data, num_iterations=1000, confidence_level=0.95)
print("Confidence interval:", confidence_interval)

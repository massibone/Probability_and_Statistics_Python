import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import genpareto

# Generate example data (casualties)
np.random.seed(0)
casualties = np.random.pareto(2, 1000) * 1000  # Simulated data with a heavy-tailed distribution

# Function to calculate mean excess function
def mean_excess(casualties, threshold):
    exceedances = casualties[casualties > threshold]
    return np.mean(exceedances - threshold)

# Identify the threshold 'u' (could be estimated based on the data characteristics)
threshold = 50000  # Example threshold value

# Calculate mean excess function for different thresholds
thresholds = np.linspace(5000, 100000, 20, dtype=int)
mean_excess_values = [mean_excess(casualties, thresh) for thresh in thresholds]

# Plot mean excess function
plt.figure(figsize=(8, 6))
plt.plot(thresholds, mean_excess_values, marker='o', linestyle='-', color='b')
plt.title('Mean Excess Function (MEPLOT) for War Casualties')
plt.xlabel('Threshold (u)')
plt.ylabel('Mean Excess')
plt.axvline(x=threshold, color='r', linestyle='--', label='Chosen Threshold')
plt.legend()
plt.grid(True)
plt.show()

# Fit Generalized Pareto Distribution (GPD) to exceedances above the chosen threshold
exceedances = casualties[casualties > threshold]
params = genpareto.fit(exceedances - threshold)

# Plot QQ plot for the fitted GPD
plt.figure(figsize=(8, 6))
genpareto.qqplot(exceedances - threshold, dist=params[0], loc=params[1], scale=params[2], line='r')
plt.title('QQ Plot of Exceedances fitted with Generalized Pareto Distribution')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Exceedances')
plt.grid(True)
plt.show()

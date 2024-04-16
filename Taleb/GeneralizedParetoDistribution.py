import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import genpareto

# Example data (casualties above a threshold)
np.random.seed(0)
exceedances = np.random.pareto(2, 500) * 100000  # Simulated exceedances data

# Fit Generalized Pareto Distribution (GPD) to exceedances
params = genpareto.fit(exceedances)

# Parameters of the GPD
xi = params[0]  # Shape parameter
beta = params[2]  # Scale parameter

# Generate GPD distribution
gpd_dist = genpareto(xi, loc=params[1], scale=params[2])

# Plot the GPD cumulative distribution function (CDF) against empirical CDF
plt.figure(figsize=(8, 6))
sorted_exceedances = np.sort(exceedances)
empirical_cdf = np.arange(1, len(sorted_exceedances) + 1) / len(sorted_exceedances)
gpd_cdf = gpd_dist.cdf(sorted_exceedances)
plt.plot(sorted_exceedances, empirical_cdf, label='Empirical CDF')
plt.plot(sorted_exceedances, gpd_cdf, label='GPD CDF')
plt.title('Generalized Pareto Distribution (GPD) Fit to Exceedances')
plt.xlabel('Exceedances')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.grid(True)
plt.show()

# QQ plot for GPD fitting
plt.figure(figsize=(8, 6))
genpareto.qqplot(exceedances, dist=gpd_dist, line='r')
plt.title('QQ Plot of Exceedances fitted with Generalized Pareto Distribution')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Exceedances')
plt.grid(True)
plt.show()

# Print estimated parameters
print(f"Estimated GPD parameters: xi = {xi}, beta = {beta}")

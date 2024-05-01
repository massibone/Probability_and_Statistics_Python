
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto

# Sample data representing casualties above a threshold
casualties = np.random.pareto(0.53, 1000) * 10000  # Example data for L=10K
# Fit Pareto Distribution to casualties exceeding a threshold
alpha, loc, scale = pareto.fit(casualties)

# Generate Pareto distribution
pareto_dist = pareto(alpha, loc=loc, scale=scale)

# Plot the fitted Pareto distribution against the empirical data
plt.figure(figsize=(8, 6))
plt.hist(casualties, bins=30, density=True, alpha=0.6, color='b', label='Empirical Data')
x = np.linspace(casualties.min(), casualties.max(), 100)
plt.plot(x, pareto_dist.pdf(x), 'r-', lw=2, label='Pareto Distribution Fit')
plt.title('Pareto Distribution Fit to Casualties (L=10K)')
plt.xlabel('Casualties')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
# Calculate mean and other statistics
sample_mean = np.mean(casualties)
true_mean = scale * alpha / (alpha - 1) if alpha > 1 else np.inf
ratio = true_mean / sample_mean

print(f"Estimated Parameters: alpha = {alpha:.4f}, scale = {scale:.4f}")
print(f"Sample Mean: {sample_mean:.2f}, True Mean (from Pareto fit): {true_mean:.2f}")
print(f"Ratio of True Mean to Sample Mean: {ratio:.2f}")

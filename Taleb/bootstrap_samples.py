import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import genpareto

# Function to estimate shape parameter (ξ) using Maximum Likelihood Estimation (MLE)
def estimate_shape_parameter(data):
    return genpareto.fit(data)[0]

# Sample data representing casualties exceeding a threshold (e.g., 50k)
data = np.random.pareto(0.53, 1000) * 50000  # Example data for L=50K

# Perform bootstrap analysis to estimate ξ over 100K bootstrap samples
num_bootstrap_samples = 100000
bootstrap_shape_params = []

for _ in range(num_bootstrap_samples):
    # Generate bootstrap sample by sampling with replacement
    bootstrap_sample = np.random.choice(data, size=int(0.9 * len(data)), replace=True)
    
    # Estimate ξ for the bootstrap sample
    bootstrap_ξ = estimate_shape_parameter(bootstrap_sample)
    
    # Store the estimated ξ in the list
    bootstrap_shape_params.append(bootstrap_ξ)

# Plot the distribution of ξ values from bootstrap samples
plt.figure(figsize=(8, 6))
plt.hist(bootstrap_shape_params, bins=50, density=True, alpha=0.6, color='b')
plt.title('Distribution of ξ Parameter over Bootstrap Samples')
plt.xlabel('Shape Parameter (ξ)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Display statistics of the ξ parameter distribution
mean_ξ = np.mean(bootstrap_shape_params)
median_ξ = np.median(bootstrap_shape_params)
std_ξ = np.std(bootstrap_shape_params)

print(f"Mean ξ: {mean_ξ:.4f}")
print(f"Median ξ: {median_ξ:.4f}")
print(f"Standard Deviation of ξ: {std_ξ:.4f}")

'''
Time Preference Under Model Error

In economics, time preference refers to how people value receiving goods or services at different points in time. 
One common method of modeling time preference is through discounting, where future values are weighted less than present values. 
However, this modeling approach can overlook uncertainties and errors in the underlying assumptions.

Imagine you're trying to decide whether to receive a massage today or wait to receive two massages tomorrow. 
According to traditional economic models, this decision should be consistent regardless of when the massages are received. 
However, what if there's uncertainty about the reliability of the person offering the massages? This uncertainty can drastically change your preference.
'''
import numpy as np
import scipy.integrate as integrate

# Define the discounting function H(t) with stochastic discount parameter lambda (λ)
def H(t, lambda_distribution):
    # Integrate over lambda_distribution with the discounting function e^(-lambda * t)
    return integrate.quad(lambda lambda_val: np.exp(-lambda_val * t) * lambda_distribution(lambda_val), -np.inf, np.inf)[0]

# Example: Calculate H(t) under a gamma distribution for lambda (λ)
def gamma_lambda_distribution(lambda_val, alpha, beta):
    return (beta**(-alpha) * lambda_val**(alpha - 1) * np.exp(-lambda_val / beta)) / np.math.gamma(alpha)

# Calculate H(t) for a given time t, gamma distribution parameters alpha and beta
def H_gamma(t, alpha, beta):
    return integrate.quad(lambda lambda_val: np.exp(-lambda_val * t) * gamma_lambda_distribution(lambda_val, alpha, beta), 0, np.inf)[0]

# Calculate the limit of H(t) as t approaches infinity
def limit_H(t, delta_t, alpha, beta):
    return H_gamma(t, alpha, beta) / H_gamma(t - delta_t, alpha, beta)

# Example usage:
alpha = 2  # Shape parameter for gamma distribution
beta = 1   # Scale parameter for gamma distribution
t = 10     # Time
delta_t = 1  # Time difference for limit calculation

result = limit_H(t, delta_t, alpha, beta)
print("Limit of H(t) as t approaches infinity:", result)

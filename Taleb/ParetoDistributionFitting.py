
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto

# Sample data representing casualties above a threshold
casualties = np.random.pareto(0.53, 1000) * 10000  # Example data for L=10K

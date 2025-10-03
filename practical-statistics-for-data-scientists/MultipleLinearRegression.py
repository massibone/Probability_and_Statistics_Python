'''
Uses the California housing dataset to demonstrate regression with multiple predictors.
'''

# Multiple Linear Regression Example
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

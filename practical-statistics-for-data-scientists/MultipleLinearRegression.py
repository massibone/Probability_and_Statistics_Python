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

# Load the California housing dataset
housing = fetch_california_housing()
X = pd.DataFrame(housing.data, columns=housing.feature_names)
y = housing.target

# Print dataset information
print("California Housing Dataset:")
print(f"Number of samples: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")
print("\nFeatures:")
for feature in housing.feature_names:
    print(f"- {feature}")

# Select a subset of features for clarity
selected_features = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms']
X_selected = X[selected_features]

# Display the first few rows of the data
print("\nFirst 5 rows of selected features:")
print(X_selected.head())
print("\nFirst 5 target values (median house value in $100,000):")
print(y[:5])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_selected, y, test_size=0.2, random_state=42
)
print(f"\nTraining set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")

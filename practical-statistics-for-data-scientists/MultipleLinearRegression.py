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
# Fit the multiple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Print model parameters
print("\nMultiple Linear Regression Results:")
print(f"Intercept (b₀): {model.intercept_:.4f}")
print("Coefficients:")
for feature, coef in zip(selected_features, model.coef_):
    print(f"  {feature}: {coef:.4f}")


# Formulate the regression equation
equation = f"y = {model.intercept_:.4f}"
for feature, coef in zip(selected_features, model.coef_):
    if coef >= 0:
        equation += f" + {coef:.4f} × {feature}"
    else:
        equation += f" - {abs(coef):.4f} × {feature}"
print(f"\nRegression Equation:\n{equation}")

# Make predictions on test data
y_pred_test = model.predict(X_test)
# Calculate performance metrics
r2_train = model.score(X_train, y_train)
r2_test = r2_score(y_test, y_pred_test)
rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))

print("\nModel Performance:")
print(f"R² Score (Training): {r2_train:.4f}")
print(f"R² Score (Testing): {r2_test:.4f}")
print(f"RMSE (Testing): {rmse_test:.4f}")

# Plot actual vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_test, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Values', fontsize=12)
plt.ylabel('Predicted Values', fontsize=12)
plt.title('Actual vs Predicted House Values', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Plot residuals
residuals = y_test - y_pred_test
plt.figure(figsize=(10, 6))
plt.scatter(y_pred_test, residuals, alpha=0.7)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted Values', fontsize=12)
plt.ylabel('Residuals', fontsize=12)
plt.title('Residual Plot', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Feature importance visualization
plt.figure(figsize=(10, 6))
plt.bar(selected_features, model.coef_)
plt.xlabel('Features', fontsize=12)
plt.ylabel('Coefficient Value', fontsize=12)
plt.title('Feature Importance', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

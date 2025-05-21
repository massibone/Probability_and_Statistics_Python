'''
Shows how to fit a basic model, make predictions, 
and evaluate performance with R² and RMSE metrics.
'''

# Simple Linear Regression Example
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Create sample data
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # Feature values between 0 and 10
y = 5 + 2 * X.flatten() + np.random.randn(100) * 2  # Target with noise

# Fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Print model parameters
print("Simple Linear Regression Results:")
print(f"Intercept (b₀): {model.intercept_:.3f}")
print(f"Slope (b₁): {model.coef_[0]:.3f}")
print(f"Equation: y = {model.intercept_:.3f} + {model.coef_[0]:.3f} * x")

# Make predictions
X_test = np.array([[2], [5], [8]])
predictions = model.predict(X_test)
print("\nPredictions:")
for x, pred in zip(X_test.flatten(), predictions):
    print(f"When x = {x}, predicted y = {pred:.3f}")

# Calculate performance metrics
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))
print(f"\nModel Performance:")
print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

# Plot the data and regression line
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', alpha=0.7, label='Data points')
plt.plot(X, y_pred, color='red', linewidth=2, label='Regression line')

# Add equation text to plot
equation = f"y = {model.intercept_:.3f} + {model.coef_[0]:.3f}x"
plt.text(1, np.max(y) - 2, f"Equation: {equation}", fontsize=12)
plt.text(1, np.max(y) - 4, f"R² = {r2:.4f}", fontsize=12)

plt.title('Simple Linear Regression', fontsize=14)
plt.xlabel('X (Independent Variable)', fontsize=12)
plt.ylabel('y (Dependent Variable)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# Visualize residuals
residuals = y - y_pred
plt.figure(figsize=(10, 6))
plt.scatter(X, residuals, color='green', alpha=0.7)
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Residual Plot', fontsize=14)
plt.xlabel('X (Independent Variable)', fontsize=12)
plt.ylabel('Residuals (y - ŷ)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

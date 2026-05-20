'''Creates a quadratic model to fit non-linear data by transforming features.
'''
# Polynomial Regression Example
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

# Create nonlinear data
np.random.seed(42)
X = np.random.rand(100, 1) * 5  # Feature values between 0 and 5
y = 2 + 3*X.flatten() - 0.5*X.flatten()**2 + np.random.randn(100) * 1.5  # Quadratic relationship with noise

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# First, fit a simple linear model for comparison
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Create polynomial features (degree=2)
poly_transformer = PolynomialFeatures(degree=2)
X_train_poly = poly_transformer.fit_transform(X_train)  # Creates [1, x, x²]
X_test_poly = poly_transformer.transform(X_test)

# Fit polynomial regression model
poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

# Print model parameters
print("Polynomial Regression Results (Degree 2):")
print(f"Intercept: {poly_model.intercept_:.4f}")
print(f"Coefficients: {poly_model.coef_}")
print(f"Equation: y = {poly_model.intercept_:.4f} + {poly_model.coef_[1]:.4f}x + {poly_model.coef_[2]:.4f}x²")

# Make predictions
y_train_pred_linear = linear_model.predict(X_train)
y_test_pred_linear = linear_model.predict(X_test)
y_train_pred_poly = poly_model.predict(X_train_poly)
y_test_pred_poly = poly_model.predict(X_test_poly)

# Calculate performance metrics
r2_train_linear = r2_score(y_train, y_train_pred_linear)
r2_test_linear = r2_score(y_test, y_test_pred_linear)
r2_train_poly = r2_score(y_train, y_train_pred_poly)
r2_test_poly = r2_score(y_test, y_test_pred_poly)

rmse_train_linear = np.sqrt(mean_squared_error(y_train, y_train_pred_linear))
rmse_test_linear = np.sqrt(mean_squared_error(y_test, y_test_pred_linear))
rmse_train_poly = np.sqrt(mean_squared_error(y_train, y_train_pred_poly))
rmse_test_poly = np.sqrt(mean_squared_error(y_test, y_test_pred_poly))

print("\nPerformance Comparison:")
print("Linear Regression:")
print(f"  R² Score (Training): {r2_train_linear:.4f}")
print(f"  R² Score (Testing): {r2_test_linear:.4f}")
print(f"  RMSE (Training): {rmse_train_linear:.4f}")
print(f"  RMSE (Testing): {rmse_test_linear:.4f}")

print("\nPolynomial Regression:")
print(f"  R² Score (Training): {r2_train_poly:.4f}")
print(f"  R² Score (Testing): {r2_test_poly:.4f}")
print(f"  RMSE (Training): {rmse_train_poly:.4f}")
print(f"  RMSE (Testing): {rmse_test_poly:.4f}")

# Generate smooth curve for plotting
X_plot = np.linspace(0, 5, 100).reshape(-1, 1)
X_plot_poly = poly_transformer.transform(X_plot)
y_plot_linear = linear_model.predict(X_plot)
y_plot_poly = poly_model.predict(X_plot_poly)

# Plot results
plt.figure(figsize=(12, 6))

# Plot training data
plt.scatter(X_train, y_train, color='blue', alpha=0.7, label='Training Data')
plt.scatter(X_test, y_test, color='green', alpha=0.7, label='Testing Data')

# Plot regression lines
plt.plot(X_plot, y_plot_linear, color='red', linewidth=2, label='Linear Regression')
plt.plot(X_plot, y_plot_poly, color='purple', linewidth=2, label='Polynomial Regression (degree=2)')

# Add equations to plot
linear_eq = f"y = {linear_model.intercept_:.2f} + {linear_model.coef_[0]:.2f}x"
poly_eq = f"y = {poly_model.intercept_:.2f} + {poly_model.coef_[1]:.2f}x + {poly_model.coef_[2]:.2f}x²"

plt.annotate(linear_eq, xy=(0.05, 0.95), xycoords='axes fraction', fontsize=10, 
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
             
plt.annotate(poly_eq, xy=(0.05, 0.88), xycoords='axes fraction', fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))

plt.title('Linear vs Polynomial Regression', fontsize=14)
plt.xlabel('X', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# Try different polynomial degrees
degrees = [1, 2, 3, 4, 5]
train_scores = []
test_scores = []

plt.figure(figsize=(12, 10))

for i, degree in enumerate(degrees):
    # Create polynomial features
    poly = PolynomialFeatures(degree=degree)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    
    # Fit model
    poly_model = LinearRegression()
    poly_model.fit(X_train_poly, y_train)
    
    # Calculate scores
    train_score = r2_score(y_train, poly_model.predict(X_train_poly))
    test_score = r2_score(y_test, poly_model.predict(X_test_poly))
    train_scores.append(train_score)
    test_scores.append(test_score)
    
    # Generate predictions for plot
    X_plot_poly = poly.transform(X_plot)
    y_plot_poly = poly_model.predict(X_plot_poly)
    
    # Plot
    plt.subplot(2, 3, i+1)
    plt.scatter(X_train, y_train, color='blue', alpha=0.4, label='Training')
    plt.scatter(X_test, y_test, color='green', alpha=0.4, label='Testing')
    plt.plot(X_plot, y_plot_poly, color='red', linewidth=2)
    plt.title(f'Degree {degree}', fontsize=12)
    plt.xlabel('X')
    plt.ylabel('y')
    if i == 0:
        plt.legend()

plt.tight_layout()
plt.show()

# Plot R² vs Degree
plt.figure(figsize=(10, 6))
plt.plot(degrees, train_scores, marker='o', label='Training R²')
plt.plot(degrees, test_scores, marker='s', label='Testing R²')
plt.xlabel('Polynomial Degree', fontsize=12)
plt.ylabel('R² Score', fontsize=12)
plt.title('Model Performance vs Polynomial Degree', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

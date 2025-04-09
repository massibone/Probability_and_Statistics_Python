'''
Compares standard linear regression with Ridge and Lasso regularization on a dataset with many features but where only a few actually matter.
'''
# Regularized Regression Example
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.pipeline import Pipeline

# Create dataset with many features but only a few are relevant
np.random.seed(42)
n_samples = 100
n_features = 20

# Create the feature matrix with random values
X = np.random.randn(n_samples, n_features)

# Only the first 5 features actually influence the target
true_coef = np.zeros(n_features)
true_coef[:5] = [2.5, -1.0, 3.0, -0.5, 1.0]

# Generate target with some noise
y = np.dot(X, true_coef) + np.random.randn(n_samples) * 2

# Create feature names for clarity
feature_names = [f"Feature_{i+1}" for i in range(n_features)]
X_df = pd.DataFrame(X, columns=feature_names)

# Print dataset information
print(f"Dataset shape: {X.shape}")
print(f"Number of actually relevant features: 5 (out of {n_features})")
print(f"True coefficients: {true_coef[:5]} for the first 5 features, 0 for the rest")

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Fit different regression models
# 1. Standard Linear Regression
linear_reg = LinearRegression()
linear_reg.fit(X_train_scaled, y_train)

# 2. Ridge Regression (L2 regularization)
ridge_reg = Ridge(alpha=1.0)  # alpha controls the strength of regularization
ridge_reg.fit(X_train_scaled, y_train)

# 3. Lasso Regression (L1 regularization)
lasso_reg = Lasso(alpha=0.1)
lasso_reg.fit(X_train_scaled, y_train)

# Print coefficients
pd.set_option('display.precision', 3)
coef_df = pd.DataFrame({
    'True': true_coef,
    'Linear': linear_reg.coef_,
    'Ridge': ridge_reg.coef_,
    'Lasso': lasso_reg.coef_
}, index=feature_names)

print("\nModel Coefficients (first 10 features):")
print(coef_df.head(10))

# Make predictions
y_pred_linear = linear_reg.predict(X_test_scaled)
y_pred_ridge = ridge_reg.predict(X_test_scaled)
y_pred_lasso = lasso_reg.predict(X_test_scaled)

# Calculate performance metrics
results = {
    'Linear Regression': {
        'R²': r2_score(y_test, y_pred_linear),
        'RMSE': np.sqrt(mean_squared_error(y_test, y_pred_linear)),
        'Non-zero coefficients': np.sum(np.abs(linear_reg.coef_) > 1e-6)
    },
    'Ridge Regression': {
        'R²': r2_score(y_test, y_pred_ridge),
        'RMSE': np.sqrt(mean_squared_error(y_test, y_pred_ridge)),
        'Non-zero coefficients': np.sum(np.abs(ridge_reg.coef_) > 1e-6)
    },
    'Lasso Regression': {
        'R²': r2_score(y_test, y_pred_lasso),
        'RMSE': np.sqrt(mean_squared_error(y_test, y_pred_lasso)),
        'Non-zero coefficients': np.sum(np.abs(lasso_reg.coef_) > 1e-6)
    }
}

# Print results table
print("\nModel Performance:")
results_df = pd.DataFrame(results).T
print(results_df)

# Plot coefficients
plt.figure(figsize=(12, 6))
plt.plot(range(n_features), true_coef, 'o', label='True Coefficients', markersize=10)
plt.plot(range(n_features), linear_reg.coef_, '^', label='Linear Regression')
plt.plot(range(n_features), ridge_reg.coef_, 's', label='Ridge (L2)')
plt.plot(range(n_features), lasso_reg.coef_, 'd', label='Lasso (L1)')
plt.axhline(y=0, color='gray', linestyle='--', alpha=0.3)
plt.xlabel('Feature Number', fontsize=12)
plt.ylabel('Coefficient Value', fontsize=12)
plt.title('Comparison of Regression Coefficients', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# Plot predicted vs actual values
plt.figure(figsize=(15, 5))

# Linear Regression
plt.subplot(1, 3, 1)
plt.scatter(y_test, y_pred_linear, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title('Linear Regression', fontsize=12)
plt.xlabel('Actual Values', fontsize=10)
plt.ylabel('Predicted Values', fontsize=10)
plt.grid(True, alpha=0.3)

# Ridge Regression
plt.subplot(1, 3, 2)
plt.scatter(y_test, y_pred_ridge, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title('Ridge Regression', fontsize=12)
plt.xlabel('Actual Values', fontsize=10)
plt.grid(True, alpha=0.3)

# Lasso Regression
plt.subplot(1, 3, 3)
plt.scatter(y_test, y_pred_lasso, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title('Lasso Regression', fontsize=12)
plt.xlabel('Actual Values', fontsize=10)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Regularization path for Lasso
print("\nExploring different alpha values for Lasso regression...")
alphas = np.logspace(-5, 2, 8)
coefs = []
r2_scores = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha, max_iter=10000)
    lasso.fit(X_train_scaled, y_train)
    coefs.append(lasso.coef_)
    y_pred = lasso.predict(X_test_scaled)
    r2_scores.append(r2_score(y_test, y_pred))

# Plot regularization path
plt.figure(figsize=(12, 10))

# Coefficient paths
plt.subplot(2, 1, 1)
for i, coef_path in enumerate(np.array(coefs).T):
    plt.plot(alphas, coef_path, '-', label=f'Feature {i+1}' if i < 5 else None)

plt.axhline(y=0, color='k', linestyle='--', alpha=0.4)
plt.xscale('log')
plt.xlabel('Alpha (regularization strength)', fontsize=12)
plt.ylabel('Coefficient value', fontsize=12)
plt.title('Lasso Regularization Path', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right')

# Performance by alpha
plt.subplot(2, 1, 2)
plt.plot(alphas, r2_scores, 'o-')
plt.xscale('log')
plt.xlabel('Alpha (regularization strength)', fontsize=12)
plt.ylabel('R² Score', fontsize=12)
plt.title('Lasso Performance vs Alpha', fontsize=14)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Find optimal alpha using cross-validation
print("\nFinding optimal alpha values using cross-validation...")

# Define pipelines with built-in cross-validation
ridge_cv = GridSearchCV(
    Ridge(),
    {'alpha': np.logspace(-3, 3, 7)},
    cv=5,
    scoring='neg_mean_squared_error'
)

lasso_cv = GridSearchCV(
    Lasso(max_iter=10000),
    {'alpha': np.logspace(-5, 0, 6)},
    cv=5,
    scoring='neg_mean_squared_error'
)

# Fit models
ridge_cv.fit(X_train_scaled, y_train)
lasso_cv.fit(X_train_scaled, y_train)

# Print best parameters
print(f"Best Ridge alpha: {ridge_cv.best_params_['alpha']}")
print(f"Best Lasso alpha: {lasso_cv.best_params_['alpha']}")

# Fit final models with optimal parameters
best_ridge = Ridge(alpha=ridge_cv.best_params_['alpha'])
best_lasso = Lasso(alpha=lasso_cv.best_params_['alpha'], max_iter=10000)

best_ridge.fit(X_train_scaled, y_train)
best_lasso.fit(X_train_scaled, y_train)

# Print final coefficients for optimal models
coef_df_optimal = pd.DataFrame({
    'True': true_coef,
    'Ridge (optimal)': best_ridge.coef_,
    'Lasso (optimal)': best_lasso.coef_
}, index=feature_names)

print("\nOptimal Model Coefficients (first 10 features):")
print(coef_df_optimal.head(10))

# Final comparison plot
plt.figure(figsize=(10, 6))
plt.plot(range(n_features), true_coef, 'o', label='True Coefficients', markersize=10)
plt.plot(range(n_features), best_ridge.coef_, 's', label='Ridge (optimal alpha)')
plt.plot(range(n_features), best_lasso.coef_, 'd', label='Lasso (optimal alpha)')
plt.axhline(y=0, color='gray', linestyle='--', alpha=0.3)
plt.xlabel('Feature Number', fontsize=12)
plt.ylabel('Coefficient Value', fontsize=12)
plt.title('Comparison of Optimal Regularized Models', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

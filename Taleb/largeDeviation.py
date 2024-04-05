import pandas as pd

def analyze_large_deviations(data, threshold_pct=0.04, window=30, pre_window=5, post_window=5):
  """
  Analyzes large deviations in stock prices.

  Args:
      data (pd.DataFrame): DataFrame containing daily closing prices (column name 'Close').
      threshold_pct (float, optional): Threshold percentage for large deviations (default: 0.04).
      window (int, optional): Window size for calculating average closing price (default: 30).
      pre_window (int, optional): Window size for analyzing predecessors (default: 5).
      post_window (int, optional): Window size for analyzing successors (default: 5).

  Returns:
      pd.DataFrame: DataFrame containing information about large deviations.
  """
  
 # Calculate daily absolute deviations
  data['Average_Close'] = data['Close'].rolling(window=window).mean()
  data['Abs_Deviation'] = abs(data['Close'] - data['Average_Close'])

  # Identify large deviations
  large_deviations = data[data['Abs_Deviation'] > data['Average_Close'] * threshold_pct]

  # Analyze predecessors and successors
  large_deviations['Precursors'] = large_deviations['Abs_Deviation'].shift(1).rolling(pre_window).sum() > data['Average_Close'] * threshold_pct * pre_window
  large_deviations['Successors'] = large_deviations['Abs_Deviation'].shift(-1).rolling(post_window).sum() > data['Average_Close'] * threshold_pct * post_window

  # Return results
  return large_deviations

# Assuming you have your daily price data in a pandas DataFrame named 'stock_data'
large_deviations_df = analyze_large_deviations(stock_data)

# Print information about large deviations
print(large_deviations_df)

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
  

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

def load_multiple_sessions(file_path):
    """Carica dati per multiple sessioni"""
    return pd.read_csv(file_path)

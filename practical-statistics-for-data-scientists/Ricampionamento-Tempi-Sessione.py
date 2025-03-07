import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from pathlib import Path

def load_session_data(file_path):
    """Carica e prepara i dati delle sessioni"""
    session_times = pd.read_csv(file_path)
    session_times.Time = 100 * session_times.Time
    return session_times

import numpy as np
from scipy import stats
import pandas as pd

def run_fishers_exact(table, verbose=True):
    """
    Esegue il test esatto di Fisher su una tabella di contingenza 2x2
    
    Parameters:
    -----------
    table : array-like
        Tabella di contingenza 2x2
    verbose : bool, optional
        Se True, stampa i risultati dettagliati
        
    Returns:
    --------
    

    odds_ratio : float
        Rapporto delle probabilità
    p_value : float
        p-value del test
    """
    # Converti in array numpy se necessario
    if isinstance(table, pd.DataFrame):
        table = table.values
    

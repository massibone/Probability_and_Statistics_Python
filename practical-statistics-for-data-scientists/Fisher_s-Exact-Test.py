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
    

    # Esegui il test
    odds_ratio, p_value = stats.fisher_exact(table)
    
    if verbose:
        print("\nTabella di contingenza:")
        print(pd.DataFrame(table, 
                         columns=['Gruppo B -', 'Gruppo B +'],
                         index=['Gruppo A -', 'Gruppo A +']))
        print(f"\nOdds Ratio: {odds_ratio:.4f}")
        print(f"P-value: {p_value:.4f}")
  
        # Interpreta il risultato
        alpha = 0.05
        print(f"\nInterpretazione (α = {alpha}):")
        if p_value < alpha:
            print("Rifiutiamo l'ipotesi nulla - c'è un'associazione significativa")
        else:
            print("Non possiamo rifiutare l'ipotesi nulla - non c'è evidenza di associazione")      

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
        
    
    return odds_ratio, p_value

# Esempio di utilizzo
if __name__ == "__main__":
    # Esempio: Studio clinico con due gruppi di trattamento
    # Righe: Trattamento A (+ / -)
    # Colonne: Trattamento B (+ / -)
    example_table = np.array([[10, 2],   # 10 negativi-negativi, 2 negativi-positivi
                             [1, 12]])    # 1 positivo-negativo, 12 positivi-positivi

    # Esegui il test
    odds_ratio, p_value = run_fishers_exact(example_table)
   

    # Esempio con DataFrame
    df_table = pd.DataFrame(example_table,
                          columns=['Gruppo B -', 'Gruppo B +'],
                          index=['Gruppo A -', 'Gruppo A +'])
    
    # Esegui il test con DataFrame
    odds_ratio, p_value = run_fishers_exact(df_table)

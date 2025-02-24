'''
un'analisi statistica comparativa dei tempi di sessione tra due pagine web utilizzando un t-test indipendente. Specificatamente:

Crea un dataset simulato con tempi di sessione per due pagine (Page A e Page B)
Applica un test t di Welch per confrontare statisticamente le medie dei tempi di sessione
Calcola e stampa il p-value per un test unilaterale
Mostra le medie dei tempi di sessione per ciascuna pagina

L'obiettivo è determinare se esiste una differenza statisticamente significativa nei tempi di sessione tra le due pagine, utilizzando un approccio che non assume varianze uguali.
'''
import pandas as pd
import scipy.stats as stats

# Creazione di un DataFrame di esempio
data = {
    'Page': ['Page A']*20 + ['Page B']*20,
    'Time': [
        # Tempi di sessione per Page A (esempio)
        45, 52, 48, 50, 47, 
        53, 49, 51, 46, 44, 
        55, 48, 52, 50, 47, 
        54, 49, 51, 46, 45,
        # Tempi di sessione per Page B (esempio)
        58, 62, 55, 60, 57, 
        63, 59, 61, 56, 54, 
        65, 58, 62, 60, 57, 
        64, 59, 61, 56, 55
    ]
}

# Creazione del DataFrame
session_times = pd.DataFrame(data)

# Esecuzione del t-test
res = stats.ttest_ind(
    session_times[session_times.Page == 'Page A'].Time, 
    session_times[session_times.Page == 'Page B'].Time, 
    equal_var=False  # Test di Welch (varianze non uguali)
)

# Stampa dei risultati
print(f'Statistica t: {res.statistic:.4f}')
print(f'p-value per test unilaterale: {res.pvalue / 2:.4f}')

# Confronto delle medie dei tempi di sessione
mean_page_a = session_times[session_times.Page == 'Page A'].Time.mean()
mean_page_b = session_times[session_times.Page == 'Page B'].Time.mean()
print(f'Media tempi di sessione Page A: {mean_page_a:.2f}')
print(f'Media tempi di sessione Page B: {mean_page_b:.2f}')

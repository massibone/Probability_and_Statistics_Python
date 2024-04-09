'''
Questa tabella presenta diversi metodi per valutare le prestazioni di un modello di previsione o di un sistema di trading. Ecco una spiegazione di ciascuna delle metriche elencate:
P(r)(T) - Cumulative P/L: Questa metrica rappresenta il profitto/perdita cumulativo del sistema di trading. È adattata alle distribuzioni del mondo reale, in particolare sotto un "filtro di sopravvivenza", il che significa che tiene conto della capacità del sistema di sopravvivere a condizioni di mercato avverse.
P(p)(n) - Tally of Bets: Questa metrica conta semplicemente il numero di scommesse effettuate dal sistema. Tuttavia, essa può essere fuorviante in presenza di code pesanti (fat tails) nella distribuzione dei rendimenti, e funziona solo per scommesse binarie o domini a code sottili.
λ(n) - Brier Score: Il Brier Score è una misura della precisione delle previsioni, ma non rappresenta accuratamente la performance in presenza di code pesanti, e ignora i momenti di ordine superiore della distribuzione.
λ(M4)n - M4 Score: Questa metrica rappresenta meglio la precisione, ma non esattamente la performance del mondo reale. Tuttavia, essa mappa la distribuzione reale delle variabili sottostanti.
λ(M5)n - Proposed M5 Score: Questa è una metrica proposta che rappresenta sia la precisione che le condizioni di sopravvivenza, prevedendo gli estremi della serie temporale.
g(.) - Machine learning nonlinear payoff function: Questa non è una metrica, ma piuttosto una funzione di payoff non lineare derivata da tecniche di machine learning. Essa esprime le esposizioni senza verbosità e riflette il vero profitto/perdita economico o di altro tipo, assomigliando ai termini di contratti finanziari derivati.
In sintesi, questa tabella confronta diverse metriche per valutare le prestazioni di sistemi di previsione e trading, evidenziando i loro punti di forza e debolezza in relazione alla capacità di rappresentare fedelmente la realtà del mondo finanziario.
'''

import numpy as np
import matplotlib.pyplot as plt

# Dati di esempio
true_values = np.random.normal(0, 1, 1000)
predicted_values = np.random.normal(0, 1.2, 1000)
bets = np.random.randint(0, 2, 1000)

# Metriche di performance

def P_r_T(true_values, predicted_values):
    """Cumulative P/L"""
    return np.sum(true_values * predicted_values)

def P_p_n(bets):
    """Tally of Bets"""
    return len(bets)

def brier_score(true_values, predicted_values):
    """Brier Score"""
    return np.mean((true_values - predicted_values)**2)

def M4_score(true_values, predicted_values):
    """M4 Score"""
    return np.mean(np.abs(true_values - predicted_values)**4)

def M5_score(true_values, predicted_values):
    """Proposed M5 Score"""
    return np.mean(np.maximum(np.abs(true_values), np.abs(predicted_values)))

def nonlinear_payoff(true_values, predicted_values):
    """Machine learning nonlinear payoff function"""
    return np.sum(np.maximum(0, true_values * predicted_values))

# Calcolo delle metriche
P_r_T_value = P_r_T(true_values, predicted_values)
P_p_n_value = P_p_n(bets)
brier_score_value = brier_score(true_values, predicted_values)
M4_score_value = M4_score(true_values, predicted_values)
M5_score_value = M5_score(true_values, predicted_values)
nonlinear_payoff_value = nonlinear_payoff(true_values, predicted_values)

# Grafico riepilogativo
metric_names = ['Cumulative P/L', 'Tally of Bets', 'Brier Score', 'M4 Score', 'M5 Score', 'Nonlinear Payoff']
metric_values = [P_r_T_value, P_p_n_value, brier_score_value, M4_score_value, M5_score_value, nonlinear_payoff_value]

plt.figure(figsize=(12, 6))
plt.bar(metric_names, metric_values)
plt.xticks(rotation=90)
plt.title('Scoring Metrics for Performance Evaluation')
plt.xlabel('Metric Name')
plt.ylabel('Value')
plt.tight_layout()
plt.show()
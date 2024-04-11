'''
 immagina che abbiamo dei dati. Questi dati sono come i pezzi di un puzzle che dobbiamo mettere insieme per capire qualcosa. Ma non è un puzzle normale, è un puzzle con pezzi strani che saltano ovunque!

Ci sono due modi principali per cercare di capire questi dati: uno è chiamato "estimatore non parametrico" e l'altro è chiamato "estimatore massima verosimiglianza" (MLE). Sono come due strumenti diversi che possiamo usare per risolvere il nostro puzzle.

Ora, quando i pezzi del nostro puzzle sono davvero strani, cioè i dati hanno code grasse (come code di dinosauro!), l'estimatore non parametrico può diventare un po' confuso. Quindi, utilizziamo l'estimatore massima verosimiglianza perché è migliore con questi tipi di dati strani.

Prendiamo ad esempio una distribuzione chiamata "Pareto". Questa distribuzione ha una forma particolare, come una montagna molto alta che si allarga in basso. Utilizzando l'estimatore massima verosimiglianza con questa distribuzione, possiamo ottenere stime molto buone del valore che stiamo cercando.

Quindi, abbiamo fatto alcune prove e abbiamo scoperto che l'estimatore massima verosimiglianza funziona meglio dell'estimatore non parametrico quando si tratta di dati strani come quelli della distribuzione Pareto. Abbiamo anche trovato quanti dati sono necessari per ottenere stime simili tra i due tipi di estimatori. È come trovare il numero giusto di pezzi di puzzle per risolvere il nostro mistero!
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto
from scipy.optimize import minimize

# Genera dati da una distribuzione Pareto
def generate_data(alpha, size):
    return pareto.rvs(alpha, size=size)

# Calcola il Gini index
def gini_index(data):
    n = len(data)
    data = np.sort(data)
    coef = 2 / n
    indexes = np.arange(1, n + 1)
    weighted_sum = (indexes * data).sum()
    total = data.sum()
    return coef * weighted_sum / total - (n + 1) / n

# Funzione di log-verosimiglianza per la distribuzione Pareto
def log_likelihood(params, data):
    alpha = params[0]
    return -np.sum(pareto.logpdf(data, alpha))

# Stima del parametro alpha della distribuzione Pareto tramite MLE
def estimate_alpha(data):
    result = minimize(log_likelihood, [1], args=(data,))
    return result.x[0]

# Calcola il Gini index stimato utilizzando l'estimatore non parametrico
def estimate_gini_nonparametric(data):
    return gini_index(data)

# Calcola il Gini index stimato utilizzando l'estimatore MLE
def estimate_gini_mle(data):
    alpha = estimate_alpha(data)
    return gini_index(pareto.rvs(alpha, size=len(data)))

# Dimensioni del campione
sample_sizes = [1000, 5000, 10000]

for size in sample_sizes:
    # Genera dati
    data = generate_data(2, size)

    # Stima del Gini index utilizzando l'estimatore non parametrico
    gini_nonparametric = estimate_gini_nonparametric(data)

    # Stima del Gini index utilizzando l'estimatore MLE
    gini_mle = estimate_gini_mle(data)

    print(f"Dimensione campione: {size}")
    print(f"Gini Index stimato (Non Parametrico): {gini_nonparametric}")
    print(f"Gini Index stimato (MLE): {gini_mle}")
    print()

# Plot dei risultati
plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, [gini_index(generate_data(2, size)) for size in sample_sizes], label='Gini Index reale', marker='o')
plt.plot(sample_sizes, [estimate_gini_nonparametric(generate_data(2, size)) for size in sample_sizes], label='Estimatore Non Parametrico', marker='o')
plt.plot(sample_sizes, [estimate_gini_mle(generate_data(2, size)) for size in sample_sizes], label='Estimatore MLE', marker='o')
plt.xlabel('Dimensione Campione')
plt.ylabel('Gini Index')
plt.title('Confronto tra Estimatori Non Parametrico e MLE')
plt.legend()
plt.grid(True)
plt.show()

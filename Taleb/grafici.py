'''
Esempio 1: Grafico a barre per le distribuzioni dei parametri
Esempio 2: Grafico della media campionaria e della media MLE
Esempio 3: Grafico log-log per confrontare f e g

'''

import matplotlib.pyplot as plt
import numpy as np

# Dati per il primo grafico (istogramma delle distribuzioni di ξ)
xi_raw = [1.2, 1.5, 1.8, 2.0, 1.3, 1.9, 2.2, 2.5, 1.7, 2.1]  # Lista dei valori ξ per i dati grezzi
xi_rescaled = [1.2, 1.5, 1.8, 2.0, 1.3, 1.9, 2.2, 2.5, 1.7, 2.1]  # Lista dei valori ξ per i dati rescaled
xi_log_rescaled = [1.2, 1.5, 1.8, 2.0, 1.3, 1.9, 2.2, 2.5, 1.7, 2.1]  # Lista dei valori ξ per i dati log-rescaled

# Dati per il secondo grafico (istogramma delle medie campionarie e MLE)
sample_means = [1.2, 1.5, 1.8, 2.0, 1.3, 1.9, 2.2, 2.5, 1.7, 2.1]  # Lista delle medie campionarie
mle_means = [1.2, 1.5, 1.8, 2.0, 1.3, 1.9, 2.2, 2.5, 1.7, 2.1]  # Lista delle medie MLE

# Dati per il terzo grafico (grafico log-log per confronto f e g)
x_values = [1.2, 1.5, 1.8, 2.0, 1.3, 1.9, 2.2, 2.5, 1.7, 2.1]  # Lista dei valori x per f
p_values = [1.2, 1.5, 1.8, 2.0, 1.3, 1.9, 2.2, 2.5, 1.7, 2.1]  # Lista dei valori p per f

# Creazione della figura e dei tre subplot
fig, axs = plt.subplots(3, 1, figsize=(10, 18))

# Primo subplot: Istogramma delle distribuzioni di ξ
axs[0].hist(xi_raw, bins=30, alpha=0.5, label='Raw Data')
axs[0].hist(xi_rescaled, bins=30, alpha=0.5, label='Naively Rescaled Data')
axs[0].hist(xi_log_rescaled, bins=30, alpha=0.5, label='Log-Rescaled Data')
axs[0].set_xlabel('Valore di ξ')
axs[0].set_ylabel('Frequenza')
axs[0].set_title('Distribuzione dei parametri ξ')
axs[0].legend()

# Secondo subplot: Istogramma delle medie campionarie e MLE
axs[1].hist(sample_means, bins=30, alpha=0.5, label='Media Campionaria')
axs[1].hist(mle_means, bins=30, alpha=0.5, label='Media MLE')
axs[1].set_xlabel('Valore della media')
axs[1].set_ylabel('Frequenza')
axs[1].set_title('Distribuzione delle medie campionarie e MLE')
axs[1].legend()

# Terzo subplot: Grafico log-log per confronto f e g
axs[2].loglog(x_values, p_values, label='f')
axs[2].set_xlabel('Log(x)')
axs[2].set_ylabel('Log(P > x)')
axs[2].set_title('Confronto log-log tra f e g')
axs[2].legend()

# Spaziatura tra i subplot per migliorare la leggibilità
plt.tight_layout()

# Mostra i grafici
plt.show()

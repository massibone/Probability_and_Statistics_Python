import numpy as np
import matplotlib.pyplot as plt

# Dati ipotetici sul numero di auto vendute
auto_vendute = [4000, 5500, 6500, 3000, 7500, 9000, 6000, 3500, 8000, 7000]

# Calcola la media e la deviazione standard delle auto vendute
media = np.mean(auto_vendute)
deviazione_standard = np.std(auto_vendute)


def disuguaglianza_chebyshev(dati, media, deviazione_standard, k):
    numeratore = k * deviazione_standard
    disuguaglianza = sum(
        abs(x - media) >= numeratore for x in dati) / len(dati)
    return disuguaglianza


# Imposta i valori di k per la disuguaglianza di Chebyshev
valori_k = [1, 2, 3, 4, 5]

# Calcola la disuguaglianza di Chebyshev per diversi valori di k
disuguaglianze = [disuguaglianza_chebyshev(
    auto_vendute, media, deviazione_standard, k) for k in valori_k]

# Crea un grafico per visualizzare i risultati
plt.plot(valori_k, disuguaglianze, marker='o',
         label='Disuguaglianza di Chebyshev')
plt.axhline(y=1, color='r', linestyle='--', label='Media')
plt.axhline(y=0, color='g', linestyle='--', label='Deviazione Standard')
plt.xlabel('k')
plt.ylabel('Percentuale')
plt.title('Disuguaglianza di Chebyshev vs. k per le auto più vendute')
plt.legend()
plt.grid(True)
plt.show()

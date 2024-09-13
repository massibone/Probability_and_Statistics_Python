'''
he simula il lancio ripetuto di un dado speciale chiamato "Dado α-stabile". Ogni volta che lanciamo questo dado, otteniamo un numero magico anziché un numero normale da uno a sei.

Ogni numero magico che otteniamo ha alcune caratteristiche speciali:

α (la stranezza): Questo ci dice quanto sono grandi i salti tra i numeri magici. Se α è basso, i numeri magici sono abbastanza "normali", ma se α è alto, allora i numeri magici possono saltare molto da uno all'altro.

β (l'inclinazione): Questo ci dice se la distribuzione dei numeri magici è inclinata in un certo modo. Se β è positivo, i numeri magici tendono ad essere inclinati da un lato, mentre se è negativo, sono inclinati dall'altro lato.

γ (la larghezza): Questo ci dice quanto sono distribuiti i numeri magici. Se γ è grande, i numeri magici sono distribuiti molto lontano l'uno dall'altro, mentre se è piccolo, sono più vicini tra loro.

δ (la posizione): Questo ci dice dove si trova il "centro" dei numeri magici. Se δ è 3, il centro dei numeri magici è intorno al numero 3.

Il nostro codice simula il lancio del dado α-stabile un numero crescente di volte, e poi calcola la media dei risultati ottenuti. Infine, mostra come questa media cambia al crescere del numero di lanci del dado in un grafico. Questo ci aiuta a capire meglio come si comportano i numeri magici quando li tiriamo molte volte, e come si avvicinano a un certo valore quando il numero di lanci diventa molto grande. In altre parole, ci aiuta a capire meglio le regole speciali dei numeri magici α-stabili!
'''
import numpy as np
import matplotlib.pyplot as plt

# Funzione per generare numeri da una distribuzione α-stabile
def alpha_stable(alpha, beta, gamma, delta, size):
    # Generazione dei numeri casuali dalla distribuzione α-stabile
    uniform_sample = np.random.uniform(-np.pi/2, np.pi/2, size)
    cauchy_sample = np.tan(uniform_sample)
    if alpha != 1:
        standard_sample = ((1 + beta**2 * (np.abs(cauchy_sample))**(alpha))**(1/alpha)) * np.sign(cauchy_sample)
        return gamma * standard_sample + delta
    else:
        standard_sample = -2/np.pi * (beta * cauchy_sample * np.log(np.abs(cauchy_sample)))
        return gamma * standard_sample + delta

# Parametri della distribuzione α-stabile
alpha = 1.1
beta = 0
gamma = 1
delta = 0

# Numero di volte che lanciamo il dado, cresce esponenzialmente con n
ns = np.arange(1, 8)
num_trials = 10 ** ns

# Simulazione dei lanci del dado e calcolo della media
mean_values = []
for n in num_trials:
    # Generazione di n numeri casuali dalla distribuzione α-stabile
    samples = alpha_stable(alpha, beta, gamma, delta, n)
    # Calcolo della media dei numeri generati
    mean_values.append(np.mean(samples))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(num_trials, mean_values, marker='o')
plt.xscale('log')
plt.xlabel('Numero di lanci del dado (n)')
plt.ylabel('Media dei risultati')
plt.title('Convergenza della media dei risultati del dado α-stabile')
plt.grid(True)
plt.show()

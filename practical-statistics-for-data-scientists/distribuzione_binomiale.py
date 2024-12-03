'''
Immagina di lanciare una moneta 
10 volte e contare quante volte 
esce testa. Ogni volta che esce testa, 
diciamo che è un successo. 
La distribuzione binomiale 
ci aiuta a capire quante volte 
ci aspettiamo che esca testa 
in questi 10 lanci. 
È come fare una previsione basata 
su quanti lanci ci aspettiamo 
di vincere a un gioco.
'''
import scipy.stats as stats

# Calcolare la probabilità di ottenere esattamente 2 successi in 5 tentativi
p_esatto = stats.binom.pmf(2, n=5, p=0.1)
print("Probabilità di 2 successi in 5 tentativi:", p_esatto)

# Calcolare la probabilità di ottenere 2 o meno successi in 5 tentativi
p_meno_di_2 = stats.binom.cdf(2, n=5, p=0.1)
print("Probabilità di 2 o meno successi in 5 tentativi:", p_meno_di_2)

'''
calcolare la probabilità che vengano 
chiamati esattamente 2 tecnici 
su un totale di 4 tecnici disponibili, 
dobbiamo considerare il numero totale 
di modi in cui possiamo selezionare 
2 tecnici su 4. 
Questo può essere calcolato utilizzando 
il coefficiente binomiale.

Il coefficiente binomiale "n choose k" (indicato come nCk o C(n,k)) rappresenta il numero di modi in cui possiamo selezionare k elementi da un insieme di n elementi senza tener conto dell'ordine.
In questo caso, vogliamo selezionare 2 tecnici su 4, quindi il coefficiente binomiale corrispondente è:

C(4, 2) = 4! / (2! * (4 - 2)!) = 6

Quindi ci sono 6 modi diversi in cui possono essere chiamati esattamente 2 tecnici.

Poiché ci sono 4 tecnici in totale, la probabilità che vengano chiamati esattamente 2 tecnici è data dal rapporto tra il numero di modi in cui possono essere chiamati 2 tecnici (6) e il numero totale di possibili combinazioni di chiamate (che è anche 6 nel nostro caso, poiché ci sono 6 modi in cui possono essere chiamati 4 tecnici):
Probabilità = 6 / 6 = 1

Quindi la probabilità che vengano chiamati esattamente 2 tecnici è 1, che corrisponde al 100%.
'''
import math

def calcola_probabilita(num_tecnici, num_chiamati, num_selezionati):
    coefficiente_binomiale = math.comb(num_chiamati, num_selezionati)
    totale_combinazioni = math.comb(num_tecnici, num_chiamati)
    probabilita = coefficiente_binomiale / totale_combinazioni
    return probabilita
  
num_tecnici = 4
num_chiamati = 2
num_selezionati = 2

probabilita = calcola_probabilita(num_tecnici, num_chiamati, num_selezionati)
print(f"La probabilità di chiamare esattamente 2 tecnici su un totale di 4 è: {probabilita}")

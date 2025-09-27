'''
calcolare il numero minimo di persone necessarie affinché sia almeno il 50% la probabilità che qualcuno sia nato il 29 febbraio, possiamo utilizzare l'approccio del complemento. Calcoleremo il numero minimo di persone necessarie affinché la probabilità che nessuno sia nato il 29 febbraio sia inferiore al 50%, quindi useremo il complemento di questa probabilità.
'''

def calcola_probabilita(n):
    probabilita = 1.0
    giorni_natali = 365
  
   for i in range(n):
        probabilita *= (giorni_natali - i) / giorni_natali

    probabilita_complemento = 1 - probabilita
    return probabilita_complemento

probabilita_obiettivo = 0.5
num_persone = 0

while True:
    num_persone += 1
    probabilita = calcola_probabilita(num_persone)
    if probabilita >= probabilita_obiettivo:
        break
print(f"Numero minimo di persone necessarie: {num_persone}")

#(Numero minimo di persone necessarie: 23)

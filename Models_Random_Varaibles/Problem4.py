'''
calcolare il numero minimo di persone necessarie affinché sia almeno il 50% la probabilità che qualcuno sia nato il 29 febbraio, possiamo utilizzare l'approccio del complemento. Calcoleremo il numero minimo di persone necessarie affinché la probabilità che nessuno sia nato il 29 febbraio sia inferiore al 50%, quindi useremo il complemento di questa probabilità.
'''


def calcola_probabilita(n):
    probabilita = 1.0
    giorni_natali = 365
  

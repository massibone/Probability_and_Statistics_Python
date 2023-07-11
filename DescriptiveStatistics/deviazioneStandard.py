'''
un programma python che calcola la radice quadrata della varianza detta deviazione standard del numero di incidenti aerei in tutto il mondo dal 1985 al 1993 per i voli commerciali
anno            1985 1986 1987 1988 1989 1990 1991 1992 1993
incidenti         22      22     26     28     27     25       30      29     24
'''

import math

incidenti = [22, 22, 26, 28, 27, 25, 30, 29, 24]

def calcola_deviazione_standard(lista_dati):
    # Calcola la media dei dati
    media = sum(lista_dati) / len(lista_dati)

    # Calcola la somma dei quadrati delle differenze dalla media
    somma_quadrati = sum((x - media) ** 2 for x in lista_dati)

    # Calcola la varianza
    varianza = somma_quadrati / len(lista_dati)

    # Calcola la deviazione standard (radice quadrata della varianza)
    deviazione_standard = math.sqrt(varianza)

    return deviazione_standard

deviazione = calcola_deviazione_standard(incidenti)
print("La deviazione standard del numero di incidenti aerei dal 1985 al 1993 è:", deviazione)

'''
La deviazione standard del numero di incidenti aerei dal 1985 al 1993 è: 2.516611478423583

'''

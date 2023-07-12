'''
calcola quanti diversi gruppi di tre lettere si possono formare usando cinque lettere A;B;C;D;E
'''
import itertools

def calcola_num_gruppi():
    lettere = ['A', 'B', 'C', 'D', 'E']
    num_gruppi = 0

    # Calcolo dei gruppi di tre lettere
    for gruppo in itertools.combinations(lettere, 3):
        num_gruppi += 1
        print(''.join(gruppo))

    # Stampa del numero totale di gruppi
    print("Numero totale di gruppi: ", num_gruppi)

# Esecuzione del programma
calcola_num_gruppi()
'''
ABC
ABD
ABE
ACD
ACE
ADE
BCD
BCE
BDE
CDE
Numero totale di gruppi:  10
'''

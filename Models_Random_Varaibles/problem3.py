'''
calcola l'approssimazione della probabilità che la somma dei punteggi di 10 dadi non truccati sia compresa tra 30 e 40.
'''
import random

def roll_dice():
    return random.randint(1, 6)

def simulate_dice_rolls(num_rolls):
    sum_of_scores = 0
    for _ in range(num_rolls):
        sum_of_scores += roll_dice()
    return sum_of_scores

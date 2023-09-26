'''
calcola l'approssimazione della probabilità che la somma dei punteggi ottenuti dal lancio 
di 10 dadi non superi 400, 
e determina in maniera approssimativa la probabilità che siano necessari più di 140 lanci.
'''
import random

def roll_dice():
    return random.randint(1, 6)

def simulate_dice_rolls(num_rolls):
    sum_of_scores = 0
    for _ in range(num_rolls):
        sum_of_scores += roll_dice()
    return sum_of_scores

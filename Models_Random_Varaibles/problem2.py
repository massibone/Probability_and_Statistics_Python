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
def calculate_probability(num_simulations, target_sum):
    count_successful = 0
    num_rolls = 0
    while count_successful < num_simulations:
        num_rolls += 1
        sum_of_scores = simulate_dice_rolls(10)
        if sum_of_scores <= target_sum:
            count_successful += 1
    probability = count_successful / num_simulations
    return probability

num_simulations = 1000  # Numero di simulazioni da eseguire
target_sum = 400  # Soglia della somma dei punteggi

probability = calculate_probability(num_simulations, target_sum)
print(f"Probabilità approssimata: {probability}")
'''
il punteggio massimo ottenibile con 10 dadi è 60 (se tutti i dadi mostrano 6). Pertanto, la probabilità che siano necessari più di 140 lanci sarà 0.
'''

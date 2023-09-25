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
def calculate_probability(num_simulations):
    count_successful = 0
    for _ in range(num_simulations):
        sum_of_scores = simulate_dice_rolls(10)
        if 30 <= sum_of_scores <= 40:
            count_successful += 1
    probability = count_successful / num_simulations
    return probability
    
num_simulations = 100000  # Numero di simulazioni da eseguire

probability = calculate_probability(num_simulations)
print(f"Probabilità approssimata: {probability}")

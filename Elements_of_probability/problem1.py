'''
si estraggono a caso due palline da un'urna che ne contiene 6 bianche e 5 nere.Qual'è la probabilità che le due estratte siano una bianca e una nera? e la probabilità che siano tutte e due bianche?
'''
import random

def calculate_probabilities():
    urn = ['white'] * 6 + ['black'] * 5  # Creating the urn with the balls

    # Drawing two balls randomly
    draw = random.sample(urn, 2)

    # Calculating the probabilities
    white_black = draw.count('white') == 1 and draw.count('black') == 1
    both_white = draw.count('white') == 2

    # Printing the results
    print("Probability of drawing one white ball and one black ball:", white_black)
    print("Probability of drawing two white balls:", both_white)

# Running the program
calculate_probabilities()

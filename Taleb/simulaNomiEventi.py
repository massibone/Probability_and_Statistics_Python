'''
simula l'assegnazione casuale di nomi agli eventi storici partendo da una lista di nomi di conflitti 
'''
import random

# Definizione di una funzione per simulare l'assegnazione di nomi agli eventi
def simulate_event_names(conflict_names, num_simulations):
    event_assignments = []
    for _ in range(num_simulations):
        # Simula l'assegnazione casuale di nomi agli eventi
        event_names = random.choices(conflict_names, k=len(conflict_names))
        event_assignments.append(event_names)
    
    return event_assignments

# Dati di esempio: nomi di conflitti o eventi storici
conflict_names = [
    "Mongolian Invasions",
    "Franco-Prussian War",
    "WWII",
    "First Jewish War",
    "American Civil War",
    "Napoleonic Wars",
    "Vietnam War"
]

num_simulations = 10  # Numero di simulazioni da eseguire

# Esegui la simulazione di assegnazione casuale di nomi agli eventi
event_assignments = simulate_event_names(conflict_names, num_simulations)

# Stampare i risultati delle simulazioni
print("Simulazioni di assegnazione di nomi agli eventi:")
for i, event_names in enumerate(event_assignments):
    print(f"Simulazione {i+1}: {event_names}")

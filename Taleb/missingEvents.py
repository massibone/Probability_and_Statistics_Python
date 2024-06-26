'''
simula l'effetto di rimuovere una proporzione specifica di eventi da un campione di eventi storici. 
La simulazione calcola quanti eventi vengono rimossi, quanti ne rimangono e la proporzione degli eventi rimossi rispetto al totale degli eventi.
'''

import random

# Dati di esempio: numero totale di eventi e proporzione da rimuovere
total_events = 1000
proportion_to_remove = 0.3  # Rimuovi il 30% degli eventi
# Funzione per simulare l'effetto di rimuovere una proporzione di eventi
def simulate_missing_events(total_events, proportion_to_remove, num_simulations):
    results = []
    
   for _ in range(num_simulations):
        # Genera un campione di eventi
        all_events = list(range(1, total_events + 1))
        
        # Determina quanti eventi rimuovere
        num_to_remove = int(total_events * proportion_to_remove)
       
  # Rimuove in modo casuale una proporzione di eventi
        removed_events = random.sample(all_events, num_to_remove)
        
        # Calcola quanti eventi rimangono
        remaining_events = [event for event in all_events if event not in removed_events]
        
        # Calcola la proporzione di eventi rimossi
        proportion_removed = num_to_remove / total_events
 # Memorizza i risultati della simulazione
        results.append((num_to_remove, len(remaining_events), proportion_removed))
    
    return results

# Numero di simulazioni da eseguire
num_simulations = 10

# Esegui la simulazione di rimozione casuale di eventi
simulation_results = simulate_missing_events(total_events, proportion_to_remove, num_simulations)

# Stampare i risultati delle simulazioni
print("Simulazioni di rimozione casuale di eventi:")
for i, result in enumerate(simulation_results):
    num_removed, num_remaining, proportion_removed = result
    print(f"Simulazione {i+1}: Eventi rimossi = {num_removed}, Eventi rimanenti = {num_remaining}, Proporzione rimossa = {proportion_removed:.2f}")

total_time = 30  # Durata totale dell'intervallo
waiting_time = 10  # Tempo di attesa desiderato

# Calcolo della probabilità
probability_a = (total_time - waiting_time) / total_time

print("La probabilità di dover aspettare più di 10 minuti è:", probability_a)

remaining_time = 15  # Durata dell'intervallo rimanente

# Calcolo della probabilità
probability_b = remaining_time / total_time


print("La probabilità di dover aspettare almeno 10 minuti dato che l'autobus non è arrivato alle 10:15 è:", probability_b)

'''
ho simulato una lista di quantità di caramelle rare e ho calcolato una stima del totale del mucchio basata su queste quantità simulate.
'''
import random

# Generazione casuale di una lista di quantità di caramelle (simula dati di caramelle rare)
quantita_caramelle_rare = [random.randint(1, 100) for _ in range(50)]

# Calcolo della stima del totale delle caramelle nel mucchio
stima_totale_caramelle = sum(quantita_caramelle_rare) * 20  # Assumiamo una distribuzione uniforme per le stime

# Stampare la stima del totale delle caramelle
print("Stima totale delle caramelle nel mucchio:", stima_totale_caramelle)

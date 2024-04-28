'''
simula l'effetto di rimuovere una proporzione specifica di eventi da un campione di eventi storici. La simulazione calcola quanti eventi vengono rimossi, quanti ne rimangono e la proporzione degli eventi rimossi rispetto al totale degli eventi.
'''

import random

# Dati di esempio: numero totale di eventi e proporzione da rimuovere
total_events = 1000
proportion_to_remove = 0.3  # Rimuovi il 30% degli eventi

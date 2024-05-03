'''
Immagina di avere un grosso barattolo pieno di molte piccole pietre di diversi colori. Ogni pietra rappresenta un numero casuale diverso. Se prendi un mucchio di queste pietre e sommi insieme i loro numeri, otterrai un numero che potrebbe sembrare simile a una forma speciale chiamata distribuzione normale o "a campana".

Ora, immagina di voler fare qualcosa di diverso. Invece di avere solo pietre con numeri precisi, aggiungiamo un po' di confusione o incertezza. Potremmo prendere una manciata di queste pietre e dare loro numeri che possono cambiare leggermente o essere meno precisi. Questo rende la distribuzione meno regolare e può far sì che i numeri risultanti siano più variabili o "grassi" nei bordi.

Quindi, quello che stiamo facendo è aggiungere sempre più livelli di incertezza. Non ci fermiamo a una sola volta, ma continuiamo ad aggiungere incertezza su incertezza. È come mettere dentro una scatola una scatola più piccola, e poi una ancora più piccola, e così via.

Questo modo di aggiungere incertezza può aiutarci a capire meglio come certe cose si comportano quando diventano più complesse, senza dover usare solo i numeri. È come una sorta di gioco di costruzione concettuale, dove possiamo esplorare idee strane e complesse.
'''

import numpy as np

def add_uncertainty(x, levels):
    """
    Aggiunge livelli di incertezza in modo ricorsivo a un valore x.
    
    Parameters:
        x (float): Valore iniziale su cui aggiungere incertezza.
        levels (int): Numero di livelli di incertezza da aggiungere.
    
    Returns:
        float: Valore di x con incertezza aggiunta.
    """
    if levels <= 0:
        return x

    # Genera un nuovo valore casuale intorno a x
    uncertainty = np.random.normal(loc=0, scale=1)  # incertezza casuale con distribuzione normale
    x_with_uncertainty = x + uncertainty
    
    # Chiamata ricorsiva per aggiungere ulteriori livelli di incertezza
    return add_uncertainty(x_with_uncertainty, levels - 1)

# Esempio di utilizzo
initial_value = 10.0
num_levels = 3

final_value = add_uncertainty(initial_value, num_levels)
print(f"Valore iniziale: {initial_value}")
print(f"Valore finale con incertezza: {final_value}")

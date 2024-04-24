import random

# Funzione per calcolare il numero approssimato di capelli rossi con incertezza
def calcola_capelli_rossi():
    # Numero totale di bambole nella scatola
    numero_totale_bambole = 100
    
    # Percentuale approssimativa di bambole con capelli rossi (tra 40% e 60%)
    percentuale_capelli_rossi = random.uniform(0.4, 0.6)
    
    # Variabilità nella percentuale di bambole con capelli rossi (tra 5% e 10%)
    variabilita_percentuale = random.uniform(0.05, 0.1)
    
    # Calcolo approssimativo del numero di bambole con capelli rossi
    bambole_con_capelli_rossi = numero_totale_bambole * percentuale_capelli_rossi
    
    # Applicazione della variabilità nella percentuale di bambole con capelli rossi
    bambole_con_capelli_rossi_con_variabilita = random.uniform(1 - variabilita_percentuale, 1 + variabilita_percentuale) * bambole_con_capelli_rossi
    
    # Arrotondiamo il risultato
    bambole_con_capelli_rossi_con_variabilita = round(bambole_con_capelli_rossi_con_variabilita)
    
    return bambole_con_capelli_rossi_con_variabilita

# Esempio di utilizzo della funzione
capelli_rossi = calcola_capelli_rossi()
print(f"Numero approssimato di bambole con capelli rossi nella scatola: {capelli_rossi}")

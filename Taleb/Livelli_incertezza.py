
'''
Immagina di avere un vaso con caramelle rosse e blu, e vuoi sapere quante sono rosse. Ma non sei sicuro della precisione del tuo conteggio. Quindi, anziché dire esattamente quante caramelle rosse ci sono, diciamo che potrebbe esserci un po' di incertezza nel conteggio. Inoltre, non sei sicuro di quanto sei sicuro nel tuo conteggio impreciso!
'''
import random

# Funzione per calcolare il numero approssimato di caramelle rosse con incertezza
def calcola_caramelle_rosse():
    # Numero totale di caramelle nel vaso
    numero_totale_caramelle = 100
    
   # Percentuale approssimativa di caramelle rosse (tra 40% e 60%)
    percentuale_caramelle_rosse = random.uniform(0.4, 0.6)

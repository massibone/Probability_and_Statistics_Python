'''
Un intervallo di confidenza bilaterale rappresenta un intervallo all'interno del quale si presume che cada un parametro di interesse, come ad esempio una media o una proporzione, con un certo livello di confidenza. In un intervallo di confidenza bilaterale, stiamo cercando di coprire sia la parte inferiore che quella superiore della distribuzione.

Ecco un esempio di calcolo di un intervallo di confidenza bilaterale per la media di un campione:

Supponiamo di avere un campione di 50 misurazioni di altezza umana e vogliamo calcolare un intervallo di confidenza al 95% per la media delle altezze della popolazione da cui è stato estratto il campione.
'''

import numpy as np
import scipy.stats as st

# Campione di altezze (in centimetri)
altezze = [170, 165, 175, 180, 160, 175, 172, 168, 180, 185,
           168, 172, 178, 163, 169, 172, 175, 180, 174, 168,
           169, 182, 176, 171, 168, 173, 172, 177, 169, 173,
           172, 174, 179, 167, 181, 172, 170, 173, 176, 171,
           178, 176, 172, 168, 169, 180, 168, 167, 175, 173]

# Calcoliamo la media del campione
media_campione = np.mean(altezze)

# Dimensione del campione
n = len(altezze)

# Livello di confidenza desiderato (95%)
confidence_level = 0.95

# Calcoliamo l'intervallo di confidenza bilaterale per la media utilizzando la distribuzione t di Student
intervallo_confidenza = st.t.interval(confidence_level, df=n-1, loc=media_campione, scale=st.sem(altezze))

print("Media campione:", media_campione)
print(f"Intervallo di confidenza al {confidence_level*100:.1f}%: ({intervallo_confidenza[0]:.2f}, {intervallo_confidenza[1]:.2f})")

# Media campione: 172.8
# Intervallo di confidenza al 95.0%: (171.35, 174.25)
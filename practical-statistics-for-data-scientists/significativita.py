'''
La significatività statistica misura se un risultato di un esperimento è più estremo di quanto la casualità potrebbe produrre. 
In un esempio di test sul web, due prezzi mostrano tassi di conversione diversi. Anche con oltre 45.000 dati, 
è importante testare la significatività statistica a causa dei bassi tassi di conversione (meno dell'1%). 
Usando una procedura di permutazione, possiamo determinare se la differenza osservata è dovuta al caso o è significativa.
'''
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

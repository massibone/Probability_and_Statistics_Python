'''
Le distribuzioni con code lunghe (long-tailed distributions) sono distribuzioni in cui esistono valori estremi 
(molto grandi o molto piccoli) che si verificano con bassa frequenza. Anche se la distribuzione normale è storicamente importante nelle statistiche, 
molte volte i dati reali non seguono una distribuzione normale. La distribuzione può essere altamente asimmetrica (skewed) o discreta. 
Le code lunghe sono comuni nei dati pratici, come i ritorni azionari, dove eventi estremi accadono più frequentemente di quanto predetto dalla distribuzione normale.
'''

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

# Dati simulati: i ritorni giornalieri di Netflix (NFLX)
# Supponiamo di avere una serie temporale di prezzi di chiusura
# In un caso reale, caricheresti questi dati da un file o un database

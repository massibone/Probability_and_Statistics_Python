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

# Simuliamo dei prezzi di chiusura per esempio
np.random.seed(0)
price = np.exp(np.cumsum(np.random.normal(0, 1, 500)))  # Simulazione di prezzi
sp500_px = pd.DataFrame({'NFLX': price})

# Calcolo dei ritorni giornalieri logaritmici
nflx = sp500_px['NFLX']
nflx_returns = np.diff(np.log(nflx[nflx > 0]))

# Creazione del QQ-Plot
fig, ax = plt.subplots(figsize=(6, 6))
stats.probplot(nflx_returns, dist="norm", plot=ax)
ax.get_lines()[1].set_color('grey')  # Cambia il colore della linea di riferimento
plt.title("QQ-Plot dei ritorni di Netflix (NFLX)")
plt.show()

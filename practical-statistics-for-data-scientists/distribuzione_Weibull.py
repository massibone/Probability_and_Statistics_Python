'''
La distribuzione di Weibull 
è usata per modellare eventi il cui tasso cambia nel tempo, come il fallimento meccanico, dove il rischio di fallimento aumenta con il passare del tempo. Ha due parametri: β (shape) e η (scale). Se β > 1, la probabilità di un evento aumenta nel tempo; se β < 1, la probabilità diminuisce. La caratteristica vita (η) rappresenta il tempo caratteristico al posto del tasso degli eventi. La distribuzione di Weibull è quindi utile per l'analisi del tempo di fallimento. In Python, si possono generare numeri casuali da una distribuzione di Weibull usando stats.weibull_min.rvs.
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# Parametri della distribuzione di Weibull
shape = 1.5  # Parametro β
scale = 5000  # Parametro η

# Generazione di 100 numeri casuali (tempi di vita) dalla distribuzione di Weibull
lifetimes = weibull_min.rvs(shape, scale=scale, size=100)

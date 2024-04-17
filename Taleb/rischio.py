import matplotlib.pyplot as plt
import numpy as np

# Generiamo dei dati casuali per rappresentare il concetto
rischio_basso = np.random.normal(loc=0.5, scale=0.1, size=1000)
rischio_alto = np.random.normal(loc=0.8, scale=0.2, size=1000)

# Creiamo un istogramma per visualizzare la distribuzione dei rischi
plt.figure(figsize=(8, 6))
plt.hist(rischio_basso, bins=30, alpha=0.5, color='blue', label='Rischio Basso')
plt.hist(rischio_alto, bins=30, alpha=0.5, color='red', label='Rischio Alto')
plt.axvline(np.mean(rischio_basso), color='blue', linestyle='dashed', linewidth=2, label='Media Rischio Basso')
plt.axvline(np.mean(rischio_alto), color='red', linestyle='dashed', linewidth=2, label='Media Rischio Alto')
plt.xlabel('Livello di Rischio')
plt.ylabel('Frequenza')
plt.title('Confronto tra Rischio Basso e Rischio Alto')
plt.legend()
plt.show()

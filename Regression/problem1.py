'''
I dati seguenti mettono in relazione la percentuale di acqua x contenuta in un certo materiale in una delle fasi di lavorazione,con la densità Y del prodotto finito.
x 5 6 7 10 12 15 18 29
Y 7.4 9.3 10.6 15.4 18.1 22.2 24.1 24.8
a) traccia il diagramma di dispersione
b) trova la retta di regressione che interpola questi dati
'''
import numpy as np
import matplotlib.pyplot as plt
# Dati di input
x = np.array([5, 6, 7, 10, 12, 15, 18, 29])
Y = np.array([7.4, 9.3, 10.6, 15.4, 18.1, 22.2, 24.1, 24.8])

# Tracciamento del diagramma di dispersione
plt.scatter(x, Y, color='blue', label='Data')
plt.xlabel('Percentuale di acqua')
plt.ylabel('Densità')
plt.title('Diagramma di dispersione')
plt.legend()
plt.grid(True)
plt.show()

# Trovare la retta di regressione (linear regression)
coefficients = np.polyfit(x, Y, 1)
m = coefficients[0]  # Coefficiente angolare
b = coefficients[1]  # Coefficiente di intercetta

# Stampa la retta di regressione
print(f"Equazione della retta di regressione: Y = {m:.4f}x + {b:.4f}")

#Equazione della retta di regressione: Y = 0.7722x + 6.6418
in windows diagramma_dispersione.png

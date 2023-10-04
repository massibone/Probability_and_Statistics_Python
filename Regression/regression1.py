'''
 dati seguenti x percentuale di acqua contenuta e Y densità del prodotto
x 5 6 7 10 12 15 18 29
Y 7.4 9.3 10.6 15.4 18.1 22.2 24.1 24.8
a)traccia il diagramma di dispersione
b)trova la retta di regressione
'''



import numpy as np
import matplotlib.pyplot as plt

# Dati forniti
x_data = np.array([5, 6, 7, 10, 12, 15, 18, 29])
y_data = np.array([7.4, 9.3, 10.6, 15.4, 18.1, 22.2, 24.1, 24.8])

# Tracciamento del diagramma di dispersione
plt.scatter(x_data, y_data, color='b', label='Dati')
plt.xlabel('Percentuale di acqua contenuta (%)')
plt.ylabel('Densità del prodotto')
plt.title('Diagramma di dispersione')
plt.legend()
plt.grid(True)
plt.show()

# Trovare la retta di regressione (y = mx + b)
m, b = np.polyfit(x_data, y_data, 1)

# Tracciamento della retta di regressione
plt.scatter(x_data, y_data, color='b', label='Dati')
plt.plot(x_data, m * x_data + b, color='r', label='Retta di regressione')
plt.xlabel('Percentuale di acqua contenuta (%)')
plt.ylabel('Densità del prodotto')
plt.title('Diagramma di dispersione con retta di regressione')
plt.legend()
plt.grid(True)
plt.show()

print(f"La retta di regressione è: y = {m:.2f}x + {b:.2f}")

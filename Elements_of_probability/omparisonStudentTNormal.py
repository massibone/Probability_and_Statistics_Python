import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, norm

# Definiamo i gradi di libertà
degrees_of_freedom = 3

# Generiamo i dati per la distribuzione di Student T e la distribuzione normale
x = np.linspace(-5, 5, 1000)
student_t_pdf = t.pdf(x, df=degrees_of_freedom)
normal_pdf = norm.pdf(x)

# Creiamo il grafico
plt.figure(figsize=(10, 6))

# Plotting delle distribuzioni
plt.plot(x, student_t_pdf, label=f"Student T (df={degrees_of_freedom})")
plt.plot(x, normal_pdf, label="Normal")

# Aggiungiamo annotazioni per i punti chiave
plt.annotate("1. Prevalenza nella finanza", xy=(1, 0.25), xytext=(2, 0.3),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate("2. Approssimazione alla Gaussiana", xy=(-2, 0.25), xytext=(-4, 0.3),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate("4. Comportamento della coda", xy=(-3, 0.05), xytext=(-4, 0.15),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate("3. Convergenza asintotica", xy=(-1, 0.15), xytext=(0, 0.25),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Etichette e titoli
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Comparison of Student T and Normal Distribution')
plt.legend()

# Mostra il grafico
plt.grid(True)
plt.show()

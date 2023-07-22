import tkinter as tk
from scipy.stats import binom

def calculate_binomial_distribution():
    n = int(n_entry.get())
    p = float(p_entry.get())
    x = int(x_entry.get())

    # Calcolo della probabilità
    probability = binom.pmf(x, n, p)
  # Mostra il risultato nella schermata
    result_label.config(text=f"Probabilità: {probability:.4f}")

# Creazione della schermata
window = tk.Tk()
window.title("Calcolatore Distribuzione Binomiale")

# Etichetta e campo di input per n
n_label = tk.Label(window, text="n:")
n_label.pack()
n_entry = tk.Entry(window)
n_entry.pack()
# Etichetta e campo di input per p
p_label = tk.Label(window, text="p:")
p_label.pack()
p_entry = tk.Entry(window)
p_entry.pack()

# Etichetta e campo di input per x
x_label = tk.Label(window, text="x:")
x_label.pack()
x_entry = tk.Entry(window)
x_entry.pack()

# Pulsante per calcolare la distribuzione binomiale
calculate_button = tk.Button(window, text="Calcola", command=calculate_binomial_distribution)
calculate_button.pack()

# Etichetta per il risultato
result_label = tk.Label(window, text="Probabilità:")
result_label.pack()
# Avvio della schermata
window.mainloop()

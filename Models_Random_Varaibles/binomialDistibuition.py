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

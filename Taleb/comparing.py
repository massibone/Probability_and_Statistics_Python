import matplotlib.pyplot as plt

# Dati della tabella
alpha_values = [1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4]
pareto_k1_values = [0.829, 0.724, 0.65, 0.594, 0.551, 0.517, 0.488, 0.465, 0.445, 0.428, 0.413, 0.4]
pareto_k130_values = [0.787, 0.65, 0.556, 0.484, 0.431, 0.386, 0.356, 0.3246, 0.305, 0.284, 0.263, 0.2532]
pareto_k1100_values = [0.771, 0.631, 0.53, 0.449, 0.388, 0.341, 0.307, 0.281, 0.258, 0.235, 0.222, 0.211]
student_k1_values = [0.792, 0.647, 0.543, 0.465, 0.406, 0.359, 0.321, 0.29, 0.265, 0.243, 0.225, 0.209]
student_k130_values = [0.765, 0.609, 0.483, 0.387, 0.316, 0.256, 0.224, 0.191, 0.167, 0.149, 0.13, 0.126]
student_k1100_values = [0.756, 0.587, 0.451, 0.352, 0.282, 0.227, 0.189, 0.159, 0.138, 0.121, 0.10, 0.093]

# Creazione del grafico
plt.figure(figsize=(10, 6))

# Plotting dei dati
plt.plot(alpha_values, pareto_k1_values, marker='o', label='Pareto κ1')
plt.plot(alpha_values, pareto_k130_values, marker='o', label='Pareto κ1,30')
plt.plot(alpha_values, pareto_k1100_values, marker='o', label='Pareto κ1,100')
plt.plot(alpha_values, student_k1_values, marker='o', label='Student κ1')
plt.plot(alpha_values, student_k130_values, marker='o', label='Student κ1,30')
plt.plot(alpha_values, student_k1100_values, marker='o', label='Student κ1,100')

# Aggiunta di etichette e titoli
plt.xlabel('Alpha')
plt.ylabel('Values')
plt.title('Comparing Pareto to Student T (Same tail exponent α)')
plt.legend()

# Mostrare il grafico
plt.grid(True)
plt.show()

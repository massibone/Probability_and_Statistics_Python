import numpy as np
import matplotlib.pyplot as plt


def plot_bar(labels, values, title, xlabel, ylabel):
    """
    Generates a bar chart with given labels, values, title, and axis labels.

    Args:
        labels (list): List of labels for each bar.
        values (list): List of values for each bar.
        title (str): Title for the chart.
        xlabel (str): Label for the X-axis.
        ylabel (str): Label for the Y-axis.
    """
    plt.bar(labels, values)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


def plot_distribution(x, y, title, xlabel, ylabel):
    """
    Generates a line plot for a distribution with given data and labels.

    Args:
        x (array): Array of values for the X-axis.
        y (array): Array of values for the Y-axis.
        title (str): Title for the chart.
        xlabel (str): Label for the X-axis.
        ylabel (str): Label for the Y-axis.
    """
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


# Common parameters
PAYOFF_A = 10  # Payoff per l'opzione A
PAYOFF_B = 20  # Payoff per l'opzione B
PROB_A = 0.7  # Probabilità dell'opzione A
PROB_B = 0.3  # Probabilità dell'opzione B
STRIKE = 50  # Prezzo di strike per l'opzione call
PROB_RARE = 0.001  # Probabilità di un evento raro
IMPACT_RARE = 100000  # Impatto di un evento raro

# Distribuzioni
X_NORM = np.linspace(-3, 3, 100)  # Intervallo per la distribuzione normale
Y_NORM = np.random.normal(0, 1, 100)  # Distribuzione normale
Y_PARETO = 1 / (X_NORM + 1)**2  # Distribuzione di Pareto

# Set figure size (optional)
plt.figure(figsize=(10, 6))  # Modifica larghezza e altezza se necessario

# 1. Confusione tra probabilità e payoff
expected_a = PROB_A * PAYOFF_A  # Valore atteso dell'opzione A
expected_b = PROB_B * PAYOFF_B  # Valore atteso dell'opzione B
plot_bar(["A", "B"], [expected_a, expected_b], "Valore atteso", "Opzione", "Valore atteso")

# 2. Payoff binari vs. continui
payoffs_binary = np.array([0, 1])  # Payoff binari (es: testa o croce)
payoffs_continuous = np.random.normal(0, 1, 1000)  # Payoff continui (es: ampiezza terremoto)

plt.subplot(121)
plt.bar(payoffs_binary, np.ones(2))
plt.xlabel("Payoff (binario)")

plt.subplot(122)
plt.hist(payoffs_continuous)
plt.xlabel("Payoff (continuo)")
plt.show()

# 3. Limitazioni delle previsioni binarie
prices = np.linspace(40, 60, 100)  # Gamma di prezzi sottostanti
payoffs_option = np.maximum(prices - STRIKE, 0)  # Payoff opzione call

plot_distribution(prices, payoffs_option, "Payoff opzione call", "Prezzo sottostante", "Payoff opzione")

# 4. Sovraestimazione di probabilità di coda
plot_bar(["Probabilità", "Impatto"], [PROB_RARE, IMPACT_RARE], "Confronto evento raro", "Evento", "Valore")

# 5. Mercati di previsione binari vs. continui
payoffs_prediction = np.array([0, 1])  # Payoff binari (es: esito elezione)
payoffs_financial = np.random.normal(0)

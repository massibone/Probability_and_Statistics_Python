import numpy as np

# Funzione per calcolare l'estimatore non parametrico
def nonparametric_estimator(data):
    # Qui simuliamo l'estimatore non parametrico che conta i mattoncini rossi
    # data è una lista dei mattoncini che osserviamo, dove i mattoncini rossi sono rappresentati da 1 e gli altri da 0
    # L'estimatore non parametrico somma tutti i mattoncini e divide per il numero totale di mattoncini
    return np.mean(data)

# Funzione per correggere l'errore dell'estimatore non parametrico
def correct_nonparametric_estimator(data):
    # Calcoliamo l'estimatore non parametrico
    nonparametric_estimate = nonparametric_estimator(data)
    # Calcoliamo il numero totale di mattoncini osservati
    total_bricks = len(data)
    # Calcoliamo la modalità della distribuzione, che è il valore più comune
    mode = np.argmax(np.bincount(data))
    # Calcoliamo la distanza tra la moda e la stima non parametrica
    mode_mean_distance = abs(mode - nonparametric_estimate)
    # Correggiamo la stima non parametrica aggiungendo la distanza tra la moda e la stima
    corrected_estimate = nonparametric_estimate + mode_mean_distance
    return corrected_estimate

# Simulazione di campioni di mattoncini rossi
sample_sizes = [1000, 5000, 10000]
for sample_size in sample_sizes:
    # Generiamo un campione di mattoncini rossi e non rossi casuali
    bricks = np.random.choice([0, 1], size=sample_size)
    
    # Calcoliamo l'estimatore non parametrico
    nonparametric_result = nonparametric_estimator(bricks)
    
    # Correggiamo l'errore dell'estimatore non parametrico
    corrected_result = correct_nonparametric_estimator(bricks)
    
    # Stampiamo i risultati
    print(f"Dimensione campione: {sample_size}")
    print(f"Estimatore non parametrico: {nonparametric_result}")
    print(f"Estimatore non parametrico corretto: {corrected_result}")
    print()

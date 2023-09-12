import scipy.stats as stats

mean = 600
std_dev = 98.99

# Calcolo della probabilità utilizzando la distribuzione normale
probability = 1 - stats.norm.cdf(600, mean, std_dev)

print("La probabilità che le precipitazioni dei prossimi due anni superino complessivamente i 600 mm è:", probability)

mean_diff = 0
std_dev_diff = 98.99

# Calcolo della probabilità utilizzando la distribuzione normale
probability_diff = 1 - stats.norm.cdf(70, mean_diff, std_dev_diff)

print("La probabilità che le precipitazioni del prossimo anno superino quelle dell'anno successivo per più di 70 mm è:", probability_diff)

'''
i dati a disposizione di metereologi indicano che le precipitazioni a Firenze hanno distribuzione normale con media 300 mm e deviazione standard 70 m.Assumiamo anche che le precipitazioni di anni successivi siano indipendenti. a)Trova la probabilità che le precipitazioni dei prssimi due anni superino complessivamente i 600 mm b)Trova la probabilità che le precipitazioni del prossimo anno superino quelle dell'anno successivo per piu' di 70 mm 
Per risolvere questo problema, possiamo utilizzare le proprietà della distribuzione normale.

a) Per calcolare la probabilità che le precipitazioni dei prossimi due anni superino complessivamente i 600 mm, dobbiamo calcolare la probabilità che la somma delle precipitazioni di due anni sia maggiore di 600 mm.

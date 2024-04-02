'''Nella prima, hai un periodo di calma chiamato "Pace" con una media positiva e una volatilità molto bassa, e un periodo di turbolenza chiamato "Guerra" con una media negativa e una volatilità estremamente alta.
Nella seconda situazione, prendi un bond B che paga interessi r alla fine di un singolo periodo. Alla scadenza, c'è una grande probabilità di ottenere B(1 + r), e una piccola possibilità di default. È molto improbabile ottenere esattamente B.
Immagina che non ci siano passaggi intermedi tra Guerra e Pace: sono stati distinti e stati discreti. I bond non vanno in default solo "un po'". Nota che la probabilità che il risultato sia vicino alla media è quasi nulla. Tipicamente, la probabilità dell'aspettativa (E(x)) è più piccola rispetto alle diverse medie dei regimi, quindi P(x = E(x)) < P (x = m1) e < P (x = m2), ma nel caso estremo (bond), P(x = E(x)) diventa sempre più piccola. L'evento raro è il risultato vicino alla media.
Lo stesso concetto si applica alle valute fissate, poiché le svalutazioni non possono essere "lievi", con un tipo di volatilità tutto-o-niente e una bassa densità nella "valle" tra i due regimi distinti.
'''
# Variety 1: Guerra e Pace
capitale_iniziale_pace = 500
tasso_interesse_annuo_pace = 0.02
capitale_iniziale_guerra = 500
tasso_interesse_annuo_guerra = -0.03

importo_finale_pace = capitale_iniziale_pace * (1 + tasso_interesse_annuo_pace)
importo_finale_guerra = capitale_iniziale_guerra * (1 + tasso_interesse_annuo_guerra)

print(f"Variety 1 - Situazione di Pace: Importo finale dopo un anno sarà di {importo_finale_pace}€")
print(f"Variety 1 - Situazione di Guerra: Importo finale dopo un anno sarà di {importo_finale_guerra}€")

# Variety 2: Stato deterministico condizionale
capitale_iniziale_bond = 1000
tasso_interesse_bond = 0.04

importo_finale_bond = capitale_iniziale_bond * (1 + tasso_interesse_bond)

print(f"Variety 2 - Bond: Importo finale dopo un anno sarà di {importo_finale_bond}€")

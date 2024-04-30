'''
Immagina di avere una cassettina per mettere i tuoi risparmi, e ogni giorno aggiungi un po' di soldi. Ora, immagina di avere anche un'altra cassettina in cui metti i soldi per comprare giocattoli da un altro paese, e ogni giorno aggiungi un po' di soldi anche a questa cassettina.

La cassettina dei risparmi è come una strada lunga e liscia, dove i soldi crescono in modo regolare ogni giorno. Se tracciassi un grafico dell'ammontare dei soldi nella cassettina dei risparmi, vedresti una linea che cresce dolcemente nel tempo, senza salti o cali improvvisi.

Ma la cassettina per i giocattoli stranieri è un po' diversa. Ci sono giorni in cui i soldi crescono di più e altri giorni in cui crescono di meno, a seconda di quanto bene va il mercato finanziario di quel paese. Quindi, se tracciassi un grafico dell'ammontare dei soldi nella cassettina dei giocattoli stranieri, vedresti una linea che salta su e giù in modo irregolare nel tempo.

Ora, prendiamo in considerazione quanto dovresti pagare per acquistare una quantità fissa di giocattoli stranieri in futuro. Se vuoi pagare utilizzando i soldi della tua cassettina dei risparmi, devi considerare quanto quei soldi crescono nel tempo, tenendo conto degli interessi che vengono aggiunti ogni giorno. Questo è come calcolare il "prezzo futuro neutrale al rischio".

D'altra parte, se vuoi pagare utilizzando i soldi della tua cassettina dei giocattoli stranieri, devi considerare quanto crescono i soldi in quella cassettina, tenendo conto di quanto guadagno ti aspetti in futuro. Questo è come calcolare il "prezzo futuro richiesto".

Quindi, se tracciassi un grafico dei prezzi futuri neutri al rischio e dei prezzi futuri richiesti nel tempo, vedresti due linee diverse. La linea del prezzo futuro neutrale al rischio sarebbe simile a quella della cassettina dei risparmi, crescendo dolcemente nel tempo. Ma la linea del prezzo futuro richiesto sarebbe più irregolare, come quella della cassettina dei giocattoli stranieri.
'''
# Calcolo del prezzo futuro neutrale al rischio
S0 = 100  # Prezzo attuale del giocattolo straniero
r = 0.05  # Tasso di interesse senza rischio
t = 1     # Periodo di tempo in anni

FQ = S0 * (1 + r) ** t
print("Prezzo futuro neutrale al rischio:", FQ)

# Calcolo del prezzo futuro richiesto
m = 0.07  # Guadagno richiesto sul giocattolo straniero

FP = S0 * (1 + m) ** t
print("Prezzo futuro richiesto:", FP)

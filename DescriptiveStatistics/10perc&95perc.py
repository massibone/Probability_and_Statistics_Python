'''
il percentile è un concetto statistico che viene utilizzato per descrivere la posizione relativa di un valore all'interno di una distribuzione di dati. In sostanza, il decimo percentile rappresenta il valore al di sotto del quale si trova il 10% dei dati, mentre il 95-esimo percentile rappresenta il valore al di sotto del quale si trova il 95% dei dati.
Ad esempio, supponiamo di avere i seguenti dati relativi ai punteggi di un esame:
punteggi = [60, 65, 70, 75, 80, 85, 90, 95, 100]

Il decimo percentile rappresenterà il punteggio al di sotto del quale si trova il 10% dei dati. Nel nostro esempio, il 10% dei dati corrisponde a 0.1 * 9 = 0.9 (arrotondato a 1). Pertanto, il decimo percentile sarà il punteggio al di sotto del quale si trova il 10% dei dati, ovvero il punteggio corrispondente all'indice 1 cioe' 65
mentre il 95% dei dati corrisponde a 0.95 * 9 = 8.55 (arrotondato a 9). Pertanto, il 95-esimo percentile sarà il punteggio al di sotto del quale si trova il 95% dei dati, ovvero il punteggio corrispondente all'indice 8 della lista ordinata cioè al 100
'''
def calcola_percentili(dati, percentile):
    dati_ordinati = sorted(dati)
    indice_percentile = int(len(dati_ordinati) * percentile / 100)
    valore_percentile = dati_ordinati[indice_percentile]
    return valore_percentile

punteggi = [60, 65, 70, 75, 80, 85, 90, 95, 100]

decimo_percentile = calcola_percentili(punteggi, 10)
print("Decimo percentile:", decimo_percentile)

novantacinquesimo_percentile = calcola_percentili(punteggi, 95)
print("95-esimo percentile:", novantacinquesimo_percentile)

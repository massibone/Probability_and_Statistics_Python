'''
Due campioni seguenti provengono da popolazioni di Poisson di media λ1 e λ2. verifica l'ipotesi λ1=λ2
campione1 24 32 29 33 40 28 34 36 
campione2 42 36 41

Per verificare se le medie dei due campioni provengono da popolazioni di Poisson con lo stesso parametro λ (ovvero λ1 = λ2), 
possiamo utilizzare il test di Kolmogorov-Smirnov. Questo test viene utilizzato per confrontare due distribuzioni empiriche e 
determinare se possono essere considerate provenienti dalla stessa distribuzione.

Nel nostro caso, possiamo considerare λ1 e λ2 come le medie dei due campioni. Pertanto, la nostra ipotesi nulla sarà "λ1 = λ2," 
e vogliamo verificare se possiamo rifiutare questa ipotesi.

Il test di Kolmogorov-Smirnov restituirà un valore p (p-value) che rappresenta 
la probabilità che i due campioni provengano da popolazioni con la stessa distribuzione. 
Se il p-value è maggiore del livello di significatività (in questo caso, 0.05), 
non avremo sufficienti evidenze per rifiutare l'ipotesi che λ1 = λ2. Al contrario, 
se il p-value è inferiore al livello di significatività, 
possiamo rifiutare l'ipotesi e concludere che i due campioni provengono da popolazioni con parametri λ diversi.

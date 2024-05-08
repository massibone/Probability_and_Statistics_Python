'''
Immagina di avere una scatola di mattoncini LEGO. Vorresti costruire una macchina che possa raccogliere tutti i mattoncini gialli sparsi nella stanza. Ma non vuoi dirle esattamente cosa fare. Quindi, la prima volta, la guidi mostrandole come raccogliere i mattoncini gialli.

La prossima volta, la macchina proverà a raccogliere i mattoncini gialli da sola, guardando ciò che hai fatto la volta precedente. Se sbaglia, impara e prova di nuovo fino a quando non riesce a farlo da sola senza il tuo aiuto. Questo è un po' come il machine learning, dove il computer impara dagli esempi e diventa sempre più bravo nel fare cose da solo.
'''
# Esempio di Machine Learning per un Bambino di 10 Anni

# Importa la libreria di machine learning (scikit-learn)
from sklearn import tree

# Esempi di mattoncini gialli raccolti (dati di addestramento)
# Ogni esempio è una lista di caratteristiche (come la forma e la dimensione dei mattoncini)
features = [
    [2, 5],  # mattoncino 1
    [3, 4],  # mattoncino 2
    [1, 3],  # mattoncino 3
    [4, 6]   # mattoncino 4
]

# Etichette corrispondenti a ciascun esempio (cosa rappresenta ciascun mattoncino)
# 1 indica mattoncini gialli, 0 indica altri mattoncini
labels = [1, 1, 0, 1]  # 1=giallo, 0=non giallo

# Crea un classificatore basato su albero decisionale (decision tree)
classifier = tree.DecisionTreeClassifier()

# Addestra il classificatore con gli esempi e le etichette
classifier = classifier.fit(features, labels)

# Ora il classificatore può "imparare" da nuovi mattoncini
# Forniamo un nuovo mattoncino da testare (caratteristiche del mattoncino)
new_brick = [[2, 4]]

# Usa il classificatore per predire se il nuovo mattoncino è giallo (1) o no (0)
prediction = classifier.predict(new_brick)

# Stampa il risultato della predizione
if prediction[0] == 1:
    print("Il mattoncino è giallo!")
else:
    print("Il mattoncino non è giallo.")

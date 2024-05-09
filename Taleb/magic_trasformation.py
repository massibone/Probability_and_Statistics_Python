'''
Immagina di avere una scatola magica che trasforma numeri in altri numeri in modo speciale. Prendiamo un numero z che è dentro a una scatola, con z che può essere tra due numeri, diciamo da 1 a 10. Ora, vogliamo trasformare questo numero in un modo magico per ottenere un nuovo numero x che può essere qualsiasi numero maggiore o uguale a 1. Per farlo, usiamo la formula magica:

x = L - H log((H - z) / (H - L))

Dove L è il numero più piccolo (1) e H è il numero più grande (10). Se mettiamo il numero 5 nella scatola magica e usiamo la formula, scopriamo che x diventa 6. Inoltre, se vogliamo sapere quante volte una certa magia funziona, usiamo la formula:

f(x) = (x - L)^(1-α) / σ

Dove α è come un potere magico che cambia la forma della distribuzione dei numeri. Questa magia ci aiuta a capire meglio i numeri e a fare stime su cose importanti come la violenza o il rischio!
'''
import math

def magic_transformation(z, L, H):
    # Calcola la trasformazione magica
    x = L - H * math.log((H - z) / (H - L))
    return x

def power_law_density(x, L, alpha, sigma):
    # Calcola la densità di probabilità della legge di potenza
    return ((x - L)**(1 - alpha)) / sigma

# Esempio di utilizzo delle funzioni
L = 1
H = 10
z = 5
alpha = 0.5
sigma = 1.0

# Applica la trasformazione magica
x = magic_transformation(z, L, H)
print("x dopo la trasformazione magica:", x)

# Calcola la densità di probabilità della legge di potenza
pdf = power_law_density(x, L, alpha, sigma)
print("Densità di probabilità della legge di potenza:", pdf)

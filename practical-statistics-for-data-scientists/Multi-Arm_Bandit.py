'''
Gli A/B test sono popolari nel marketing e nel commercio elettronico, 
ma non sono l'unico tipo di esperimento statistico. 
È possibile includere trattamenti aggiuntivi e prendere misure ripetute sui soggetti. 
I trial farmaceutici, ad esempio, 
possono avere diverse opportunità per fermare l'esperimento e raggiungere una conclusione. 
I design sperimentali tradizionali rispondono a domande statiche 
sull'efficacia dei trattamenti specificati, 
ma i data scientist sono più interessati a sapere quale, 
tra molteplici opzioni, è la migliore.

Per questo motivo, viene utilizzato un nuovo tipo di design 
sperimentale: l'algoritmo multi-armed bandit. 
Inoltre, esperimenti aziendali spesso non richiedono 
permessi come quelli medici. Tuttavia, Facebook ha suscitato critiche nel 2014 
per aver condotto un esperimento sulla tonalità 
emotiva dei feed senza il consenso degli utenti.
'''
import numpy as np

class MultiArmBandit:
    def __init__(self, arms, epsilon=0.1):
        self.arms = arms
        self.epsilon = epsilon
        self.counts = np.zeros(arms)  # Numero di volte che ogni braccio è stato tirato
        self.values = np.zeros(arms)  # Valore medio di ricompensa per ogni braccio


    def select_arm(self):
        if np.random.rand() > self.epsilon:
            return np.argmax(self.values)  # Scegli il braccio con il valore medio più alto
        else:
            return np.random.randint(self.arms)  # Scegli un braccio a caso
    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]
        value = self.values[chosen_arm]
        self.values[chosen_arm] = ((n - 1) / n) * value + (1 / n) * reward
    # Numero di bracci (tipi di caramelle)
arms = 5
bandit = MultiArmBandit(arms)

# Simulazione dell'esperimento
num_trials = 1000
rewards = np.random.rand(arms)  # Ricompense vere per ogni braccio
total_reward = 0
for _ in range(num_trials):
    chosen_arm = bandit.select_arm()
    reward = rewards[chosen_arm]
    bandit.update(chosen_arm, reward)
    total_reward += reward
    
    print(f"Total reward: {total_reward}")
print(f"Arm values: {bandit.values}")
print(f"Arm values: {bandit.values}")
print(f"Arm counts: {bandit.counts}")

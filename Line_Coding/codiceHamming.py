
import numpy as np

class HammingCode:
    def __init__(self):
        # Matrice generatrice G per il codice di Hamming (7,4)
        self.G = np.array([
            [1, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0],
            [1, 1, 0, 1, 0, 0, 1]
        ])
        
        # Matrice di controllo di parità H
        self.H = np.array([
            [1, 0, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 1]
        ])

    def encode(self, message):
        """
        Codifica un messaggio di 4 bit usando il codice di Hamming (7,4)
        """
        if len(message) != 4:
            raise ValueError("Il messaggio deve essere di 4 bit")
        
        # Converte il messaggio in array numpy
        message_array = np.array(message)
        
        # Moltiplica il messaggio per la matrice generatrice
        encoded = np.remainder(np.dot(message_array, self.G), 2)
        return encoded.tolist()

    def detect_and_correct(self, received):
        """
        Rileva e corregge un singolo errore nel messaggio ricevuto
        """
        received_array = np.array(received)
        
        # Calcola la sindrome
        syndrome = np.remainder(np.dot(self.H, received_array), 2)
        
        # Converte la sindrome in decimale
        error_position = int("".join(map(str, syndrome)), 2)
        
        if error_position != 0:
            # Corregge l'errore
            received[error_position - 1] ^= 1
            
        return received

    def decode(self, received):
        """
        Decodifica il messaggio ricevuto nei 4 bit originali
        """
        # Prima corregge eventuali errori
        corrected = self.detect_and_correct(received)
        
        # Estrae i bit di informazione (posizioni 0,1,3,4)
        return [corrected[2], corrected[4], corrected[5], corrected[6]]

# Esempio di utilizzo
def main():
    # Crea un'istanza del codificatore
    hamming = HammingCode()
    
    # Messaggio originale di 4 bit
    message = [1, 0, 1, 1]
    print(f"Messaggio originale: {message}")
    
    # Codifica il messaggio
    encoded = hamming.encode(message)
    print(f"Messaggio codificato: {encoded}")
    
    # Simula un errore nel messaggio codificato
    received = encoded.copy()
    error_position = 2  # Introduciamo un errore nella posizione 2
    received[error_position] ^= 1
    print(f"Messaggio ricevuto con errore: {received}")
    
    # Corregge l'errore e decodifica
    decoded = hamming.decode(received)
    print(f"Messaggio decodificato: {decoded}")

if __name__ == "__main__":
    main()


import numpy as np

class HammingCode:
    """
    Implementa il codice di Hamming (7,4) utilizzando un approccio sistematico.
    In un codice sistematico, i bit del messaggio originale sono direttamente
    incorporati nella parola di codice, rendendo la decodifica più intuitiva.
    """
    def __init__(self):
        # Matrice generatrice G in forma sistematica [I_4 | P]
        # I_4 è la matrice identità 4x4.
        # P è la matrice che calcola i bit di parità.
        # I bit di dati (d1,d2,d3,d4) vengono mappati direttamente nelle prime 4 posizioni.
        # I bit di parità (p1,p2,p3) vengono calcolati e messi nelle posizioni 5,6,7.
        self.G = np.array([
            [1, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 1]
        ], dtype=int)
        
        # Matrice di controllo di parità H in forma sistematica [P^T | I_3]
        # P^T è la trasposta della matrice P dalla matrice G.
        # I_3 è la matrice identità 3x3.
        # Questa struttura è direttamente correlata a G e semplifica la verifica.
        self.H = np.array([
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 0, 1]
        ], dtype=int)
        
        # Matrice di decodifica R (per un codice sistematico, è semplice)
        # Estrae semplicemente i bit di dati (le prime 4 colonne).
        self.R = np.array([
            [1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0]
        ], dtype=int)

    def encode(self, message: list) -> list:
        """
        Codifica un messaggio di 4 bit usando il codice di Hamming (7,4).
        
        Args:
            message: Messaggio di 4 bit da codificare (es. [1, 0, 1, 1]).
        
        Returns:
            Lista contenente il messaggio codificato di 7 bit.
        
        Raises:
            ValueError: Se l'input non è una lista di 4 bit.
        """
        if not isinstance(message, list) or len(message) != 4 or not all(bit in [0, 1] for bit in message):
            raise ValueError("Il messaggio deve essere una lista di 4 bit (0 o 1).")
        
        message_array = np.array(message)
        
        # Moltiplica il messaggio per la matrice generatrice e calcola il resto mod 2.
        encoded = np.dot(message_array, self.G) % 2
        return encoded.tolist()
    
    def detect_and_correct(self, received: list) -> tuple[list, int]:
        """
        Rileva e corregge un singolo errore nel messaggio ricevuto di 7 bit.
        
        Args:
            received: Messaggio ricevuto di 7 bit.
        
        Returns:
            Una tupla contenente:
            - La parola di codice corretta (lista di 7 bit).
            - La posizione dell'errore (0 se non ci sono errori).
        
        Raises:
            ValueError: Se l'input non è una lista di 7 bit.
        """
        if not isinstance(received, list) or len(received) != 7 or not all(bit in [0, 1] for bit in received):
            raise ValueError("Il messaggio ricevuto deve essere una lista di 7 bit (0 o 1).")
        
        received_array = np.array(received)
        
        # Calcola la sindrome: H * received^T (mod 2)
        syndrome = np.dot(self.H, received_array) % 2
        
        # Converte la sindrome (un array binario) in un indice intero.
        # La sindrome corrisponde a una colonna della matrice H.
        # Se la sindrome non è zero, la sua sequenza binaria indica la colonna (e quindi la posizione) dell'errore.
        error_position = 0
        if np.any(syndrome):
            # Cerca la colonna in H che corrisponde alla sindrome
            for i in range(self.H.shape[1]):
                if np.array_equal(self.H[:, i], syndrome):
                    error_position = i + 1  # Le posizioni sono 1-based
                    break
        
        if error_position != 0:
            print(f"\nErrore rilevato nella posizione {error_position}.")
            # Corregge l'errore invertendo il bit. Le posizioni sono 1-based, gli indici 0-based.
            received[error_position - 1] ^= 1
            print(f"Messaggio dopo la correzione: {received}")
            
        return received, error_position

    def decode(self, received: list) -> list:
        """
        Decodifica un messaggio di 7 bit (prima correggendolo) nei 4 bit originali.
        
        Args:
            received: Messaggio ricevuto di 7 bit.
        
        Returns:
            Messaggio decodificato di 4 bit.
        """
        # Passo 1: Rileva e corregge eventuali errori nel messaggio ricevuto.
        corrected_message, _ = self.detect_and_correct(received)
        
        # Passo 2: Estrae i bit di dati.
        # Grazie alla forma sistematica di G, i bit di dati sono semplicemente i primi 4.
        # L'operazione matriciale con R è il modo formale per farlo.
        decoded = np.dot(corrected_message, self.R.T)
        
        return decoded.tolist()

def main():
    """
    Funzione principale per dimostrare il funzionamento del codice di Hamming.
    """
    try:
        # Crea un'istanza del codificatore/decodificatore
        hamming = HammingCode()
        
        # 1. Messaggio originale
        message = [1, 0, 1, 1]
        print("--- Esempio di Esecuzione ---")
        print(f"Messaggio originale (4 bit):    {message}")
        
        # 2. Codifica del messaggio
        encoded = hamming.encode(message)
        print(f"Messaggio codificato (7 bit):   {encoded}")
        
        # 3. Simulazione di un errore
        # Copiamo il messaggio codificato e introduciamo un errore.
        received = encoded.copy()
        error_index = 4  # Posizione 5
        received[error_index] ^= 1 # Inverte il bit (0->1 o 1->0)
        print(f"Messaggio ricevuto con errore:  {received} (errore introdotto all'indice {error_index})")
        
        # 4. Decodifica e correzione
        # La funzione decode chiama internamente detect_and_correct.
        decoded = hamming.decode(received)
        print(f"\nMessaggio decodificato (4 bit): {decoded}")
        
        # 5. Verifica
        if message == decoded:
            print("\nVerifica: SUCCESSO! Il messaggio originale è stato ripristinato correttamente.")
        else:
            print("\nVerifica: FALLIMENTO! Il messaggio decodificato non corrisponde all'originale.")

    except ValueError as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    main()

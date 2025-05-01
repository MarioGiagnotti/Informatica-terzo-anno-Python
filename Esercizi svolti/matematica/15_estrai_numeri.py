import random

def estrai_numeri():
    gruppi = [
        list(range(1, 16)),
        list(range(1, 16)),
        list(range(1, 16)),
        list(range(1, 16))
    ]
    
    iterazione = 1
    
    while all(len(gruppo) > 0 for gruppo in gruppi):
        estratti = []
        for gruppo in gruppi:
            numero = random.choice(gruppo)
            estratti.append(numero)
            gruppo.remove(numero)
        
        print(f"Iterazione {iterazione}: Numeri estratti = {estratti}")
        iterazione += 1
    
    print("Non ci sono più numeri disponibili in tutti i gruppi per un'estrazione completa.")

estrai_numeri()

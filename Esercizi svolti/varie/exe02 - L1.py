def exe02():
    '''
    Problema: Dato un numero intero stampare a video il doppio del numero inserito, il quadrato del numero inserito e la somma del doppio e del quadrato
    
    Analisi: Devo chiedere all'utente un dato: un numero intero num
    Ottenuto il dato di input posso calcolare il doppio come num_doppio = 2 * num
    poi posso calcolare il quadrato come num_quad = num * num
    poi posso calcolare la somma come sum = num_doppio + num_quad
        
    
    Strategia risolutiva in pseudocodice:
    
    1. num <-- Chiedi all'utente "Inserisci un numero intero" e fai il casting in int
    2. num_doppio <-- Calcola il doppio del numero come come num_doppio = num * 2
    3. num_quad <--Calcola il quadrato del numero come num_quad = num * num
    4. sum <-- Calcola la somma come sum = num_doppio + num_quad
    5. Stampa a video "Il doppio del numero inserito è: ", num_doppio
    6. Stampa a video "Il quadrato del numero inserito è: ", num_quad
    7. Stampa a video "La somma del doppio e del quadrato del numero inserito è: ", sum
    
    '''
print(exe02.__doc__)

num = int(input("Inserisci un numero intero ")) #1
num_doppio = num * 2 #2
num_quad = num * num #3
sum = num_doppio + num_quad #4
print("Il doppio del numero inserito è: \n",num_doppio) #5
print("Il quadrato del numero inserito è: \n",num_quad) #6
print("La somma del doppio e del quadrato del numero inserito è: \n",sum) #7
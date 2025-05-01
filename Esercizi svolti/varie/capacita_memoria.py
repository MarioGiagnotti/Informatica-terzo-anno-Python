def exe01():
    '''
    Problema: Dato il numero di fili dell' Address Bus e la dimensione della locazione di memoria determinare la Capacità totale 
    
    Analisi: Devo chiedere all'utente due dati: numero di fili del bus indirizzi e dimensione della locazione di memoria
    Ottenuti i dati di input posso calcolare l'output come C = (2^numero di fili) * dimensione locazione
    Chiedo la dimensione in bit e restituisco la capacità in bit, in byte (Dividendo C per 2^3), in KiB (dividendo il risultato 
    dell'operazione precedente per 2^10), in MiB (dividendo il risultato dell'operazione precedente per 2^10), in GiB (dividendo il risultato dell'operazione precedente per 2^10),
    
    
    Strategia risolutiva in pseudocodice:
    
    1. importa math
    2. dim_loc <-- Chiedi all'utente "inserisci la dimensione in bit della locazione di memoria" e fai il casting in int
    3. num_fili <-- Chiedi all'utente "inserisci il numero di fili del bus indirizzi" e fai il casting in int
    4. C_bit<--Calcola C = (2^numero di fili) * dimensione locazione
    5. Stampa a video "La Capacità della memoria in bit è: ", C_bit
    6. C_byte<--Calcola C_byte = C_bit/(2^3) 
    7. Stampa a video "La Capacità della memoria in byte è: ", C_byte
    8. C_kiB<--Calcola C_kiB = C_byte/(2^10) 
    9. Stampa a video "La Capacità della memoria in kiB è: ", C_kiB
    10. C_MiB<--Calcola C_MiB = C_kiB/(2^10) 
    11. Stampa a video "La Capacità della memoria in MiB è: ", C_MiB
    12. C_GiB<--Calcola C_GiB = C_MiB/(2^10) 
    13. Stampa a video "La Capacità della memoria in GiB è: ", C_GiB
    '''
print(exe01.__doc__)

import math #1
dim_loc = int(input("Inserisci la dimensione in bit della locazione di memoria ")) #2
num_fili = int(input("Inserisci il numero di fili del bus indirizzi ")) #3
C_bit = (pow(2,num_fili)*dim_loc) #4
print("La Capacità della memoria in bit è: \n",C_bit) #5
C_byte = (C_bit/pow(2,3)) #6
print("La Capacità della memoria in byte è: \n",C_byte) #7
C_kiB = (C_byte/pow(2,10)) #8
print("La Capacità della memoria in kiB è: \n",C_kiB) #9
C_MiB = (C_kiB/pow(2,10)) #10
print("La Capacità della memoria in MiB è: \n",C_MiB) #11
C_GiB = (C_MiB/pow(2,10)) #10
print("La Capacità della memoria in GiB è: \n",C_GiB) #11

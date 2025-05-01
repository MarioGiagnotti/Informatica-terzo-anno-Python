def exe02():
    '''
    Problema: Dati hit time, Miss time e percentuale di hit determinare il tempo medio di accesso alla cache 
    
    Analisi: Devo chiedere all'utente tre dati: Ht=hit time (in ns), Mt=miss time (in ns) e Hr=percentuale di hit (come intero)
    Ottenuti i dati di input posso calcolare l'output come Tma = Ht*Hr/100 + Mt* (1-Hr/100)
    
    
    
    Strategia risolutiva in pseudocodice:
    
    1. importa math
    2. Ht <-- Chiedi all'utente "inserisci il tempo di hit in nanosecondi" e fai il casting in float
    3. Mt <-- Chiedi all'utente "inserisci il tempo di miss in nanosecondi" e fai il casting in float
    4. Hr <-- Chiedi all'utente "Inserissci l'Hit rate come intero" e fai il casting a float
    5. Hrp<--Calcola Htp = Hr/100
    6. Mrp<--Calcola Mrp = 1-Hrp
    7. Tma_nan<--Calcola Tma_nan = Ht*Hrp + Mt*Mrp
    8. Stampa a video "Il tempo medio di accesso alla memoria in nanosecondi è: ", Tma_nan
    9. Tma_mic<--Calcola il tempo medio in microsecondi come Tma/(10^3)
    10. Stampa a video "Il tempo medio di accesso alla memoria in microsecondi è: ", Tma_mic
    '''
print(exe02.__doc__)

import math #1
Ht= float(input("Inserisci il tempo di hit in nanosecondi ")) #2
print("Ht: \n", Ht)
Mt = float(input("Inserisci il tempo di miss in nanosecondi ")) #3
print("Mt: \n", Mt)
Hr = float(input("Inserisci l'Hit rate come intero ")) #4
print("Hr: \n", Hr)
Hrp = Hr/100  #5
print("Hrp: \n", Hrp)
Mrp = (100 - Hr)/100 #6
print("Mrp: \n", Mrp)
Tma_nan =  Ht*Hrp + Mt*Mrp #7
print("Il tempo medio di accesso alla memoria in nanosecondi è: \n",Tma_nan) #8
Tma_mic = (Tma_nan/pow(10,3)) #9
print("Il tempo medio di accesso alla memoria in microsecondi è: \n",Tma_mic) #10

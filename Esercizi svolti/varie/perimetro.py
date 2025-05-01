def exe01():
    '''
    Problema: Dato il perimetro di un quadrato determinare l'area
    
    Analisi: Devo chiedere all'utente un dato: il valore del perimetro del quadrato
    Ottenuto il dato di input posso calcolare la misura del lato come l = P/4
    e poi posso calcolare l'output come A = l*l
        
    
    Strategia risolutiva in pseudocodice:
    
    1. P <-- Chiedi all'utente "Inserisci il valore del perimetro" e fai il casting in float
    2. l <-- Calcola il lato come l=P/4
    3. A <--Calcola l'area come A = l*l
    4. Stampa a video "L'area del quadrato è: ", A
    
    '''
print(exe01.__doc__)

P = float(input("Inserisci il valore del perimetro ")) #1
l = P/4 #2
A = l*l #3
print("L'area del quadrato è: \n",A) #4

def aree():
    """
    Scrivi una funzione che, a scelta dell'utente, calcoli l'area di:

    
    un quadrato
    un rettangolo
    un triangolo
    un cerchio

    Algoritmo: devo proporre all'utente un menù associando la scelta ad un numero e poi in base alla scelta eseguita 
    chiedo il valore dei lati o del raggio. Eseguo il calcolo e rispondo con il risultato

    Pseudocodice: 
    importo math
    1) stampo il menù assoiando un numeo ad ogni scelta
    2) chiedo in input il numero che rappresenta la scelta e lo memorizzo in una variabile
    3) se scelta è '1':
        4a)chiedo il lato e lo memorizzo in l
        4b)calcolo l'area come area = pow(l,2)
        4c) stampo il risultato
    4) altrimenti se scelta è '2':
        4a)chiedo la base e la memorizzo in b
        4b)chiedo l'altezza e la memorizzo in h
        4c)calcolo l'area come area = b*h
        4d) stampo il risultato
    5) altrimenti se scelta è '3':
        5a)chiedo la base e la memorizzo in b
        5b)chiedo l'altezza e la memorizzo in h
        5c)calcolo l'area come area = b*h/2
        5d) stampo il risultato
    6) altrimenti se scelta è '4':
        6a)chiedo il raggio e lo memorizzo in r
        6b)calcolo l'area come area = pow(r,2)*math.pi
        6c) stampo il risultato
    7)altrimenti:
        stampo (il numero non corrisponde a una scelta corretta)
     """
print(aree.__doc__)

#code
import math
print("""
    Fai la tua scelta:
    Area Quadrato --> 1
    Area Rettangolo--> 2
    Area Triangolo--> 3
    Area Cerchio--> 4
    """)

scelta = int(input("Di quale figura geometrica desideri calcolare l'area? \n"))
if scelta == 1:
    l = float(input('Inserisci il valore del lato del quadrato '))
    print("L'Area del Quadrato, avente lato",l," è: ",pow(l,2) )
elif scelta == 2:
    b = float(input('Inserisci il valore della base '))
    h = float(input('Inserisci il valore dell´altezza '))
    print("L'Area del Rettangolo, avente base", b, " e altezza ", h ," è: ", b*h)
elif scelta == 3:
    b = float(input('Inserisci il valore della base '))
    h = float(input('Inserisci il valore dell´altezza '))
    print("L'Area del Triangolo, avente base", b, " e altezza ", h ," è: ", b*h/2)
elif scelta == 4:
    r = float(input('Inserisci il valore del raggio '))
    print("L'Area del Cerchio, avente raggio",r," è: ",pow(r,2) * math.pi )
else:
    print ('Nessun calcolo disponibile per la scelta effettuata!')

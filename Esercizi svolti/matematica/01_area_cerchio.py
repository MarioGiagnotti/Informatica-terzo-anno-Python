def area_cerchio():
    """

    Algoritmo:
    Per calcolare l'area del cerchio ho bisogno di conoscere il raggio. Per implementare la soluzione 
    ho necessità di definire una variabile (raggio) e assegnarle un valore casuale (anche decimale).
    Ho necessità di definire una variabile (pi) che rappresenti il pigreco troncando il valore al 
    secondo digit (scelta personale). Dopo aver definito le variabili calcolo l'area con 
    la formula pi*raggio*raggio ed assegno il risultato ad una variabile (Area). 
    Stampo poi a video il risultato

    Pseudocodice:
    1)Definisco la variabile raggio e le assegno un numero casuale
    2)Definisco la variabile pi e le assegno il valore 3.14
    3)Definisco la variabile Area e le assegno l'espressione pi*raggio*raggio
    4)Stampo "L'area del cerchio di raggio",raggio "è: ", Area
    

    """
print(area_cerchio.__doc__)

#code
raggio = 3.72
pi = 3.14
Area = pi * raggio * raggio
print("L'area del cerchio di raggio", raggio, "è: ",Area)
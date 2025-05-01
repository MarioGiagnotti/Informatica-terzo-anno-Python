def procedimento ():
    """
    algoritmo:
    chiedo all'utente di indovinare un numero da 1 a 10 impostando un ciclo while
    
    """

print (procedimento.__doc__)

#codice

import random

target = random.randint(1, 11)
indovinato = True

while indovinato:
    n = int(input("scegli un numero da 1 a 10"))
    if n == target:
        indovinato = False
        print("hai indovinato")
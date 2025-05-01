numero = float(input("Inserisci un numero: "))
if numero > 0:
    if numero%2 == 0:
        print ("Il numero "+str(numero)+" è positivo ed è multiplo di 2")
    else:
        print ("Il numero "+str(numero)+" è positivo e non è multiplo di 2")
else:
        print ("Il numero "+str(numero)+" è negativo")
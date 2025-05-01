numero = int(input("Inserisci un numero: "))
if numero % 5 > 0:
    print("Il numero "+str(numero)+" non è divisibile per 5")
else:
    print("Il numero "+str(numero)+" è divisibile per 5 ed il risultato è: "+str(numero/5))
numero = int(input("Inserisci un numero intero positivo: "))

prodotto = 1
i = 1
while i <= numero:
    prodotto *= i
    i += 1

print("Il prodotto dei numeri da 1 a "+str(numero)+" è : ",prodotto)

numero = int(input("Inserisci un numero intero positivo: "))

fattoriale = 1
for i in range(1, numero + 1):
    fattoriale *= i

print("Il fattoriale di ",numero," è: ",fattoriale)

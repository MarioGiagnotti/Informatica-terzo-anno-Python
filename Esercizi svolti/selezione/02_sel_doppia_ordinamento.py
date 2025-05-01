def sel_doppia2():
    """
    Ordina due numeri in modo crescente

    Algoritmo:
    Dopo aver chiesto due numeri in input se il primo è minore del secondo stampa il primo e poi il secondo altrimenti stampa il secondoe poi ilprimo

    Pseudocodice
    1. chiedi all'utente il primo numero intero e memorizzalo nella variabile a
    2. chiedi all'utente il secondo numero intero e memorizzalo nella variabile b
    3. se n1 < n2 stampa (a), stampa (b) altrimenti stampa (b), stampa (a)
    """
print(sel_doppia2.__doc__)

#code
a = int(input("Primo numero: "))
b = int(input("Secondo numero: "))

if a < b: 
    print(a)
    print(b)
else:
    print(b)
    print(a)
            
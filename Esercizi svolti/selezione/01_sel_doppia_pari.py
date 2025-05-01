def sel_doppia():
    """
    Verifica se un numero è pari o dispari (un numero è pari quando il resto della divisione intera per 2 è uguale a 0)

    Algoritmo:
    Dopo aver chiesto un numero intero in input lo divido per 2. Se i resto è zero stampa 'il numero è pari' altrimenti stampa 'il numero è dispari

    Pseudocodice
    1. chiedi all'utente un numero intero e memorizzalo nella variabile n
    2. calcolo ul resto della divisione per 2 e lo memorizzo nella variabile r
    3. se r == 0 stampa ("Il numero è pari") altrimenti stampa ("Il numero è dispari")
    """
print(sel_doppia.__doc__)
#code
n = int(input("Inserisci un numero intero \n"))
r = n%2
if r == 0:
    print("Il numeroè pari")
else:
    print("Il numero è dispari")
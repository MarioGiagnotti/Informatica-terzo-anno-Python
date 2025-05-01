def liste():
    """
    Algoritmo:

    Creo tre liste, una per studente, contenente i seguenti dati: Nome, Cognome, Data di nascita, Comune di nascita, Comune di residenza.
    Poi stampare a video per ciascuna lista: 
    - Cognome e Data di nascita (su una sola riga)
    - Cognome, Comune di nascita e Comune di residenza (su una sola riga)
    utilizzando l'operatore ":" per definire un range e l'operatore "+" per concatenare.
    I campi hanno indice che parte da 0 e si incrementa. Per definire un range occorre indicare l'indice di partenza
    : indice_arrivo +1;
    
    Pseudocodice:
    1. Definisco list1 racchiudendo i campi tra [ ], completando i campi richiesti e dividendoli con una virgola.
    2. Definisco list2 racchiudendo i campi tra [ ], completando i campi richiesti e dividendoli con una virgola.
    3. Definisco list3 racchiudendo i campi tra [ ], completando i campi richiesti e dividendoli con una virgola.
    4. Definisco gli indici e li memorizzo in due variabili
    5. Stampo a video gli elementi della lista da indice di partenza a indice di arrivo per list1
    6. Stampo a video gli elementi della lista da indice di partenza a indice di arrivo per list2
    7. Stampo a video gli elementi della lista da indice di partenza a indice di arrivo per list3
    8. Stampare a video il secondo, il quarto e il quinto elemento della variabile list1.
    9. Stampare a video il secondo, il quarto e il quinto elemento della variabile list2.
    10. Stampare a video il secondo, il quarto e il quinto elemento della variabile list3.
    
    """
    
print(liste.__doc__)

#codice

list1 = ["Nome: Mario", "Cognome: Rossi", "Data di nascita: 01/01/2001", "Comune di nascita: Milano", "Comune di residenza: Bergamo"]
list2 = ["Nome: Giuseppe", "Cognome: Verdi", "Data di nascita: 02/02/2002", "Comune di nascita: Ancona", "Comune di residenza: Torino"]
list3 = ["Nome: Luigi", "Cognome: Bianchi", "Data di nascita: 03/03/2003", "Comune di nascita: Verona", "Comune di residenza: Venezia"]

indice_nome = 1
indice_data = 3
print(list1[indice_nome:indice_data])
print(list2[indice_nome:indice_data])
print(list3[indice_nome:indice_data])

print(list1[1], "-", list1[3], "-", list1[4])
print(list2[1], "-", list2[3], "-", list2[4])
print(list3[1], "-", list3[3], "-", list3[4])
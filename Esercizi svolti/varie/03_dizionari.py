def dizionari ():
    """
    Algoritmo:

    Creo tre dizionari costituiti dai dati di tre studenti. Essi contengono chiavi e relativi valori di:
    - Nome.
    - Cognome.
    - Data di nascita.
    - Comune di nascita.
    - Comune di residenza.
    Per ogni dizionario stampo a video solo i valori relativi a:
    - Cognome e Data di nascita.
    Per ogni dizionario stampo a video chiavi e valori relativi a:
    - Cognome, Comune di Nascita e Comune di residenza.
    i metodi keys() e values() di un dizionario non supportano l'indicizzazione diretta come le liste o le tuple per cui devo
    necessariamente convertire chiavi e valori in liste
    
    Pseudocodice:
    1. Definisco dic1 utilizzando le parentesi graffe e scrivendo chiave : valore per ogni campo.
    2. Definisco dic2 utilizzando le parentesi graffe e scrivendo chiave : valore per ogni campo.
    3. Definisco dic3 utilizzando le parentesi graffe e scrivendo chiave : valore per ogni campo.
    4. faccio il casting a lista delle chiavi
    5. faccio il casting a lista dei valori
    6. Stampo a video il valore di Cognome e il valore di Data di nascita del primo dizionario.
    7. Stampo a video il valore di Cognome e il valore di Data di nascita del secondo dizionario.
    8. Stampo a video il valore di Cognome e il valore di Data di nascita del terzo dizionario.
    9. Stampo a video chiave e valore di Cognome, Comune di nascita e di Comune di residenza del primo dizionario.
    10. Stampo a video chiave e valore di Cognome, Comune di nascita e di Comune di residenza del secondo dizionario.
    11. Stampo a video chiave e valore di Cognome, Comune di nascita e di Comune di residenza del terzo dizionario.
    
    """

print(dizionari.__doc__)

#codice
dic1 = {"Nome": "Mario", "Cognome": "Rossi", "Data di nascita": "01/01/2001", "Comune di nascita": "Milano", "Comune di residenza": "Bergamo"}
dic2 = {"Nome": "Giuseppe", "Cognome": "Verdi", "Data di nascita": "02/02/2002", "Comune di nascita": "Ancona", "Comune di residenza": "Torino"}
dic3 = {"Nome": "Luigi", "Cognome": "Bianchi", "Data di nascita": "03/03/2003", "Comune di nascita": "Verona", "Comune di residenza": "Venezia"}

lista_chiavi = list(dic1.keys()) #faccio il casting a lista (le chiavi sono identiche per i tre dizionari)
lista_valori_dic1 = list(dic1.values())
lista_valori_dic2 = list(dic2.values())
lista_valori_dic3 = list(dic3.values())

print(lista_valori_dic1[1], lista_valori_dic1[2])
print(lista_valori_dic2[1], lista_valori_dic2[2])
print(lista_valori_dic3[1], lista_valori_dic3[2])
print(lista_chiavi[1],":", lista_valori_dic1[1],",", lista_chiavi[3],":", lista_valori_dic1[3],",", lista_chiavi[4],":", lista_valori_dic1[4])
print(lista_chiavi[1],":", lista_valori_dic2[1],",", lista_chiavi[3],":", lista_valori_dic2[3],",", lista_chiavi[4],":", lista_valori_dic2[4])
print(lista_chiavi[1],":", lista_valori_dic3[1],",", lista_chiavi[3],":", lista_valori_dic3[3],",", lista_chiavi[4],":", lista_valori_dic3[4])
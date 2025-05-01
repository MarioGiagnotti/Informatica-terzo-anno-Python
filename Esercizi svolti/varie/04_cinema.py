def cinema ():
    """
    problema: 
    Calcola l'importo totale da pagare al cinema e stampa il risultato, sapendo che:
    ogni 15 studenti spetta una gratuità e che per chi ha meno di 17 anni il biglietto 
    è scontato del 50%

    
    Algoritmo:

    Leggo in input il numero totale degli studenti
    Leggo in input il numero degli under 17
    Leggo in input l'importo del biglietto
    Devo calcolare quante gratuità ci sono facendo la divisione intera (divisione senza resto) 
    con l'operatore // tra il totale degli studenti e 15
    Calcolo il numero dei paganti prezzo intero e il numero di paganti prezzo ridotto
    Calcolo il costo complessivo
    
    Pseudocodice:
    1. dichiaro la costante MAX = 15 che mi serve per le gratuità
    2. dichiaro la costante PERCENTAGE = 0.5 che mi serve per il calcolo del prezzo ridotto
    1. Chiedo in input il numero degli studenti facendo il casting a int
    2. Chiedo in input il numero degli studenti che hanno meno di 17 anni facendo il casting a int
    3. Chiedo in input il prezzo del biglietto
    4. Calcolo il numero delle gratuità
    5. Sottraggo dal totale le graturità
    6. Calcolo il costo totale dei paganti a prezzo pieno
    7. Calcolo il costo totale dei paganti a prezzo ridotto
    8. Sommo i due valori precedenti
    9. stampo la somma

    """
print(cinema.__doc__)

#codice
MAX = 15
PERCENTAGE = 0.5
num_tot_studenti = int(input("Inserisci il numero totale degli studenti "))
u17_studenti = int(input("Inserisci il numero di studenti che hanno meno di 17 anni "))
biglietto = int(input("Inserisci il costo del biglietto "))
gratuità = num_tot_studenti // MAX
totale_paganti = num_tot_studenti - gratuità
tot_prezzo_pieno = (totale_paganti - u17_studenti) * biglietto
tot_prezzo_ridotto = u17_studenti * biglietto * PERCENTAGE
tot = tot_prezzo_pieno + tot_prezzo_ridotto

print("Il costo complessivo è di: ",tot, " €")
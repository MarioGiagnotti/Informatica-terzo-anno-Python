def exe02():
    '''
    Problema: Calcola l'importo totale da pagare al cinema, sapendo che:
    o ogni 15 studenti spetta una gratuità e che per chi ha meno di 17 anni il
    biglietto è scontato del 50%
    o leggi in input il numero totale di studenti
    o il numero di studenti con meno di 17 anni
    o il costo del biglietto.
    
    
    Analisi: Devo chiedere all'utente tre dati: numero di studenti complessivo, il numero di studenti che hanno meno di 17 anni
    ed il costo del biglietto.
    Ottenuto il numero totale di studenti  calcolo quante gratuità spettano utilizzando l'operatore // tra numero totale studenti e 15
    calcolo poi gli studenti paganti sotraendo dal numero totale di studenti le gratuità 
    calcolo poi gli studenti paganti il prezzo intero sottraendo algli studenti paganti il numero di studenti con meno di 17 anni
    calcolo il costo totale degli studenti paganti prezzo intero moltiplicando il risultato precedente per il costo del biglietto
    calcolo il prezzo totale scontato per gli studenti con meno di 17 anni moltiplicando il numero di tali studenti * il costo del biglietto *0.5
    calcolo l'importo totale sommando i due risultati precedenti
    
    
    Strategia risolutiva in pseudocodice:
    
    1. num_stu <-- Chiedi all'utente "Inserisci il numero totale degli studenti" e fai il casting in int
    2. num_17 <-- Chiedi all'utente "Inserisci il numero degli studenti che hanno meno di 17 anni" e fai il casting in int
    3. biglietto <-- Chiedi all'utente "Inserisci il prezzo del biglietto" e fai il casting in float
    4. gratis <-- num_stu//15
    5. paganti <-- num_stu - gratis
    6. paganti_intero <-- paganti - num_17
    7. costo_pag_intero <-- paganti_intero * biglietto
    8. costo_pag_sco <-- num_17 * biglietto * 0.5
    9. costo_tot <-- costo_pag_intero + costo_pag_sco
    10. Stampa a video "Il costo totale è: ", costo_tot
    '''
print(exe02.__doc__)

num_stu = int(input("Inserisci il numero totale di studenti: "))#1
num_17 = int(input("Inserisci il numero di studenti con meno di 17 anni: "))#2
biglietto = float(input("Inserisci il costo del biglietto: "))#3
gratis = num_stu//15#4
paganti = num_stu - gratis#5
paganti_intero = paganti - num_17#6
costo_pag_intero = paganti_intero * biglietto#7
costo_pag_sco = num_17 * biglietto * 0.5#8
costo_tot = costo_pag_intero + costo_pag_sco#9
print("Il costo complessivo per l'ingresso al cinema è: {:7.2f} \u20AC".format(costo_tot))#10
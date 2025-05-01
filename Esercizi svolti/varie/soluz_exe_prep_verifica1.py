def exe01():
    '''
    Problema: Descrivere l'algoritmo risolutivo in pseudocodice del seguente problema:
    o Dato un numero di studenti e sapendo che gli accompagnatori sono 4,
    calcolare il costo complessivo dell'ingresso a teatro sapendo che: il costo unitario del biglietto è di €15 e
    che i quattro accompagnatori hanno uno sconto del 20%.
    
    
    Analisi: Devo chiedere all'utente un dato: numero di studenti
    Ottenuto il dato di input posso calcolare il costo per gli studenti moltiplicando il numero per il prezzo del biglietto.
    Calcolo poi il costo per gli accompagnatori moltiplicando il prezzo * 4 (accompagnatori) e per 0,8 (sconto del 20%)
    Calcolo l'output come somma dei costi precedentemente ottenuti
    
    
    Strategia risolutiva in pseudocodice:
    
    1. num_stu <-- Chiedi all'utente "inserisci il numero degli studenti" e fai il casting in int
    2. PREZZO_B <-- 15
    3. NUM_ACC <-- 4
    4. costo_stu <-- num_stu * prezzo_b
    5. costo_acc_sco <-- prezzo_b * 4 * 0.8
    6. costo_tot <-- costo_stu + costo_acc_sco 
    7. Stampa a video "Il costo totale è: ", costo_tot
    '''
print(exe01.__doc__)

num_stu = int(input("Inserisci il numero di studenti: "))#1 
PREZZO_B = 15#2
NUM_ACC = 4#3
costo_stu = num_stu * PREZZO_B#4
costo_acc_sco = PREZZO_B * 4 *0.8#5
costo_tot = costo_stu + costo_acc_sco#6
print("Il costo complessivo per l'ingresso a teatro è: {:5.2f} \u20AC".format(costo_tot))#7
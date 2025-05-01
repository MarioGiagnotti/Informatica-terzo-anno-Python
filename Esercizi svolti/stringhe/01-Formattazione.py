def formattazione():
    '''
    la formattazione viene eseguita da una stringa racchiusa da apiti o virgolette seguita dal punto e dalla parola chiave format
    più precisamente format() è un metodo applicato ad una stringa
    All'interno della stringa viene inserito uno o più placeholder racchiusi da una coppia di parentesi graffe che specificano il formato del dato
    mentre format ha come argomento il dato da formattare
    
    le specifice di formato sono contrassegante di caratteri %d per gli interi, da %f per i float e da %s per le stringhe
    per visualizzare il risultato del dato formattato entro x posizioni dopo l'ultimo carattere stampato a video si usa :x 
    
    INDICI POSIZIONALI:
    {0:20} {1:45} 0 e 1 sono indici di posizione mentre 20 e 45 sono le posizioni (la prima posizione è sempre la 0)
    
    ALLINEAMENTO
     di default le stringhe sono allineate a destra mentre i numeri a sinistra. Si può modificare l'allineamento se dopo i : si inserisce
     < per allineamento a sx
     ^ per allineamento centrato
     > per allineamento a destra
     
     SEGNI
     I dati numerici vengono visualizzati con segno se dopo i : viene inserito il carattere +. Se viene inserito uno spazio vengono visualizzati
     i segni solo per i numeri negativi
     
     FORMATTAZIONE CON LE F-STRING
     Senza l'uso del metodo format() si può anteporre alla stringa da formattare la lettera f
    '''
print(formattazione.__doc__)

p = 1200
print("Il prezzo è {:10.2f}".format(p)) #valore entro 10 caratteri e 2 cifre decimali

età = 18
print("Mario ha: {:3d}".format(età),"anni")

cognome = "Rossi"
nome = "Mario"
età = 47
print("L'utnte si chiama: {:10s} {:10s} ed ha: {:2d} anni".format(cognome, nome, età))

#indici posizionali
cognome = "Rossi"
nome = "Mario"
età = 47
print("L'utnte si chiama: {0:10} {1:20} ed ha: {2:2} anni".format(cognome, nome, età))

a=10
print("Il numero è: {0:2d}, il doppio è: {1:2d}, il triplo è: {2:2d}".format(a,a*2,a*3))

peso=0.230
prezzo=6.25
totale= peso * prezzo
print("Il peso è: {0:5.2f}, il prezzo è: {1:5.2f}, il totale è: {2:7.2f}".format(peso,prezzo,totale))

print("Il peso è: {0:5.2f} kg, il prezzo è: {1:5.2f} \u20AC/kg, il totale è: {2:7.2f} \u20AC".format(peso,prezzo,totale)) #con € (unicode u20AC)

#allineamento
print("L'utnte si chiama: {0:^10} {1:>20} ed ha: {2:<2} anni".format(cognome, nome, età))

#SEGNO
a=18
b=-18
print("{0:+d} {1:+d}".format(a,b))
print("{0: d} {1: d}".format(a,b))

#Formattazione con f-string
print(f"Il peso è: {peso:5.2f} kg, il prezzo è: {prezzo:5.2f} \u20AC/kg, il totale è: {totale:7.2f} \u20AC")
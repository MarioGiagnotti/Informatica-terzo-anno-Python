nome = input("Inserisci il tuo nome: ")
eta = int(input("Inserisci la tua età: "))
ANNO_CORRENTE = 2024
anno_nascita = str(ANNO_CORRENTE - eta)
print("Ciao "+nome+", se hai "+str(eta)+", anni "+"sei nato nel "+anno_nascita)
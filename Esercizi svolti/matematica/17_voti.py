voto = int(input("Inserisci il tuo voto (0-10): "))

if voto < 6:
    print("Insufficiente")
elif voto < 7:
    print("Sufficiente")
elif voto < 9:
    print("Buono")
else:
    print("Ottimo")

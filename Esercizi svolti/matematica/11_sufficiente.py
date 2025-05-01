voto = float(input("Inserisci il voto: "))
if 6 <= voto <= 10:
    print("Se hai preso "+str(voto)+" è sufficiente")
elif 0<= voto <6:
    print("Se hai preso "+str(voto)+" è insufficiente")
else:
    print("Il voto inserito non è valido")
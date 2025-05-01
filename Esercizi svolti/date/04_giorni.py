giorno = int(input("Inserisci un numero: "))
match giorno:
    case 1:
        print("Il numero "+str(giorno)+" corrisponde a lunedì")
    case 2:
        print("Il numero "+str(giorno)+" corrisponde a martedì")
    case 3:
        print("Il numero "+str(giorno)+" corrisponde a marcoledì")
    case 4:
        print("Il numero "+str(giorno)+" corrisponde a giovedì")
    case 5:
        print("Il numero "+str(giorno)+" corrisponde a venerdì")
    case 6:
        print("Il numero "+str(giorno)+" corrisponde a sabato")
    case 7:
        print("Il numero "+str(giorno)+" corrisponde a domenica")
    case _:
        print("Il numero "+str(giorno)+" non è valido")
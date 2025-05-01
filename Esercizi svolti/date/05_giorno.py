giorno = input("Inserisci un giorno della settimana: ").lower()

match giorno:
    case "lunedì":
        print("Oggi è giorno di allenamento.")
    case "martedì":
        print("Oggi è giorno di studio.")
    case "mercoledì":
        print("Oggi è giorno di riposo.")
    case "giovedì":
        print("Oggi è giorno di uscire con gli amici.")
    case "venerdì":
        print("Oggi è giorno di lavoro.")
    case "sabato":
        print("Oggi è giorno di fare shopping.")
    case "domenica":
        print("Oggi è giorno di famiglia.")
    case _:
        print("Giorno non riconosciuto.")

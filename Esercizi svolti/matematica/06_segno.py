num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))

if num1 >= 0:
    if num2 >= 0:
        print("Entrambi i numeri sono positivi.")
    else:
        print("I numeri sono di segno opposto.")
else:
    if num2 < 0:
        print("Entrambi i numeri sono negativi.")
    else:
        print("I numeri sono di segno opposto.")

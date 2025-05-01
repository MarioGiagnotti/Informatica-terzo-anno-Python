max_num = None

while True:
    num = int(input("Inserisci un numero (0 per terminare): "))
    if num == 0:
        break
    if max_num is None or num > max_num:
        max_num = num

print("Il numero massimo inserito è: ",max_num)

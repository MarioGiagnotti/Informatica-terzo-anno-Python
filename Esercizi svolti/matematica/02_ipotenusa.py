import math

cateto1 = float(input("Inserisci la lunghezza del primo cateto: "))
cateto2 = float(input("Inserisci la lunghezza del secondo cateto: "))

ipotenusa = math.sqrt(cateto1**2 + cateto2**2)
print("La lunghezza dell'ipotenusa è: ",ipotenusa)

angolo_rad = float(input("Inserisci un angolo in radianti: "))
angolo_gradi = math.degrees(angolo_rad)
print("L'angolo in gradi è: ",angolo_gradi)

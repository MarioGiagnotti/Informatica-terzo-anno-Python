import math

raggio = float(input("Inserisci il raggio"))
volume = (math.pi * math.pow(raggio,3))/math.sqrt(3)
print("Il volume del cono di raggio "+str(raggio)+" è: "+str(volume))
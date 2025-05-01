def exe01():
    '''
    Il modulo datetime contiene tre tipi principali di oggetti: data, ora e datetime
    '''
print(exe01.__doc__)

import datetime

from datetime import datetime
# generiamo un oggetto
# che contiene data e ora corrente
obj = datetime.now()

# generiamo una stringa
# che rappresenta l'orario corrente
orarioCorrente = obj.strftime("%H:%M:%S")
print("Sono le:", orarioCorrente)

# Estrazione della data corrente
data_corrente = obj.strftime("%d-%m-%Y")
# Stampa a video della data
print("Oggi è il:", data_corrente)


today = datetime.today()
print(today)
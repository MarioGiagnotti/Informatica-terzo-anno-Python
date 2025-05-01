def operatori():
    '''
    OPERATORI MATEMATICI
    1. DIVISIONE
    Python esegue la DIVISIONE reale tra gli operandi CON IL SIMBOLO /. 
    
    2. ADDIZIONE
    Python esegue la ADDIZIONE tra gli operandi CON IL SIMBOLO +. 
    
    3. SOTTRAZIONE
    Python esegue la SOTTRAZIONE tra gli operandi CON IL SIMBOLO -. 
    
    4. MOLTIPLICAZIONE
    Python esegue la MOLTIPLICAZIONE tra gli operandi CON IL SIMBOLO *.
    
    5. ESPONENZIALI
    Python esegue l'ELEVAMENTO A POTENZA CON IL SIMBOLO ** TRA BASE ED ESPONENTE
    in alternativa si può utilizzare la funzione built-in pow oppure 
    importare il modulo math e richiamare il metodo pow
    oppure importare il modulo operator e chiamare il metodo pow
    
    la funzione math.exp(x) esegue l'esponenziale di e^x
    
    6. TRIGONOMETRICHE
    Python esegue le funzioni trigonometriche attraverso i metodi della funzione math
    
    7. INPLACE
    Python esegue alcune operazioni matematiche in forma contratta:
    
    a+=1 coincide con a=a+1
    a*=3 coincide con a = a*3
    
    qui di seguito le possibili forme contratte:
    -= decrement the variable in place
    += increment the variable in place
    *= multiply the variable in place
    /= divide the variable in place
    //= floor divide the variable in place # Python 3
    %= return the modulus of the variable in place
    **= raise to a power in place
    
    8.LOGARITMI
    Per impostazione predefinita, la funzione math.log calcola il logaritmo di un numero, in base e. 
    Facoltativamente è possibile specificare una base come secondo argomento:
    
    import math
    math.log(5) # = 1.6094379124341003 # optional base argument. Default is math.e
    math.log(5, math.e) # = 1.6094379124341003
    math.log(1000, 10) # 3.0 (always returns float)

    9. MODULO
    La funzione modulo restituisce il resto intero di una divisione. L'operatore è %
    
    a=10
    b=3
    a%b restituisce 1
    
    import math
    math.log(5) # = 1.6094379124341003 # optional base argument. Default is math.e
    math.log(5, math.e) # = 1.6094379124341003
    math.log(1000, 10) # 3.0 (always returns float)

    '''
print(operatori.__doc__)

#DIVISIONE
a, b, c, d, e = 3, 2, 2.0, -3, 10
print(a/b)
print(a/c)
print(d/b)
print("{0:5.3f}".format(b/d))
print("{0:5.3f}".format(b/a))
print("{0:5.3f}".format(d/e))

#ADDIZIONE
print(a+b)
print(a+c)
print(d+b)
print("{0:5.3f}".format(b+d))
print("{0:5.3f}".format(b+a))
print("{0:5.3f}".format(d+e))

#SOTTRAZIONE
print(a-b)
print(a-c)
print(d-b)
print("{0:5.3f}".format(b-d))
print("{0:5.3f}".format(b-a))
print("{0:5.3f}".format(d-e))

#MOLTIPLICAZIONE
print(a*b)
print(a*c)
print(d*b)
print("{0:5.3f}".format(b*d))
print("{0:5.3f}".format(b*a))
print("{0:5.3f}".format(d*e))

#ESPONENZIALI
base = 2
esponente = 3
ris = base**esponente
print(ris)

ris = pow(base,esponente)
print(ris)

import math
ris = math.pow(base,esponente)
esp = math.exp(1)
print(ris)
print(esp)

import operator
ris = operator.pow(base,esponente)
print(ris)

#TRIGONOMETRICHE
A = math.pi
print(A)
B = 270
gradi_a = math.degrees(A)
print(gradi_a)
radianti_b = math.radians(B)

#INPLACE
a += 1
print(a)
a *= 2
print(a)

#LOGARITMI
import math

print(math.log(5))
print(math.log(5, math.e))
print((math.log(1000, 10)))

#MODULO
a=10
b=3
print(a%b)
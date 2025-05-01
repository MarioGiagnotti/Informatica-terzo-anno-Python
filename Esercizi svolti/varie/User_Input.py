def user_input():
    '''
    Per ottenere input dall'utente, utilizzare la funzione input (nota: in Python 2.x, la funzione si chiama invece raw_input)
    Tieni presente che l'input è sempre di tipo str, il che è importante se desideri che l'utente inserisca dei numeri. 
    Pertanto, è necessario convertire la str prima di provare a usarla come numero
    '''
                    
print(user_input.__doc__)

name = input("Qual è il tuo nome? ")
print("Ciao ",name)

x = input("Inseisci un numero:")
# casting da str a float
print("Il numero inseito è: ",float(x))

def moduli():
    ''' 
    Un modulo è un file contenente definizioni e istruzioni Python. La funzione è un pezzo di codice che esegue qualcosa.
    Per verificare la funzione incorporata in Python possiamo usare dir(). Se chiamato senza argomenti, restituisce i nomi nel file
    nell'attuale scope. Altrimenti, restituisce un elenco in ordine alfabetico di nomi che comprendono (alcuni degli) attributi dell'oggetto 
    dato e di attributi raggiungibili da esso
    per conoscere le funzionalità di un modulo si invoca la funzione help()
    per importare i moduli si utilizza import <nome_modulo>
    
    Un modulo è un file importabile contenente definizioni e istruzioni.
    Un modulo può essere creato creando un file .py.
    
    Le funzioni in un modulo possono essere utilizzate importando il modulo.
    I moduli che hai creato dovranno trovarsi nella stessa directory del file che li sta importando. 
    
    I moduli possono essere importati da altri moduli.
    # hello.py
    def say_hello():
        print("Hello!")
    
    #richiamare una funzione di un modulo in un altro modulo    
    import hello
    hello.say_hello()
    
    #oppure
    from hello import say_hello
    say_hello()
    
    #alias per hello.py
    import hello as hl
    hl.say_hello()
    
    #mandare in run un modulo
    if __name__ == '__main__':
        from hello import say_hello
        say_hello()

    
    È possibile importare funzioni specifiche di un modulo.
    I moduli possono essere alias.
    Un modulo può essere uno script eseguibile autonomo.
    
    I moduli esterni possono essere installati con la parola chiave pip:
    
    $ pip install [package_name] # latest version of the package
    $ pip install [package_name]==x.x.x # specific version of the package
    $ pip install '[package_name]>=x.x.x' # minimum version of the package
    
    Per aggiornare un modulo:
    In Linux o macOS X:
    $ pip install -U pip

    Su Windows:
    py -m pip install -U pip
    oppure
    python -m pip install -U pip
    
    '''
print(moduli.__doc__)

import math

print(dir(__builtins__))
help(max)
a=16
print(math.sqrt(a))



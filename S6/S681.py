import time

class Timer1:
    def __enter__(self):
        print("Entering Timer1")
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        print(f"Total duration {time.time()-self.start:2f}")
        return True
    
with Timer1():
    n = 0
    for i in range(2*10**6):
        n += i**2
        
with Timer1():
    n = 0
    for i in range(2*10**6):
        n += i**2 / 0

# une deuxième version de Timer
# qui propage correctement les exceptions

class Timer2:
    def __enter__(self):
        print("Entering Timer2")
        self.start = time.time()
        # rappel : le retour de __enter__ est ce qui est passé
        # à la clause `as` du `with`
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print(f"Total duration {time.time()-self.start:2f}")
            # ceci indique que tout s'est bien passé
            return True
        else:
            print(f"OOPS : on propage l'exception {exc_type} - {exc_value}")
            # c'est ici que je propage l'exception au dehors du with
            raise exc_type(exc_value)
        return True

try:
    with Timer2():
        n = 0
        for i in range(2*10**6):
            n += i**2 / 0
except Exception as e:
    print(f"L'exception a bien été propagée, {type(e)} - {e}")
    
print("***"*20)

class MyContext:
    def __enter__(self):
        print("in enter")
        return self

    def __exit__(self, *args):
        print("in exit")
        return True

with MyContext() as c:
    print("bloc with enter")
    raise Exception
    print("bloc with exit")
        
    
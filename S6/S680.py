import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        #print(f"{duree}")
        return self
    
    def __exit__(self, *args):
        duree = time.time() - self.start
        print(f"{duree}s")
        return False
    
    def __str__(self):
        duree = time.time() - self.start
        return f"intermediaire: {duree}s"
    
with Timer() as t:
    sum(x for x in range(10_000_000))
    print(t)
    sum(x**2 for x in range(10_000_000))
from itertools import permutations
set = {1, 2, 3}

for p in permutations(set):
    print(p)
    
class Aplatir:
    def __init__(self, my_iter):
        self.my_iter = my_iter

    def __iter__(self):
        for elem in self.my_iter:
            for e in elem:
                yield e

a = Aplatir(['on', [1, 2, 3], 'mer', (True, 4), 'va'])

print(iter(a))

print("".join(str(i) for i in a))
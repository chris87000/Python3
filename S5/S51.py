import itertools
import string

s = {1,2,3,'a'} 
print([x for x in s if type(x) is int])

it = iter(s)
next(it)
next(it)
next(it)
next(it)

a = [1,2]
b = [2,3]
z = zip(a,b)
print(z is iter(z))
print([i for i in z])


liste = [[1], [2], [3]]
print('avant', liste)
for sous_liste in liste:
    sous_liste.append(100)
print('après', liste)

for x in itertools.chain((1, 2), [3, 4]):
    print(x)
    

support = string.ascii_lowercase
print(f'support={support}')

for x in range(3, 8):
    print(x)
    
for x in itertools.islice(support, 0, 10):
    print(x)
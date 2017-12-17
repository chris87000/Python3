

carre = lambda x: x**2 -1

def image(f):
    for x in range(10):
        print(f" {f(x)}: {x}")
        
#image(lambda x: x**2 -1)

image(carre)

m = map(carre, range(10))
print(list(m))
      
print("***"*10)
f = filter(lambda x: x%2 == 0, range(10))
print(list(f))

print("***"*10)
# fonction lambda 
coordonnees = [(43, 7), (46, -7), (46, 0)]

def longitude(element): 
    return element[1]

coordonnees.sort(key=longitude)
print("coordonnées triées par longitude", coordonnees)


coordonnees.sort(key=lambda x: x[1])
print("coordonnées triées par longitude", coordonnees)

# méthode operator.getitem
import operator
coordonnees = [(43, 7), (46, -7), (46, 0)]
coordonnees.sort(key=operator.itemgetter(1))
print("coordonnées triées par longitude", coordonnees)

liste = [8, 7, 4, 3, 2, 9, 1, 5, 6]
# ce qu'on a fait dans la cellule précédente est équivalent à

print("***"*10)
triee = liste[:]
triee.sort(reverse=True)
# 
print('la liste triée est une copie ', triee)
print('la liste initiale est intacte', liste)
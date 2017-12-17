from functools import reduce

# la multiplication, mais sous forme de fonction et non d'opérateur
from operator import add

def factoriel(n):
    return reduce(add, range(1, n+1), 0)

#for i in range(5):
 #   print(f"{i} -> {factoriel(i)}")
    

coordonnees = [(43, 7), (46, -7), (46, 0)]
    
def longitude(element): 
    return element[0]

#coordonnees.sort(key=longitude)
#print("coordonnées triées par longitude", coordonnees)

# fonction lambda 
coordonnees = [(43, 7), (46, -7), (46, 0)]
coordonnees.sort(key=lambda x: x[1])
#print("coordonnées triées par longitude", coordonnees)

# méthode operator.getitem
import operator
coordonnees = [(43, 7), (46, -7), (46, 0)]
coordonnees.sort(key=operator.itemgetter(0))
#print("coordonnées triées par longitude", coordonnees)

liste = [8, 7, 4, 3, 2, 9, 1, 5, 6]
# on peut passer à sorted les mêmes arguments que pour sort
triee = sorted(liste, reverse=True)
# nous avons maintenant deux objets distincts
#print('la liste triée est une copie ', triee)
#print('la liste initiale est intacte', liste)

liste = [8, 7, 4, 3, 2, 9, 1, 5, 6]
# ce qu'on a fait dans la cellule précédente est équivalent à
triee = liste[:]
triee.sort(reverse=True)
# 
#print('la liste triée est une copie ', triee)
#print('la liste initiale est intacte', liste)



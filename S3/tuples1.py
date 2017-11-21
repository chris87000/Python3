# on fabrique une liste pas à pas
liste = list(range(10))
print(liste)
liste[9] = 'Inconnu'
del liste [2:5]
print(liste)

# on convertit le résultat en tuple
mon_tuple = tuple(liste)
print(mon_tuple)

print("*"*100)  
reference = [1, 2, 3, 4, 5]
print(type(reference))
a, *b, c = reference
print(f"a={a} b={b} c={c}")
mon_tuple= (1,2,3)
print(type(mon_tuple))
print("*"*100)  
reference = range(20)
a, *b, c = reference
print(f"a={a} b={b} c={c}")
print(type(b))

print("*"*100)  
# si on sait que data contient prenom, nom, et un nombre inconnu d'autres informations
data = [ 'Jean', 'Dupont', '061234567', '12', 'rue du chemin vert', '57000', 'METZ', ]
# on peut utiliser la variable _ qui véhicule l'idée qu'on ne s'y intéresse pas vraiment
prenom, nom, *_ = data
print(f"prenom={prenom} nom={nom}")
print(type(data))

print("*"*100)  
entree = [1, 2, 3]
_, milieu, _ = entree
print('milieu', milieu)
ignored, ignored, right = entree
print('right', right)

print("*"*100)  
structure = ['abc', [(1, 2), ([3], 4)], 5]
print(type(structure))

(a, (b, ((trois,), c)), d) = structure
print('trois', trois)
trois = structure[1][1][0][0]
print('trois', trois)

print("*"*100)  
# un exemple très alambiqué avec plusieurs variables *extended
tree = [1, 2, [(3, 33, 'three', 'thirty-three')], ( [4, 44, ('forty', 'forty-four')])]
print(type(tree))
*_,  ((_, *x3, _),), (*_, x4) = tree
print(f"x3={x3}, x4={x4}")





from collections import defaultdict

# on lit dans un fichier des couples (x, y)

tuples = [
    (1, 2),
    (2, 1),
    (1, 3),
    (2, 4),
]

# et on veut construire un dictionnaire
# x -> [ liste de tous les y connectés à x]
resultat = {}

for x, y in tuples:
    if x not in resultat:
        resultat[x] = []
    resultat[x].append(y)

for key, value in resultat.items():
    print(key, value)
print(resultat)

print("**"*20)
# on indique que les valeurs doivent être créés à la volée
# en utilisant la fonction list
resultat = defaultdict(list)
# du coup plus besoin de vérifier la présence de la clé
for x, y in tuples:
    resultat[x].append(y)    
for key, value in resultat.items():
    print(key, value) 
    
print("**"*20)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
print(type(s))
for k, v in s:
    d[k].append(v)
print(d.items())    

print("**"*20)
compteurs = defaultdict(int)
phrase = "une phrase dans laquelle on veut compter les caractères"
for c in phrase:
    compteurs[c] += 1  
print(sorted(compteurs.items()))

print("**"*20)
annuaire = dict([('marc', 35), ('alice', 30), ('eric', 38)])
print('avant', annuaire)
# ceci sera sans effet car eric est déjà présent
print('set_default eric', annuaire.setdefault('eric', 50))
# par contre ceci va insérer une entrée dans le dictionnaire
print('set_default inconnu', annuaire.setdefault('inconnu', 50))
# comme on le voit 
print('après', annuaire)

     

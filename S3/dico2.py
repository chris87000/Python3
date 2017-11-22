
from collections import OrderedDict

annuaire = dict([('marc', 35), ('alice', 30), ('eric', 38)])
print(annuaire)
annuaire = dict(marc=35, alice=30, eric=38)
print(annuaire)
print('la valeur pour marc est', annuaire['marc'])

print('valeur pour marc', annuaire.get('marc', 0))
print('valeur pour inconnu', annuaire.get('inconnu', 0))
print("**"*20)

annuaire['eric'] = 39
print(annuaire)
for nom, age in annuaire.items():
    print(f"{nom}, age {age}")
print("**"*20)    
for clé in annuaire.keys():
    print(clé)
print("**"*20)
for valeur in annuaire.values():
    print(valeur)
print(f"{len(annuaire)} entrées dans annuaire")

print("**"*20)
print(f"avant: {list(annuaire.items())}")
annuaire.update({'jean':25, 'eric':70})
print(f"apres: {list(annuaire.items())}")

print("**"*20)
d = {'c' : 3, 'b' : 1, 'a' : 2}
for k, v in d.items():
    print( k, v)

print("**"*20)
d = OrderedDict()
for i in ['a', 7, 3, 'x']: 
    d[i] = i
print(f"d: {d}")
for k, v in d.items():
    print('OrderedDict', k, v)
    



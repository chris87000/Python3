
#Type     Mutable ?
#int, float     immuable
#complex,bool     immuable
#str     immuable
#list     mutable
#dict     mutable
#set     mutable
#frozenset     immuable

personnes = [
   {'nom': 'pierre',  'age': 25, 'email': 'pierre@foo.com'},
   {'nom': 'paul',    'age': 18, 'email': 'paul@bar.com'},
   {'nom': 'jacques', 'age': 52, 'email': 'jacques@cool.com'},
]

print(personnes, "\n", type(personnes))
personnes[0]['age'] += 10
for personne in personnes:
    print(10*"=")
    print("--> dico: ", type(personne))
    print("--> item de dico", personne.items(), ", ", type(personne.items()))
    print("--> liste de couples cle/valeur",list(personne.items()), ", ", type(list(personne.items())))
    for info, valeur in list(personne.items()):
        print(f"{info} -> {valeur}")
#####
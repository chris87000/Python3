comprehension = [x**2 for x in range(100) if x%17 == 0] 
#print(comprehension)

generator = (x**2 for x in range(100) if x%17 == 0) 
#print(list(generator))

#for count, carre in enumerate(generator, 1):
#print(f'Contenu de generator après {count} itérations : {carre}')

generator = (x**2 for x in range(10**18) if x%17==0) 
# on va calculer tous les carrés de multiples de 17 
# plus petits que 10**10 et dont les 4 derniers chiffres sont 1316
recherche = set()
# le point important, c'est qu'on n'a pas besoin de 
# créer une liste de 10**18 éléments 
# qui serait beaucoup trop grosse pour la mettre dans la mémoire vive
# avec un générateur, on ne paie que ce qu'on utilise...
for x in generator:
    if x > 10**10:
        break
    elif str(x)[-4:] == '1316':
        recherche.add(x)
#print(recherche)

depart = (-5, -3, 0, 3, 5, 10)
arrivee2 = (x**2 for x in depart)
#print(list(arrivee2))

#for x, y in zip(depart, arrivee2):
    #print(f"x={x} => y={y}")
    
def produit_scalaire(X, Y): 
    return sum((x * y for x, y in zip(X, Y)))

print(list(zip(  range(3, 9),range(5, 11))))
print(produit_scalaire( (1, 2), (3, 4)))

    



    
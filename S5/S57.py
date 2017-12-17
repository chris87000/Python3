import matplotlib.pyplot as plt

depart = (-5, -3, 0, 3, 5, 10)
arrivee = [x**2 for x in depart]
#print(arrivee)

#plt.ion()
#plt.plot(depart, arrivee);
#plt.show()

d = {x: ord(x) for x in 'abc'}
#print(d)

e = {x**2 for x in (6,8,9,97, 98, 99) if x %2 == 0}
#print(e)

#print([n + p for n in [2, 4] for p in [10, 20, 30]])
#print([n + p for n in [2, 4] for p in [10, 20, 30] if n*p >= 40])
#print([[n + p for n in [2, 4]] for p in [10, 20, 30]])

resultat = []
for n in [2, 4]:
    for p in [10, 20, 30]:
        if n*p >= 40:
            resultat.append(n + p)
#print(resultat)

n=4
#print([[(i, j) for i in range(1, j + 1)] for j in range(1, n + 1)])

resultat_exterieur = []
for j in range(1, n + 1):
    resultat_interieur = []
    for i in range(1, j + 1):
        resultat_interieur.append((i, j))
    resultat_exterieur.append(resultat_interieur)
#print(resultat_exterieur)

print([[(i, j) for i in range(1, j + 1) if (i + j)%2 == 0]  for j in range(1, n + 1) if j % 2 == 0])

#print([(x, y) for x in [1, 2] for y in [1, 2]])

#print([ (i, j) for i in range(1, j + 1) for j in range(1, n + 1) ])

resultat = []
for i in range(1, j + 1):
    for j in range(1, n + 1):
        resultat.append((i, j))
print(resultat)





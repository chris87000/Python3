item = (1, 2)
a, b = item
print(f"a={a} b={b}")

print("*"*100)  
entrees = [(1, 2), (3, 4), (5, 6)]
for a, b in entrees:
    print(f"a={a} b={b}")
    
villes = ["Paris", "Nice", "Lyon"]
populations = [2*10**6, 4*10**5, 10**6] 

print("*"*100)  
list(zip(villes, populations))
print(type(villes))
print(type(populations))
print("*"*100)  
for ville, population in zip(villes, populations):
    print(population, "habitants à", ville)
    
print("*"*100)  
# on n'itère que deux fois 
# car le premier argument de zip est de taille 2
for units, tens in zip( [1, 2, 'a'], [10, 20, 30, 40]):
    print(units, tens)

print("*"*100)  
for i, ville in enumerate(villes):
    print(i, ville)
print("*"*100) 
for i in range(len(villes)):
    print(i, villes[i])
print("*"*100) 
for i, ville in zip(range(len(villes)), villes):
    print(i, ville)

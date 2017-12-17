
import collections

def aplatir(conteneurs):
    tab = []
    for conteneur in conteneurs:
       if isinstance(conteneur, collections.Iterable):
           for cont in conteneur:
               tab.append(cont)
       else:
            tab.append(conteneur)
    return tab

#print(aplatir([(1,)]))

#print(aplatir(([1],)) )

#print(aplatir([ (0, 6, 2),[1, ('a', 4), 5]]))

def aplatir2(conteneurs):
    return [cont  for conteneur in conteneurs if  isinstance(conteneur, collections.Iterable) for cont in conteneur ]

#print(aplatir2([ (0, 6, 2),[1, ('a', 4), 5]]))
#print(aplatir2([(1,)]))    
#print(aplatir( ( (1, [2, 3]), [], 'a',['b', 'c'])))
#print(aplatir2([ (0, 6, 2),[1, ('a', 4), 5]]))

def alternat(c1, c2):
    tabzips= list(zip (c1,c2))
    return [z  for tabzip in tabzips if  isinstance(tabzip, collections.Iterable) for z in tabzip] 

#print(alternat( (1, 2),  ('a', 'b')))
#print(alternat((1, 2, 3),('a', 'b', 'c')))

def intersect(A, B):
    tab = []
    for a in A:
        ax, ay = a
        for b in B:
            bx,by = b
            if bx == ax:
               tab.append(by)
               tab.append(ay)
        
    return set(tab)

    
   #return set([ (ay, by) for a in A for b in B  ax,ay= a bx,by=b  ])

print(
  { (8, 'huit'),
    (10, 'dixA'),
    (12, 'douze')},
  { (5, 'cinq'),
    (10, 'dixB'),
    (15, 'quinze')})   

print(intersect2(
  { (8, 'huit'),
    (10, 'dixA'),
    (12, 'douze')},
  { (5, 'cinq'),
    (10, 'dixB'),
    (15, 'quinze')})   )


from audioop import reverse
tab = [ [40, 12, 25],  [ 'spam', 'egg', 'bacon']]

def getKey(item):
    return item[0]

def multi_tri(listes): 
    return [liste.sort() for liste in listes]

def multi_tri2(listes): 
    for liste in listes:
        liste.sort()
    return listes

def multi_tri_reverse(listes, reverses):
    i = 0
    for liste in listes:
        liste.sort(reverse=reverses[i])
        i = i + 1
    return listes
#tab.sort(key=lambda x: x[1])

#print(multi_tri(tab))

print(multi_tri_reverse(
  [[1, 2], [3, 4]],
  [True, False]))
    
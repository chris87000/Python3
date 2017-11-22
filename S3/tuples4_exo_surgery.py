

def surgery(liste):
    length = len(liste)
    if length ==0 or length == 1:
        return liste
    elif length %2 == 0:
        liste[0], liste[1] = liste[1], liste[0]
        return liste
    elif length %2 > 0 :
        liste[length-2], liste[length-1] = liste[length-1], liste[length-2]
        return liste
    else:
         return
        

print(surgery([]))

print(surgery([0]))

print(surgery([0,1]))    

print(surgery([0, 1, 2]))    

print(surgery([0, 1, 2, 3]))    



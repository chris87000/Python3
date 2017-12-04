"""
 S4 - Exercice - niveau basique
 
"""

def dispatch1(a, b):
    "renvoie une valeur dans les cas a,b pairs/impairs"
    if (a%2==0) and (b%2==0):
        return a*a+b*b
    elif  (a%2==1) and (b%2==0):
        return (a-1)*b
    elif (a%2==0) and (b%2==1):
        return a*(b-1)
    else:
        return a*a - b*b
    
    
def dispatch2(a, b, A, B):
    if (a in A) and (b in B):
         return a*a+b*b
    elif (a not in A) and (b in B):
         return (a-1)*b
    elif (a in A) and (b not in B):
         return a*(b-1)
    else:
         return a*a + b*b
      
import string
# coding: utf-8

def laccess(liste):
    l = len(liste)
    if l==0:
        return
    elif l>0 and l%2==0:
        return liste[l-1]
    else:
        return liste[int(l/2)]
    return 

print(laccess([]))
print(laccess([1]))
print(laccess(['spam', 2]))
print(laccess(['spam', 2, 'bacon']))
print(laccess([1, 2, 3, 4]))
print(laccess([1, 2, 3, 4, 5]))

print("**"*50)
def divisible(a, b):
    if a%b==0 or b%a==0:
        return True
    else:
        return False
    
def morceaux(x):
    if x <= -5:
        return x * (-1) -5
    elif x > -5 and x < 5:
        return 0
    else:
        return x /5 -1
    return       
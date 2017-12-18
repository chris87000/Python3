import spam
from spam import beans

egg = 2

def f():
    return spam.egg(), spam.spam, egg

#print(f())



def g(L):
    L.append(spam.beans)
    L.append(beans)
    spam.beans = 2
    L.append(spam.beans)
    L.append(beans)
    L.append(spam.f())
    return L

print(g([]))
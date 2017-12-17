
import operator
import math

def doubler_premier(fonction, arg1, arg2):
    x = fonction(2*arg1,arg2)
    return x

#print(doubler_premier(operator.add,1,4))


def add3(x, y=0, z=0):
    return x + y + z

def mul3(x=1, y=1, z=1):
    return x * y * z

#def doubler_premier_kwds(fct,*args):
#    return fct(2*args[0],args)

def doubler_premier_kwds(fct,x=0, y=0, z=0):
    print(fct, " ", x, ", ", y, ", ", z)
    return fct(x*2, y,z)  

#print(doubler_premier_kwds(add3,1,2,3))

def compare_all(f, g, entrees):
    x =[]
    for entree in entrees:
        #print(entree)
        x.append(f(entree) == g(entree))
    return x

#print(compare_all(math.factorial,math.factorial, [1,2,3]))
def compare_all2(f, g, entrees):
    #r = filter(lambda x: f(x) == g(x), entrees)
    cmp = lambda x: f(x) == g(x)
    r = map(cmp,entrees)
    return list(r)

def compare_args(f, g, entrees):
    tab =[]
    for entree in entrees:
        if len(entree) > 1:
            X, Y = entree
            print(X, ", ",Y)
            tab.append(f(X,Y) == g(X,Y))
        else:
            X = entree[0]
            print(X)
            tab.append(f(X) == g(X))
    return tab

print(compare_args(math.factorial,math.factorial, [(2,), (0, ), (4, )]   ))

print(compare_args(operator.add,operator.add, [(2,3), (0, 4), (4, 1)]   ))

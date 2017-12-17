from builtins import isinstance
carre = [x**2 for x in range(1000)]
print(carre)
print(sum(carre))
carre = (x**2 for x in range(1000))
print(carre)
print(sum(carre))
print("*************"*5)

gen_carre= ( x**2 for x in range(1000))

palin = (x for x in gen_carre if str(x) == str(x)[::-1])
print(list(palin))

print("%%%%%%%%%%%%%%%%%"*5)

def gen(x):
    yield 10
    x = x + 1
    yield x
g = gen(10)
#print(next(g))
#print(next(g))
#print(next(g))


print("%%%%%%%%%%%%%%%%%"*5)
def carre(a , b):
    for i in range(a, b):
        yield i**2
c = carre(1,10)
#print(list(c))

def palin(it):
    for i in it:
        if isinstance(i,(str,int)) and str(i) == str(i)[::-1]:
            yield i
p = palin([121,10,12321,'abc', 'abba'])
print(list(p))
print(list(palin((x**2 for x in range(1000)))))
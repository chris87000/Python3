from math import sqrt
def f(*args):
    print(args)
L = [1, 2, 'a']

#f(1, 2) 
#f('a', 4, 5, 6, 7, [1,2]) 
#f(*L) 

def distance(*args):
    result = 0
    for arg in args:
        result = result + arg*arg
    return sqrt(result)


def numbers(*args):
    sum = 0
    if args:
        tab = list(args)
        tab.sort(reverse=True)
        min = tab[-1]
        max = tab[0]
        for arg in args:
            sum = sum +arg
        return (sum, min, max)
    else:
        return (0,0,0)
    return

print (numbers(45,78,8,54,89,78))
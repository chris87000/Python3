def my_add(a,b):
    print(f"{a} plus {b}")
    return a+b


print (my_add(1.6, 3.56))

print (my_add('toto', ' est bo'))


def increment(n):
    print(id(n))
    n += 1
    print('-->n', n)

compteur = 10
print(id(compteur))
increment(compteur)
print(compteur)

def flatten(containers):
    "returns a list of the elements of the elements in containers"
    return [element for container in containers for element in container]

help(flatten)

# un style de docstring multi-lignes
def flatten(containers):
    """
provided that containers is a list (or more generally an iterable)
of elements that are themselves iterables, this function
returns a list of the items in these elements
    """
    return [element for container in containers for element in container]

help(flatten)
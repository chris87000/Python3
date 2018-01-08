class Foo: 
    def __repr__(self):
        return 'custom repr'
    
foo = Foo()
# lorsque vous affichez un objet comme ceci
print(foo)
# en fait vous utilisez repr()

# une classe qui ne définit que __repr__
class Point:
    "première version de Point - on ne définit que __repr__"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x},{self.y})"
    
point = Point (0,100)

print("avec print", point)

# si vous affichez un objet sans passer par print
# vous utilisez repr()
repr(point)

# la même chose mais où on redéfinit __str__ et __repr__
class Point2:
    "seconde version de Point - on définit __repr__ et __str__"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point2({self.x},{self.y})"
    def __str__(self):
        return f"(str: {self.x},{self.y})"
    
point2 = Point2 (0,100)

print("avec print", point2)

# les f-strings (ou format) utilisent aussi __str__
print(f"avec format {point2}")

# et si enfin vous affichez un objet sans passer par print
# vous utilisez repr()
print(point2)

# notre classe Matrix2 avec encore une autre implémentation
class Matrix2:

    def __init__(self, *args):
        """
        le constructeur accepte 
        (*) soit les 4 coefficients individuellement
        (*) soit une liste - ou + généralement une séquence - des mêmes
        """
        # on veut pouvoir créer l'objet à partir des 4 coefficients
        # souvenez-vous qu'avec la forme *args, args est toujours un tuple
        if len(args) == 4:
            self.coefs = args
        # ou bien d'une séquence de 4 coefficients
        elif len(args) == 1:
            self.coefs = tuple(*args)

    def __repr__(self):
        "l'affichage"
        return "[" + ", ".join([str(c) for c in self.coefs]) + "]"

    def __add__(self, other):
        """
        l'addition de deux matrices retourne un nouvel objet
        la possibilité de créer une matrice à partir
        d'une liste rend ce code beaucoup plus facile a écrire
        """
        return Matrix2([a + b for a, b in zip(self.coefs, other.coefs)])

    def __bool__(self):
        """
        on considère que la matrice est non nulle 
        si un au moins de ses coefficients est non nul
        """
        # ATTENTION le retour doit être un booléen 
        # ou à la rigueur 0 ou 1
        for c in self.coefs:
            if c:
                return True
        return False
    
print("***********"*10)
    
zero     = Matrix2 ([0,0,0,0])

matrice1 = Matrix2 (1,2,3,4)
matrice2 = Matrix2 (list(range(10,50,10)))

print('avant matrice1', matrice1)
print('avant matrice2', matrice2)

print('somme', matrice1 + matrice2)

print('après matrice1', matrice1)
print('après matrice2', matrice2)

if matrice1: 
    print(matrice1,"n'est pas nulle")
if not zero: 
    print(zero,"est nulle")
    
print(sum([matrice1, matrice2, matrice1] , zero))

print("***********"*10)

# remarquez que les opérandes sont apparemment inversés
# dans le sens où pour evaluer 
#     reel * matrice
# on écrit une méthode qui prend en argument
#   la matrice, puis le réel
# mais n'oubliez pas qu'on est en fait en train
# d'écrire une méthode sur la classe `Matrix2`
def multiplication_scalaire(self, alpha):
    return Matrix2([alpha * coef for coef in self.coefs])

# on ajoute la méthode spéciale __rmul__
Matrix2.__rmul__ = multiplication_scalaire
    
print(matrice1)
print(10 * matrice1)
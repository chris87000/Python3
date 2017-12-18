class Matrix2:
    "Une implémentation sommaire de matrice carrée 2x2"

    def __init__(self, a11, a12, a21, a22):
        "construit une matrice à partir des 4 coefficients"
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22
        
    def determinant(self):
        "renvoie le déterminant de la matrice"
        return self.a11 * self.a22 - self.a12 * self.a21
    
#print(help(Matrix2))

matrice = Matrix2(1, 2, 2, 1)
print(matrice)

class Matrix22:
    """Une deuxième implémentation, tout aussi
    sommaire, mais différente, de matrice carrée 2x2"""
    
    def __init__(self, a11, a12, a21, a22):
        "construit une matrice à partir des 4 coefficients"
        # on décide d'utiliser un tuple plutôt que de ranger
        # les coefficients individuellement
        self.a = (a11, a12, a21, a22)
        
    def determinant(self):
        "le déterminant de la matrice"
        return self.a[0] * self.a[3] - self.a[1] * self.a[2]
    
    def __repr__(self):
        "comment présenter une matrice dans un print()"
        return f"<<mat-2x2 {self.a}>>"

matrice = Matrix22(1, 2, 2, 1)
print("Determinant =", matrice.determinant())
print(matrice)

composite = [matrice, None, Matrix22(1, 0, 0, 1)]
print(f"composite={composite}")


class Personne:
    """Une personne possède un nom, un âge et une adresse e-mail"""
    
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email
        
    def __repr__(self):
        # comme nous avons la chance de disposer de python-3.6
        # utilisons un f-string
        return f"<<{self.nom}, {self.age} ans, email:{self.email}>>"
    

personnes = [

    # on se fie à l'ordre des arguments dans le créateur
    Personne('pierre', 25, 'pierre@foo.com'),

    # ou bien on peut être explicite
    Personne(nom='paul', age=18, email='paul@bar.com'),

    # ou bien on mélange
    Personne('jacques', 52, email='jacques@cool.com'),
]
for personne in personnes:
    print(personne)
print("*************"*10)   
index_par_nom = {personne.nom: personne for personne in personnes}
pierre = index_par_nom['pierre']
print(pierre)

pierre.age += 1
print(pierre)

# pour une implémentation réelle voyez la bibliothèque smtplib
# https://docs.python.org/3/library/smtplib.html

def sendmail(self, subject, body):
    "Envoie un mail à la personne"
    print(f"To: {self.email}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    
Personne.sendmail = sendmail

print(help(Personne))
print(pierre.sendmail("Coucou", "Salut ça va ?"))



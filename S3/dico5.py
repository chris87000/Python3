class Personne:

    # le constructeur - vous ignorez le paramètre self,
    # on pourra construire une personne à partir de 
    # 3 paramètres
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email
        
    # je définis cette méthode pour avoir
    # quelque chose de lisible quand je print()
    def __repr__(self):
        return f"{self.nom} ({self.age} ans) sur {self.email}"
    
personnes2 = [
    Personne('pierre', 25, 'pierre@foo.com'),
    Personne('paul', 18, 'paul@bar.com'),
    Personne('jacques', 52, 'jacques@cool.com'),
] 
print(personnes2[0])
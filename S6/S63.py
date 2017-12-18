class Temperature1:
    def __init__(self, kelvin):
        self.kelvin = kelvin
        
    def __repr__(self):
        return f"{self.kelvin}°K"

t1 = Temperature1(20)
print(t1)
print(t1.kelvin)

class Temperature2:
    def __init__(self, kelvin):
        # au lieu d'écrire l'attribut il est plus sûr
        # d'utiliser le setter
        self.set_kelvin(kelvin)
        
    def set_kelvin(self, kelvin):
        # je m'assure que _kelvin est toujours positif
        # et j'utilise un nom d'attribut avec un _ pour signifier
        # que l'attribut est privé et qu'il ne faut pas y toucher directement
        # on pourrait aussi bien sûr lever une exception 
        # mais ce n'est pas mon sujet ici
        self._kelvin = max(0, kelvin)
        
    def get_kelvin(self):
        return self._kelvin
        
    def __repr__(self):
        return f"{self._kelvin}°K"

class Temperature3:
    def __init__(self, kelvin):
        self.kelvin = kelvin

    # je définis bel et bien mes accesseurs de type getter et setter
    # mais _get_kelvin commence avec un _ 
    # car il n'est pas censé être appelé par l'extérieur
    def _get_kelvin(self):
        return self._kelvin

    # idem
    def _set_kelvin(self, kelvin):
        self._kelvin = max(0, kelvin)
        
    # une fois que j'ai ces deux éléments je peux créer une property
    kelvin = property(_get_kelvin, _set_kelvin)
    
    # et toujours la façon d'imprimer
    def __repr__(self):
        return f"{self._kelvin}°K"   
t3 = Temperature3(200)
print(t3)    



class Temperature:

    ## les constantes de conversion
    # kelvin / celsius
    K = 273.16
    # fahrenheit / celsius
    RF = 5 / 9
    KF = (K / RF) - 32

    def __init__(self, kelvin=None, celsius=None, fahrenheit=None):
        """
        Création à partir de n'importe quelle unité
        Il faut préciser exactement une des trois unités
        """
        # on passe par les properties pour initialiser
        if kelvin is not None:
            self.kelvin = kelvin
        elif celsius is not None:
            self.celsius = celsius
        elif fahrenheit is not None:
            self.fahrenheit = fahrenheit
        else:
            self.kelvin = 0
            raise ValueError("need to specify at least one unit")

    # pour le confort
    def __repr__(self):
        return f"<{self.kelvin:g}°K == {self.celsius:g}℃ " \
               f"== {self.fahrenheit:g}℉>"

    def __str__(self):
        return f"{self.kelvin:g}°K"
# l'attribut 'kelvin' n'a pas de conversion à faire,
    # mais il vérifie que la valeur est positive
    def get_kelvin(self):
        return self._kelvin

    def set_kelvin(self, kelvin):
        if kelvin < 0:
            raise ValueError(f"Kelvin {kelvin} must be positive")
        self._kelvin = kelvin

    # la property qui définit l'attribut `kelvin`
    kelvin = property(get_kelvin, set_kelvin)


    # les deux autres properties font la conversion, puis 
    # sous-traitent à la property kelvin pour le contrôle de borne
    def set_celsius(self, celsius):
        # using .kelvin instead of ._kelvin to enforce
        self.kelvin = celsius + self.K

    def get_celsius(self):
        return self._kelvin - self.K
    
    celsius = property(get_celsius, set_celsius)

    def set_fahrenheit(self, fahrenheit):
        # using .kelvin instead of ._kelvin to enforce
        self.kelvin = (fahrenheit + self.KF) * self.RF

    def get_fahrenheit(self):
        return self._kelvin / self.RF - self.KF
    
    fahrenheit = property(get_fahrenheit, set_fahrenheit)
    
    
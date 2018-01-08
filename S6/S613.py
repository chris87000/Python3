from enum import Enum

class Flavour(Enum):
    CHOCOLATE = 1
    VANILLA = 2
    PEAR = 3
   
vanilla = Flavour.VANILLA 
print(str(vanilla))
print(repr(vanilla))

chocolate = Flavour['CHOCOLATE']
print(chocolate)
print(chocolate.name)


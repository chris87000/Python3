
class Phrase:
    
    def __init__(self, ma_phrase):
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()
        
    def nb_lettre(selfself):
        return len(self.ma_phrase)

    def __len__(self):
        return len(self.mots)
    
    def __contains__(self, mot):
        return mot in self.mots
        
    def __str__(self):
        return " ||  ".join(self.mots)
    
     
p = Phrase("Hi you!")

#print(p.ma_phrase)
#print(len(p))
#print('Hi' in p)
#print(p)

class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Pt[{self.x}, {self.y}]"
    
    def __str__(self):
        return f" ({self.x}), ({self.y})"
    
# deux instances 
p1 = Point1(2, 3)
p2 = Point1(3, 4)
p3 = Point1(15,22)

# bien qu'ils soient mutables, on peut les mettre dans un ensemble
s = {p1, p2, p3}
print(p1)
print(s)

s="Je fais un MOOC sur Python"

class IterPhrase:
    def __init__(self,mots):
        self.mots = mots[:]
      
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.mots:
            raise StopIteration
        return self.mots.pop(0)
    
class Phrase:
    def __init__(self, ma_phrase):
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()
        
    def __iter__(self):
        return IterPhrase(self.mots)
  
  
p = Phrase(s)
print( [m for m in p])

print( [m for m in p])
print("*************"*10)
class Phrase2:
    def __init__(self, ma_phrase):
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()
        
    def __iter__(self):
        for m in self.mots:
            yield m
            
p = Phrase2(s)
print( [m for m in p])
print( [m for m in p])
                
    
    

s = "Je fais un MOOC sur Python"

class Phrase:
    
    def __init__(self, ma_phrase):
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()
        
    def nb_lettre(self):
        return len(self.ma_phrase)

    def __len__(self):
        return len(self.mots)
    
    def __contains__(self, mot):
        return mot in self.mots
        
    def __str__(self):
        return " ||  ".join(self.mots)
    
     

class PhraseSansCasse(Phrase):
    def __init__(self, ma_phrase):
        Phrase.__init__(self, ma_phrase)
        self.mots_lower = {m.lower() for m in self.mots}

    def __contains__(self,mot):
        return mot.lower() in self.mots_lower 
        
p_no = PhraseSansCasse(s)
print(p_no)

print('Mooc'  in p_no)

p = Phrase(s)
p_no = PhraseSansCasse(s)
print('mooc' in p," ",  'mooc' in p_no, ", ",p.nb_lettre(),  ", " ,p_no.nb_lettre())

s  = "je m'appelle toto et je suis bô!!!"
class Phrase:
    
    def initia(self, ma_phrase):
        self.ma_phrase = ma_phrase
    ma_phrase = "je m'appelle toto et je suis bô!"
    mots = ma_phrase.split()
    
p = Phrase()
print(p)

print(Phrase.__dict__)
print(vars(Phrase))
print(vars(p))

print(p.ma_phrase)
print(p.mots)

m = Phrase()
m.initia(s)
print(vars(m))
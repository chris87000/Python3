class Phrase:
    def __init__(self, ma_phrase):
        self.ma_phrase = ma_phrase
        if not ma_phrase:
            raise PhraseVideError('alerte phrase vide!', 22)
        self.mots=ma_phrase.split()

class PhraseVideError(Exception):
    pass

try:
    Phrase('')
except PhraseVideError as e:
    print("Erreur: ", e.args)
    
class MyError(Exception):
    pass

try:
    raise MyError("une exception personalisée", 100)
except MyError as e:
    print(e.args)
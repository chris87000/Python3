import string
# coding: utf-8

def label(prenom, note):
    if  note < 10:
        print("{} est recalé".format(prenom))
    elif (note >=10 and note <= 16):
        print("{} est reçu".format(prenom))
    elif note > 16:
        print("félicitations à {}".format(prenom))
        
label('toto', 20)
label('titi', 10)
label('tutu', 17)
label('tete', 8)


chaine = string.ascii_lowercase
print(chaine)
ret = chaine[-5:-2] == "vwx"
print(chaine[3:26] )
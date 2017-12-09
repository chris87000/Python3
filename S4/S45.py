import re

data = ['Joseph, Dupont, 4', 'Jean', 'Jules , Durand, 1', ' Ted, Mosby, 2,' , ' Jacques , Martin, 3 \t', 'Sheldon, Cooper ,5, ', '\t John, Doe\t, ' ,  'John, Smith, , , , 3' ]

def libelle(ligne):
     ligne_splitted = ligne.split(',')
     #print("splitted: ", ligne_splitted)
     tab = []
     taille = len(ligne_splitted)
     if taille >=3 and taille < 4 :
         if ligne_splitted[0] :
             tab.append(ligne_splitted[0].strip())
         if ligne_splitted[1]:
             tab.append(".")
             tab.append(ligne_splitted[1].strip())
         if ligne_splitted[2]:
             second = ligne_splitted[2]
             if len(second) > 0:
                 if second.strip() =='1':
                     tab.append(" (")
                     tab.append(second.strip())
                     tab.append("er)")
                 else:
                     tab.append(" (")
                     tab.append(second.strip())
                     tab.append("-ème)")
         else:
            return
     else:
         #print("Ne convient pas: " , ligne)
         return   
     tab[0], tab[2] = tab[2], tab[0] 
     return "".join(tab)


for stringue in data:
     s =libelle(stringue)
     print("Result: ", s)
     print("**"*10)
         
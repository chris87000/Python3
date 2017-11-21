import re
# coding: utf-8

tabs = ['Daniel:Durand', 'Jean:Dupont:'	, 'Jean:Dûpont::', ':Dupöntel:'	, 'Jean-Noël:Dupont-Nemours', 'Charles-Henri:Du Pré', 'Charles Henri:DuPré']

#regex = r"^[\w]?[-]?[\w]?[:]{1}[\w]{1}[-]?[\w]?[:]?$"
#regex = r"^[\w\S]*[-]*[\w\S]*[:][\w\S]*[-]*[\w\S]*[:]?$"

#valid = re.compile(regex, re.VERBOSE)

#regex = "(?P<prenom>[\w\S]*[-]*[\w\S]*)[:]{1}(?P<nom>[\w\S]*[-]*[\w\S]*)[:]?"
#regex = "(?P<prenom>[\w\S-]+?)[:]{1}(?P<nom>[\w\S]*?[-]*?[\w\S]*?)[:]??"
regex = "(?P<prenom>[\w-]*)[:]{1}(?P<nom>[\w-]+)[:]?\Z"

pattern = re.compile(regex)

#print(valid)
                   

for tab in tabs:
        rez = pattern.search(tab)
        if rez:
                print(rez.groupdict())
        else:
                print("None")
                
        #cp = re.search(regex,tab).group('prenom')
        #cn = re.search(regex,tab).group('nom')
        #print(f"-->{tab:>25s}  :  {cp}  |  {cn}")
        #  print('--> {} :  {}'.format(tab,corresp ))     

 


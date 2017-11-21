import re

tab = ['a', '_','__','-','aa1','A1a','1Aa','-aa1','_aa1','a-a1','a_a1','aa-1','aa_1','-A1a','_A1a','A-1a','A_1a','A1-a','A1_a','-1Aa','_1Aa','1-Aa','1_Aa','1A-a','1A_a']
attendu =['True','True','True','False','True','True','False','False','True','False','True','False','True','False','True','False','True','False','True','False','True','False','False','False','False']
regex = r"^[^\-0-9][^\-]*$"

j=0
for i in tab:
    valid = re.compile(regex)
    ch=""
    resultat=""
    if valid.match(i) is None:
        ch = "False"
        if ch==attendu[j]:
            resultat="OK"
        else:
            resultat="KO"
        print("Pour '{}' attendu: '{}'    obtenue: '{}'   {}".format(i,attendu[j],ch, resultat))
    else:
        ch = "True"
        if ch==attendu[j]:
            resultat="OK"
        else:
            resultat="KO"        
        print("Pour '{}' attendu: '{}'    obtenue: '{}'  {}".format(i,attendu[j],ch, resultat))
    j+=1
    
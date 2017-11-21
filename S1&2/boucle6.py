import re

#def clean(str):
def carre(ligne):
    sep=":"
    ret=[]
    regex = r"[-]?[\d]+"
    pattern = re.compile(regex)
    matches = pattern.findall(ligne)
    print(matches)
    for match in matches:
        carre = str(int(match) * int(match)) 
        ret.append(carre)
    return sep.join(ret)

datas = ['1;2;3',  '2 ; 5;6;', '; 12 ; -23;\t60; 1\t', '; -12 ; ; -23; 1 ;;\t']
print(type(datas))
for i in datas:
    print(carre(i))
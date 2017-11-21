import locale
# coding: utf-8

nf = "nomsdelangages.txt"
with open(nf, 'r') as f:
    L = []
    for ligne in f:
        langage = ligne.split()[0].rstrip(',')
        if langage not in L:
            L.append(langage)
# sauvegarde de la locale courante
lcl = locale.getlocale()

# sélection des langages disponible sur l'OS:
LW = []
for loc in L:
    try:
        locale.setlocale(locale.LC_ALL, loc)
        enc = locale.normalize(loc).split('.')
        if len(enc)!=2:
            continue
        LW.append([loc, enc[0], enc[1]])
    except:
        pass

# restauration de la locale initiale
locale.setlocale(locale.LC_ALL, lcl)
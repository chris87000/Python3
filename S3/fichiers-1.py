
with open(r"c:\temp\foo.txt", "w", encoding='utf-8') as sortie:
    for i in range(2):
        sortie.write(f"{i}\n")
        
with open(r"c:\temp\foo.txt", "a", encoding='utf-8') as sortie:
    for i in range(100, 102):
        sortie.write(f"{i}\n")
        
with open(r"c:\temp\foo.txt", encoding='utf-8') as entree: # remarquez que sans 'mode', on ouvre en lecture seule
    for line in entree:
        # line contient déjà un newline
        print(line, end='')
        
# Si on essaie d'écrire deux boucles imbriquées
# sur le même objet fichier, le résultat est inattendu
with open(r"c:\temp\foo.txt", encoding='utf-8') as entree:
    for l1 in entree:
        # on enleve les fins de ligne
        l1 = l1.strip()
        print("->{}".format(l1))
        for l2 in entree:
            # on enleve les fins de ligne
            l2 = l2.strip()
            print(l1, "x", l2)
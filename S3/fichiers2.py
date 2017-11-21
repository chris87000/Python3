

with open(r"c:\temp\foo.txt", encoding='utf-8') as entree:
    full_contents = entree.read()
    print(f"Contenu complet\n{full_contents}", end="")
    
print("*"*100)
# lire dans le fichier deux blocs de 4 caractères
with open(r"c:\temp\foo.txt", encoding='utf-8') as entree:
    for bloc in range(2):
        print(f"Bloc {bloc} >>{repr(entree.read(4))}<<")

print("*"*100)        
with open(r"c:\temp\foo.txt", encoding='utf-8') as input:
    for line in input:
        print("on a lu un objet de type", type(line))

        
print("*"*100)   
with open('strbytes', 'w', encoding='utf-8') as output:
    output.write("déjà l'été\n")
    # phase 2: on rouvre le fichier en mode binaire
with open('strbytes', 'rb') as rawinput:
    # on relit tout le contenu
    octets = rawinput.read()
    # qui est de type bytes
    print("on a lu un objet de type", type(octets))
    # si on regarde chaque octet un par un
    for i, octet in enumerate(octets):
        print(f"{i} → {repr(chr(octet))} [{hex(octet)}]")

print("*"*100)  
# on peut comparer le nombre d'octets et le nombre de caractères
with open('strbytes', encoding='utf-8') as textfile:
    print(f"en mode texte, {len(textfile.read())} caractères")
with open('strbytes', 'rb') as binfile:
    print(f"en mode binaire, {len(binfile.read())} octets")
from pathlib import Path
from pathlib import PurePosixPath

# le nom de notre fichier jouet 
nom = 'fichier-temoin'
# on crée un objet de la classe Path, associé au nom de fichier
path = Path(nom)
print(path)
# si j'écris dedans je le crée
with open(nom, 'w', encoding='utf-8') as output:
    output.write('0123456789\n')
print(path.stat())

mtime = path.stat().st_mtime
from datetime import datetime
mtime_datetime = datetime.fromtimestamp(mtime)
print(mtime_datetime)
print(f"{mtime_datetime:%H:%M}")

# ou encore mieux, si je veux détruire 
# seulement dans le cas où il existe je peux aussi faire
try: 
    path.unlink()
except FileNotFoundError:
    print("no need to remove")

print("*"*100)  
dirpath = Path('F:\Python3\S3')
# tous les fichiers *.json dans le répertoire data/
for json in dirpath.glob("*.*"):
    print(json)
compteur = 0
for temoin in [ [], True, {}, "", None, False ] + list(range(3)):
    if temoin:
        print("temoin: ", temoin)
        compteur += 1
        
print(compteur)
n = 4
u = None
if 'a' in 'spam':
    if n == 10:
        print('non')
else:
    print('oui')